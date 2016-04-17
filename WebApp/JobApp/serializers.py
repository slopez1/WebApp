from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Job, User, Grade, Competency


class UserSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name = 'JobApp:UserDetail')
    grades_set = HyperlinkedRelatedField(many = True, read_only = True, view_name = 'JobApp:GradeDetail')
    competencies_set = HyperlinkedRelatedField(many = True, read_only = True, view_name = 'JobApp:CompetencyDetail')
    class Meta:
        model = User
        fields = ('url', 'code_u', 'name', 'age', 'gender', 'is_looking_for_a_job', 'grades_set', 'competencies_set')


class JobSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name = 'JobApp:JobDetail')
    grades_set = HyperlinkedRelatedField(many = True, read_only = True, view_name = 'JobApp:GradeDetail')
    competencies_set = HyperlinkedRelatedField(many = True, read_only = True, view_name = 'JobApp:CompetencyDetail')
    class Meta:
        model = Job
        fields = ('url', 'code_j', 'name', 'sector', 'grades_set', 'competencies_set')

class GradeSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name = 'JobApp:GradeDetail')
    class Meta:
        model = Grade
        fields = ('url', 'code_g', 'name', 'area', 'description')


class CompetencySerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name = 'JobApp:CompetencyDetail')
    class Meta:
        model = Competency
        fields = ('url', 'code_c', 'name', 'area', 'description')
