from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class User(models.Model):
    tipus = (('dona','dona'),('home','home'))
    code_u=models.IntegerField()
    name=models.TextField(max_length = 50)
    age=models.IntegerField()
    gender=models.CharField(max_length=4,choices=tipus,unique=False)
    is_looking_for_job=models.TextField(blank=True, null=True)
    def __unicode__(self):
        return u"%i" % self.code_u
    def get_absolute_url(self):
        return reverse('JobApp:UserDetail',kwargs={'pk':self.pk})
        

class Job(models.Model):
    tipus = (('primari','primari'),('secundari','secundari'),('terciari','terciari'))
    code_j=models.IntegerField(unique=True)
    name=models.TextField(max_length = 50)
    sector=models.CharField(max_length=15,choices=tipus,unique=False)
    def __unicode__(self):
        return  u"%i" % self.code_j
    def get_absolute_url(self):
        return reverse('JobApp:JobDetail',kwargs={'pk':self.pk})    


class Grade(models.Model):
    tipus = (('Ciencies','Ciencies'),('Lletres','Lletres'),('Art','Art'))
    code_g=models.IntegerField()
    name_g=models.TextField(max_length = 50)
    area=models.CharField(max_length=15,choices=tipus,unique=False)
    description=models.TextField(max_length = 150)
    def __unicode__(self):
        return u"%i" % self.code_g
    def get_absolute_url(self):
        return reverse('JobApp:GradeDetail',kwargs={'pk':self.pk})


class Competency(models.Model):
    tipus = (('Ciencies','Ciencies'),('Lletres','Lletres'),('Art','Art'))
    code_c=models.IntegerField()
    name_c=models.TextField(max_length = 50)
    area=models.CharField(max_length=15,choices=tipus,unique=False)
    description=models.TextField(max_length = 150)
    def __unicode__(self):
        return u"%i" % self.code_c
    def get_absolute_url(self):
        return reverse('JobApp:CompetencyDetail',kwargs={'pk':self.pk})
    
    
class Has_Grade(models.Model):
    code_u=models.ForeignKey(User,null=False,related_name='grades')
    code_g=models.ForeignKey(Grade)
    year_start=models.IntegerField()
    year_finished=models.IntegerField()

    
class Has_Competency(models.Model):
    code_u=models.ForeignKey(User,related_name='competencies')
    code_c=models.ForeignKey(Competency,)
    experience_since_year=models.IntegerField()
    

class Need_Grade(models.Model):
    code_j = models.ForeignKey(Job,related_name="grades")
    code_g = models.ForeignKey(Grade)
    
   
class Need_Competency(models.Model):
    code_j = models.ForeignKey(Job,related_name="competencies")
    code_c = models.ForeignKey(Competency)
    

