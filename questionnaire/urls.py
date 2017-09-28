from django.conf.urls import url
from . import views

app_name = 'questionnaire'

urlpatterns = [
    url(r'index/$', views.index_view, name="index"),
    url(r'first_time/$', views.first_time_view, name="first_time"),
    url(r'subject/$', views.subject_view, name="subject"),
    url(r'guidelines/$', views.guidelines_view, name="guidelines"),
    url(r'situation/(?P<s>[0-9]+)/(?P<i>[0-9]+)/$',
        views.situation_view, name='situation'),
    url(r'item/(?P<s>[0-9]+)/(?P<i>[0-9]+)/$', views.item_view, name='item'),
    url(r'results/$', views.results_view, name="results"),
    url(r'regulation/$', views.regulation_view, name="regulation"),
    url(r'about_us/$', views.about_us_view, name="about_us"),
    url(r'the_end/$', views.the_end_view, name="the_end")]
