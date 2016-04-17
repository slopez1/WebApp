from django.conf.urls import patterns,url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import User,Job,Competency,Grade,Has_Grade,Has_Competency
from views import  JobDetail, UserDetail, GradeDetail, CompetencyDetail

from views import APIUserList, APIUserDetail, APIJobList, APIJobDetail, APIGradeList, APIGradeDetail, APICompetencyList, APICompetencyDetail

urlpatterns = patterns('',
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
    url(r'^Job/(?P<pk>\d+)/$',
        JobDetail.as_view(),
        name='JobDetail')
        , 
    url(r'^User/$',
        ListView.as_view(
            queryset=User.objects.all(),
            context_object_name='user_list',
            template_name='JobApp/User_list.html'),
        name='User_list'),    
    url(r'^User/(?P<pk>\d+)/$',
        UserDetail.as_view(),
        name='UserDetail')
        ,
    url(r'^Grade/$',
        ListView.as_view(
            queryset=Grade.objects.all(),
            context_object_name='grade_list',
            template_name='JobApp/Grade_list.html'),
        name='Grade_list'),
    url(r'^Grade/(?P<pk>\d+)/$',
        GradeDetail.as_view(),
        name='GradeDetail')
        ,
    url(r'^Competency/$',
        ListView.as_view(
            queryset=Competency.objects.all(),
            context_object_name='competency_list',
            template_name='JobApp/Competency_list.html'),
        name='Competency_list'),    
    url(r'^Competency/(?P<pk>\d+)/$',
        CompetencyDetail.as_view(),
        name='CompetencyDetail')
        ,
    #url(r'^api/$', 'api_root'),
    url(r'^api/job/$',APIJobList.as_view(),name='job-list'),
    url(r'^api/job/(?P<pk>\d+)/$',APIJobDetail.as_view(),name='job-detail'),
    url(r'^api/user/$',APIUserList.as_view(),name='user-list'),
    url(r'^api/user/(?P<pk>\d+)/$',APIUserDetail.as_view(),name='user-detail'),
    url(r'^api/grade/$',APIGradeList.as_view(),name='grade-list'),
    url(r'^api/grade/(?P<pk>\d+)/$',APIGradeDetail.as_view(),name='grade-detail'),
    url(r'^api/competency/$',APICompetencyList.as_view(),name='competency-list'),
    url(r'^api/competency/(?P<pk>\d+)/$',APICompetencyDetail.as_view(),name='competency-detail'),
        )
 
    
