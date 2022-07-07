from django.db import models

class Class(models.Model):
    class_num = models.IntegerField('Class Number', primary_key=True, editable=True)
    strength = models.IntegerField('Strength')
    sections = models.IntegerField('Sections', default=3)
    subjects = models.CharField('Subjects', max_length=300)
    
class Teacher(models.Model):
    name = models.CharField('Name', max_length=100)
    subject = models.CharField('Subject', max_length=100)
    class_num = models.IntegerField('Class', editable=True)
    id = models.IntegerField('ID', primary_key=True, editable=True)

