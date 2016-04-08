from django.db import models

# Create your models here.

class User(models.Model):
    tipus = (('d','dona'),('h','home'))
    code_u=models.IntegerField()
    name=models.TextField(max_length = 50)
    age=models.IntegerField()
    gender=models.CharField(max_length=4,choices=tipus,unique=False)
    is_looking_for_job=models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return u"%i" % self.code_u
    def get_absolute_url(self):
        return reverse('JobApp:user_detail',kwargs={'pk':self.pk})
        
    

class Job(models.Model):
    tipus = (('p','primari'),('s','secundari'),('t','terciari'))
    code_j=models.IntegerField()
    name=models.TextField(max_length = 50)
    sector=models.CharField(max_length=15,choices=tipus,unique=False)
    
    def __unicode__(self):
        return  self.code_j
    def get_absolute_url(self):
        return reverse('JobApp:job_detail',kwargs={'pk':self.pk})    


class Grade(models.Model):
    tipus = (('C','Ciencies'),('L','Lletres'),('A','Art'))
    code_g=models.IntegerField()
    name_g=models.TextField(max_length = 50)
    area=models.CharField(max_length=15,choices=tipus,unique=False)
    description=models.TextField(max_length = 150)
    def __unicode__(self):
        return self.code_c
    def get_absolute_url(self):
       return reverse('JobApp:grade_detail',kwargs={'pk':self.pk})

class competency (models.Model):
    tipus = (('C','Ciencies'),('L','Lletres'),('A','Art'))
    code_c=models.IntegerField()
    name_c=models.TextField(max_length = 50)
    area=models.CharField(max_length=15,choices=tipus,unique=False)
    description=models.TextField(max_length = 150)
    def __unicode__(self):
        return self.code_c
    def get_absolute_url(self):
        return reverse('JobApp:competencies_detail',kwargs={'pk':self.pk})
    
class Has_Grade(models.Model):
    code_u=models.ForeignKey(User)
    code_g=models.ForeignKey(Grade)
    year_start=models.IntegerField()
    year_finished=models.IntegerField()

    
class Has_Competency(models.Model):
    code_u=models.ForeignKey(User)
    code_c=models.ForeignKey(Grade)
    experience_since_year=models.IntegerField()
    

