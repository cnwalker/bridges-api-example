from django.contrib.auth.models import User
from rest_framework import serializers
from bridges_api.models import Question, UserProfile

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('title', 'description', 'answer', 'tags', 'number_of_views')
