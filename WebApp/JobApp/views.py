from django.shortcuts import render
from django.core.urlresolvers import reverse 
from django.http  import  HttpResponseRedirect
from django.shortcuts  import  get_object_or_404
from django.views.generic import DetailView, ListView,DeleteView
from django.views.generic.edit import CreateView
from models import Client,Job,Competency,Grade


from rest_framework import generics,authentication,permissions,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.core.urlresolvers import reverse_lazy
from serializers import ClientSerializer, JobSerializer, GradeSerializer, CompetencySerializer

from django.contrib.auth import get_user_model




from forms import JobForm, ClientForm, GradeForm, CompetencyForm


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API
    """
    return Response({
        'Client': reverse('client-list', request=request),
        'Job': reverse('job-list', request=request),
        'Grade': reverse('grade-list', request=request),
        'Competency': reverse('competency-list', request=request),

    })






#Details##############################################################################################################################################################
class JobDetail(DetailView):
    model = Job
    template_name = 'JobApp/Job_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(JobDetail, self).get_context_data(**kwargs)
        #context['RATING_CHOICES'] =	RestaurantReview.RATING_CHOICES
        return context

class ClientDetail(DetailView):
    model = Client
    template_name = 'JobApp/Client_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(ClientDetail, self).get_context_data(**kwargs)
        #context['RATING_CHOICES'] =	RestaurantReview.RATING_CHOICES
        return context


class GradeDetail(DetailView):
    model = Grade
    template_name = 'JobApp/Grade_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(GradeDetail, self).get_context_data(**kwargs)
        #context['RATING_CHOICES'] =	RestaurantReview.RATING_CHOICES
        return context


class CompetencyDetail(DetailView):
    model =	Competency
    template_name = 'JobApp/Competency_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(CompetencyDetail, self).get_context_data(**kwargs)
        #context['RATING_CHOICES'] =	RestaurantReview.RATING_CHOICES
        return context
##############################################################################################################################################################



####LIST#######################################################################################
class JobList(ListView):
	queryset=Job.objects.all()
	context_object_name='job_list'
        template_name='JobApp/Job_list.html'

class ClientList(ListView):
	queryset=Client.objects.all()
        context_object_name='client_list'
        template_name='JobApp/Client_list.html'

class GradeList(ListView):
	 queryset=Grade.objects.all()
         context_object_name='grade_list'
         template_name='JobApp/Grade_list.html'

class CompetencyList(ListView):
	queryset=Competency.objects.all()
        context_object_name='competency_list'
        template_name='JobApp/Competency_list.html'


      




##############################################################################################################################################################

#DELETE##############################################################################################################################################################
class JobDelete(DeleteView):
	model = Job
	success_url ="../.."

class ClientDelete(DeleteView):
	model = Client
	success_url ="../.."


class GradeDelete(DeleteView):
	model = Grade
	success_url ="../.."

class CompetencyDelete(DeleteView):
	model = Competency
	success_url ="../.."

#######################################################################################################################################################


#Create############################################################################################################################
class JobCreate(CreateView):
	model=Job
	template_name='JobApp/form.html'
	form_class = JobForm
	
	def form_valid(self, form):
		form.instance.user =  self.request.user
		form.instance.code_j =  Job.objects.latest('id').id+1
		return super(JobCreate, self).form_valid(form)

class ClientCreate(CreateView):
	model= Client
	template_name='JobApp/form.html'
	form_class = ClientForm
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.code_u = Client.objects.latest('id').id+1

		return super(ClientCreate, self).form_valid(form)

class GradeCreate(CreateView):
	model= Grade
	template_name='JobApp/form.html'
	form_class = GradeForm
	
	def form_valid(self, form):
		form.instance.user =  self.request.user
		form.instance.code_g =  Grade.objects.latest('id').id+1
		return super(GradeCreate, self).form_valid(form)




class CompetencyCreate(CreateView):
	model= Competency
	template_name='JobApp/form.html'
	form_class = CompetencyForm
	
	def form_valid(self, form):
		form.instance.user =  self.request.user
		form.instance.code_c =  Competency.objects.latest('id').id+1
		return super(CompetencyCreate, self).form_valid(form)

############################################################################################################################












##API####################################################################
class APIClientList(generics.ListCreateAPIView):
    queryset=Client.objects.all()
    model = Client
    serializer_class = ClientSerializer


class APIClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Client.objects.all() 
    model = Client
    serializer_class = ClientSerializer

    
class APIJobList(generics.ListCreateAPIView):
    queryset=Job.objects.all()
    model = Job
    serializer_class = JobSerializer


class APIJobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Job.objects.all()
    model = Job
    serializer_class = JobSerializer

    
    
class APIGradeList(generics.ListCreateAPIView):
    queryset=Grade.objects.all()
    model = Grade
    serializer_class = GradeSerializer
    


class APIGradeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Grade.objects.all()
    model = Grade
    serializer_class = GradeSerializer

    
class APICompetencyList(generics.ListCreateAPIView):
    queryset=Competency.objects.all()
    model = Competency
    serializer_class = CompetencySerializer


class APICompetencyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Competency.objects.all()
    model = Competency
    serializer_class = CompetencySerializer
