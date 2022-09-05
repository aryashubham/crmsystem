from django.db import models




# Create your models here.
Source_Choice = (
    ('Facebook', 'Facebook'),
    ('Instagram', 'Instagram'),
    ('Youtube', 'Youtube')
)

class Lead(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=Source_Choice,max_length=250)
    profile_picture = models.ImageField(blank=True, null=True)
    special_file = models.FileField(null=True, blank=True)