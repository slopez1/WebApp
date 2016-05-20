from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Grade(models.Model):
    tipus = (('Ciencies','Ciencies'),('Lletres','Lletres'),('Art','Art'))
    code_g=models.IntegerField()
    name_g=models.CharField(max_length = 50)
    area=models.CharField(max_length=15,choices=tipus,unique=False)
    description=models.TextField(max_length = 150)
    def __unicode__(self):
        return u"%s" % self.name_g
    def get_absolute_url(self):
        return reverse('JobApp:GradeDetail',kwargs={'pk':self.pk})


class Competency(models.Model):
    tipus = (('Ciencies','Ciencies'),('Lletres','Lletres'),('Art','Art'))
    code_c=models.IntegerField()
    name_c=models.CharField(max_length = 50)
    area=models.CharField(max_length=15,choices=tipus,unique=False)
    description=models.TextField(max_length = 150)
    def __unicode__(self):
        return u"%s" % self.name_c
    def get_absolute_url(self):
        return reverse('JobApp:CompetencyDetail',kwargs={'pk':self.pk})
    
 
class Client(models.Model):
	tipus = (('dona','dona'),('home','home'))
	code_u=models.IntegerField()
	name=models.CharField(max_length = 50)
	age=models.IntegerField()
	gender=models.CharField(max_length=4,choices=tipus,unique=False)
	zodiac_sign = models.CharField(default="Pisces", max_length=20)
	id_city =models.CharField(default="Lleida", max_length=50)
	is_looking_for_job=models.CharField(max_length = 30, blank=True, null=True)
	grades = models.ManyToManyField(Grade)
	competencies = models.ManyToManyField(Competency)
	def __unicode__(self):
		return u"%i" % self.code_u
	def get_absolute_url(self):
		return reverse('JobApp:ClientDetail',kwargs={'pk':self.pk})
        

class Job(models.Model):
	tipus = (('primari','primari'),('secundari','secundari'),('terciari','terciari'))
	code_j=models.IntegerField(unique=True)
	name=models.CharField(max_length = 50)
	sector=models.CharField(max_length=15,choices=tipus,unique=False)
	id_city =models.CharField(default="Lleida", max_length=50)
	grades = models.ManyToManyField(Grade)
	competencies = models.ManyToManyField(Competency)
	
	def __unicode__(self):
		return  u"%i" % self.code_j
	def get_absolute_url(self):
		return reverse('JobApp:JobDetail',kwargs={'pk':self.pk})    



