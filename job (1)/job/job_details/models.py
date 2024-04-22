from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.TextField()
    requirements = models.TextField()
    app_deadline = models.DateField()

    class Meta:
        db_table = 'Job'
    

class Apply(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    ten_marks = models.DecimalField(decimal_places=2, max_digits = 5)
    twelve_marks = models.DecimalField(decimal_places=2, max_digits = 5)
    yoe = models.IntegerField()

    class Meta:
        db_table = 'Apply'