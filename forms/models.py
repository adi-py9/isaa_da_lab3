from operator import mod
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.TextField(max_length=200,null=True)
    email = models.EmailField(blank=False,null=True)
    #subject = models.CharField(max_length=256,null=True)
    message = models.TextField(null=True)
    D_o_b  = models.DateField(null=True)
    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', ('Freshman')
        SOPHOMORE = 'SO', ('Sophomore')
        JUNIOR = 'JR', ('Junior')
        SENIOR = 'SR', ('Senior')
        GRADUATE = 'GR', ('Graduate')
    year_in_school = models.CharField(max_length=2,
    choices=YearInSchool.choices,
    default=YearInSchool.FRESHMAN,)
    
    class Language(models.TextChoices):
        Tamil = 'tm', ('Tamil')
        Hindi = 'hn', ('Hindi')
        English = 'en', ('English')
    Language = models.CharField(max_length=2,
    choices=Language.choices,
    default=Language.English,)

    class Gender(models.TextChoices):
        Female = 'fm', ('Female')
        Male = 'ma', ('Male')
        Other = 'ot', ('Other')
    Gender = models.CharField(max_length=2,
    choices=Gender.choices,)

    


    