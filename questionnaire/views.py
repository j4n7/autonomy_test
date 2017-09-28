# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from .models import Subject, Item
from .forms import FirstTimeForm, SubjectForm, ItemForm

from .test_items import *
from .radar_chart import *

import base64
from random import shuffle
from datetime import datetime
from io import BytesIO


n_situ = 12


def request_session(name, request):
    if name in request.session:
        return request.session[name]

# Create your views here.


def index_view(request):
    return render(request, 'questionnaire/index.html')


def first_time_view(request):
    if request.method == 'POST':
        form = FirstTimeForm(request.POST)
        form.label_classes = ('custom-control', 'custom-radio', )
        if form.is_valid():
            request.session['first_time'] = form.cleaned_data['first_time']

            return redirect('questionnaire:subject')
    else:
        form = FirstTimeForm()
        form.label_classes = ('custom-control', 'custom-radio', )

    return render(request, 'questionnaire/first_time.html', {
        'form': form})


def subject_view(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            # "commit=False" tells Django: "don't send this to database yet."
            subject = form.save(commit=False)
            subject.first_time = request_session('first_time', request)
            subject.save()
            request.session['subject_id'] = subject.id

            return redirect('questionnaire:guidelines')
    else:
        form = SubjectForm()

    return render(request, 'questionnaire/subject.html', {
        'form': form})


def guidelines_view(request):
    situ_order = list(range(n_situ))
    item_order = list(range(5))
    shuffle(situ_order)
    shuffle(item_order)
    current_s = situ_order[0]
    current_i = item_order[0]
    del situ_order[0]
    del item_order[0]
    request.session['situ_order'] = situ_order
    request.session['item_order'] = item_order

    return render(request, 'questionnaire/guidelines.html', {
        'current_s': current_s,
        'current_i': current_i})


def situation_view(request, s, i):
    current_s = int(s)
    current_i = int(i)
    situation = situations[current_s]
    if request.method == 'POST':
        request.session['time'] = str(datetime.now())

        return redirect('questionnaire:item', current_s, current_i)

    return render(request, 'questionnaire/situation.html', {
        'situation': situation})


def item_view(request, s, i):
    s = int(s)
    i = int(i)
    situation = situations[s]
    item = items[s][i]

    subject_id = request_session('subject_id', request)
    situ_order = request_session('situ_order', request)
    item_order = request_session('item_order', request)
    time = datetime.strptime(request_session('time', request),
                             '%Y-%m-%d %H:%M:%S.%f')

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = Item()
            subject = Subject.objects.get(id=subject_id)
            item.subject = subject
            item.situation_n = s
            item.item_n = i
            item.score = form.cleaned_data['slider']
            item.latency = float((datetime.now() - time).total_seconds())
            item.save()

            request.session['time'] = str(datetime.now())

            if situ_order:
                if item_order:
                    '''Only item changes'''
                    current_s = s
                    current_i = item_order[0]
                    del item_order[0]
                    request.session['item_order'] = item_order
                    return redirect('questionnaire:item', current_s, current_i)
                else:
                    '''Both situation and item change'''
                    item_order = list(range(5))
                    shuffle(item_order)
                    current_s = situ_order[0]
                    current_i = item_order[0]
                    del situ_order[0]
                    del item_order[0]
                    request.session['situ_order'] = situ_order
                    request.session['item_order'] = item_order
                    return redirect('questionnaire:situation', current_s, current_i)
            else:
                if item_order:
                    '''Only item changes'''
                    current_s = s
                    current_i = item_order[0]
                    del item_order[0]
                    request.session['item_order'] = item_order
                    return redirect('questionnaire:item', current_s, current_i)
                else:
                    '''The End'''
                    return redirect('questionnaire:results')
    else:
        form = ItemForm()

    return render(request, 'questionnaire/item.html', {
        'situation': situation,
        'item': item,
        'form': form})


def results_view(request):
    subject_id = request_session('subject_id', request)
    subject = Subject.objects.get(id=subject_id)

    max_score = 100 * n_situ

    def scale_score(score):
        return (score * 100) / max_score

    pre_score = scale_score(subject.pre_score)
    ano_score = scale_score(subject.ano_score)
    het_score = scale_score(subject.het_score)
    soc_score = scale_score(subject.soc_score)
    sov_score = scale_score(subject.sov_score)

    stages = ['Prenomía', 'Anomía', 'Heteronomía',
              'Soc. Comp.', 'Soc. Vinc.']
    scores = [pre_score, ano_score, het_score, soc_score, sov_score]

    theta = radar_factory(5, frame='polygon')

    fig, axes = plt.subplots(figsize=(10, 10), nrows=1, ncols=1,
                             subplot_kw=dict(projection='radar'))
    axes.set_xlim([0, 100])
    axes.set_ylim([0, 100])
    axes.set_rgrids([20, 40, 60, 80])
    axes.set_title(
        'Autonomía', weight='bold', size='xx-large', position=(0.5, 1.1),
        horizontalalignment='center', verticalalignment='center')
    axes.plot(theta, scores, color='b')
    axes.fill(theta, scores, facecolor='b', alpha=0.25)
    axes.set_varlabels(stages)

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    figdata_png = figfile.getvalue()  # extract string (stream of bytes)
    figdata_png = base64.b64encode(figdata_png)
    plt.close()  # this might help to free memory

    return render(request, 'questionnaire/results.html', {
        'pre_score': pre_score,
        'ano_score': ano_score,
        'het_score': het_score,
        'soc_score': soc_score,
        'sov_score': sov_score,
        'figdata_png': figdata_png})


def regulation_view(request):
    return render(request, 'questionnaire/regulation.html')


def about_us_view(request):
    return render(request, 'questionnaire/about_us.html')


def the_end_view(request):
    return render(request, 'questionnaire/the_end.html')
