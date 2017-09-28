from django.db import models
from django.db import IntegrityError
from django.core.validators import MinValueValidator, MaxValueValidator

from django_countries.fields import CountryField

n_situ = 12
n_items = n_situ * 5

# Create your models here.


class Subject(models.Model):
    SEX_CHOICES = (
        ('0', 'Mujer'),
        ('1', 'Hombre'))
    CIVIL_STATUS_CHOICES = (
        ('S', 'Soltero/a'),
        ('P', 'Con pareja'),
        ('C', 'Casado/a'),
        ('D', 'Divorciado/a (separado/a)'),
        ('V', 'Viudo/a'))
    LAST_STUDIES_CHOICES = (
        ('P', 'Primaria'),
        ('S', 'Secundaria'),
        ('B', 'Bachillerato'),
        ('FM', 'Formación profesional media'),
        ('FS', 'Formación profesional superior'),
        ('U', 'Universidad'))
    LIFE_SATISFACTION_CHOICES = [(n + 1, n + 1) for n in range(10)]

    first_time = models.BooleanField(default=True)
    code = models.CharField(max_length=46, blank=True)
    age = models.IntegerField(validators=[
        MinValueValidator(18), MaxValueValidator(100)])
    sex = models.CharField(max_length=2, choices=SEX_CHOICES)
    life_satisfaction = models.IntegerField(
        choices=LIFE_SATISFACTION_CHOICES, blank=True, null=True)
    civil_status = models.CharField(
        max_length=2, choices=CIVIL_STATUS_CHOICES, blank=True)
    last_studies = models.CharField(
        max_length=2, choices=LAST_STUDIES_CHOICES, blank=True)
    occupation = models.CharField(max_length=46, blank=True)
    home_country = CountryField(blank=True)
    home_city = models.CharField(max_length=46, blank=True)
    current_country = CountryField(blank=True)
    current_city = models.CharField(max_length=46, blank=True)
    postal_code = models.CharField(max_length=46, blank=True)
    n_items = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    total_time = models.FloatField(default=0)
    pre_score = models.IntegerField(default=0)
    ano_score = models.IntegerField(default=0)
    het_score = models.IntegerField(default=0)
    soc_score = models.IntegerField(default=0)
    sov_score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class Item(models.Model):

    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    situation_n = models.IntegerField()
    item_n = models.IntegerField()
    score = models.IntegerField()
    latency = models.FloatField()

    class Meta:
        unique_together = ('subject', 'situation_n', 'item_n')

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            owner = Subject.objects.get(id=self.subject.id)
            owner.n_items += 1
            if owner.n_items == n_items:
                owner.completed = True
            owner.total_time += self.latency
            if self.item_n == 0:
                owner.pre_score += self.score
            elif self.item_n == 1:
                owner.ano_score += self.score
            elif self.item_n == 2:
                owner.het_score += self.score
            elif self.item_n == 3:
                owner.soc_score += self.score
            elif self.item_n == 4:
                owner.sov_score += self.score
            owner.save()
        except IntegrityError:
            pass

    def __str__(self):
        return str(self.subject.id) + '_' + str(self.situation_n).zfill(2) + '_' + str(self.item_n)
