from django.conf.urls import patterns,url,include
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from models import Client,Job,Competency,Grade
from views import JobDetail, ClientDetail, GradeDetail, CompetencyDetail
from views import JobCreate, ClientCreate, GradeCreate, CompetencyCreate
from views import ClientDelete, GradeDelete, JobDelete, CompetencyDelete
from views import APIClientList, APIClientDetail, APIJobList, APIJobDetail, APIGradeList, APIGradeDetail, APICompetencyList, APICompetencyDetail
from forms import ClientForm, GradeForm, CompetencyForm, JobForm
from rest_framework.authtoken.views import obtain_auth_token
#from board.urls import router

#router = DefaultRouter()
#router.register(r'Client',views.ClientViewSet)
#router.register(r'Grade',views.GradeViewSet)

urlpatterns = [
    url(r'^$',ListView.as_view(
            queryset='',
            context_object_name='',
            template_name='JobApp/main.html'),name='Home'),
    url(r'^Job/$',
        ListView.as_view(
            queryset=Job.objects.all(),
            context_object_name='job_list',
            template_name='JobApp/Job_list.html'),
        name='Job_list'),

    url(r'^Job/(?P<pk>\d+)/delete/$',
        JobDelete.as_view(),
        name='Job_delete'),

    url(r'^Job/create/$',
        JobCreate.as_view(),
	name='Job_create'),
    url(r'^Job/(?P<pk>\d+)/$',
        JobDetail.as_view(),
        name='JobDetail')
        , 

     url(r'^Job/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
	    model = Job,
	    template_name = 'JobApp/form.html',
	    form_class = JobForm),
        name='Job_edit'),


    url(r'^Client/$',
        ListView.as_view(
            queryset=Client.objects.all(),
            context_object_name='client_list',
            template_name='JobApp/Client_list.html'),
        name='Client_list'),

    url(r'^Client/(?P<pk>\d+)/delete/$',
        ClientDelete.as_view(),
        name='Client_delete'),

    url(r'^Client/create/$',
        ClientCreate.as_view(),
	name='Client_create'),   


    url(r'^Client/(?P<pk>\d+)/$',
        ClientDetail.as_view(),
        name='ClientDetail'),


    url(r'^Client/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
	    model = Client,
	    template_name = 'JobApp/form.html',
	    form_class = ClientForm),
        name='Client_edit'),


    url(r'^Grade/$',
        ListView.as_view(
            queryset=Grade.objects.all(),
            context_object_name='grade_list',
            template_name='JobApp/Grade_list.html'),
        name='Grade_list'),

    url(r'^Grade/(?P<pk>\d+)/delete/$',
        GradeDelete.as_view(),
        name='Grade_delete'),

    url(r'^Grade/create/$',
        GradeCreate.as_view(),
	name='Grade_create'),
    url(r'^Grade/(?P<pk>\d+)/$',
        GradeDetail.as_view(),
        name='GradeDetail'),

    url(r'^Grade/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
	    model = Grade,
	    template_name = 'JobApp/form.html',
	    form_class = GradeForm),
        name='Grade_edit'),

    url(r'^Competency/$',
        ListView.as_view(
            queryset=Competency.objects.all(),
            context_object_name='competency_list',
            template_name='JobApp/Competency_list.html'),
        name='Competency_list'), 

    url(r'^Competency/(?P<pk>\d+)/delete/$',
        CompetencyDelete.as_view(),
        name='Competency_delete'),

     url(r'^Competency/create/$',
        CompetencyCreate.as_view(),
	name='Competency_create'),   
    url(r'^Competency/(?P<pk>\d+)/$',
        CompetencyDetail.as_view(),
        name='CompetencyDetail'),

    url(r'^Competency/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
	    model = Competency,
	    template_name = 'JobApp/form.html',
	    form_class = CompetencyForm),
        name='Competency_edit'),
    url(r'^api/job/$',APIJobList.as_view(),name='job-list'),
    url(r'^api/job/(?P<pk>\d+)/$',APIJobDetail.as_view(),name='job-detail'),
    url(r'^api/client/$',APIClientList.as_view(),name='client-list'),
    url(r'^api/client/(?P<pk>\d+)/$',APIClientDetail.as_view(),name='client-detail'),
    url(r'^api/grade/$',APIGradeList.as_view(),name='grade-list'),
    url(r'^api/grade/(?P<pk>\d+)/$',APIGradeDetail.as_view(),name='grade-detail'),
    url(r'^api/competency/$',APICompetencyList.as_view(),name='competency-list'),
    url(r'^api/competency/(?P<pk>\d+)/$',APICompetencyDetail.as_view(),name='competency-detail'),
        ]
 
    
