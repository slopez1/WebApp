from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Job, User, Grade, Competency


class UserSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name = 'JobApp:user-detail')
    class Meta:
        model = User
        fields = ('url', 'code_u', 'name', 'age', 'gender', 'is_looking_for_job')


class JobSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name = 'JobApp:job-detail')
    class Meta:
        model = Job
        fields = ('url', 'code_j', 'name', 'sector')

class GradeSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name = 'JobApp:grade-detail')
    class Meta:
        model = Grade
        fields = ('url', 'code_g', 'name_g', 'area', 'description')


class CompetencySerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name = 'JobApp:competency-detail')
    class Meta:
        model = Competency
        fields = ('url', 'code_c', 'name_c', 'area', 'description')
