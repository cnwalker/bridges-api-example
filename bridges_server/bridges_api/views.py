from bridges_api.models import Question
from bridges_api.serializers import QuestionSerializer

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    """
    The response object is dank, and takes a python dictionary and
    renders it directly, no template necessary!
    """
    return Response({
        'questions': "No questions to display yet!"
    })

class QuestionList(generics.ListAPIView):
    """
    This uses that generic API list view to return a list
    of Question models as a response to GET requests. The queryset
    variable is the list of Question Models that ultimately gets
    serialized and returned to the User
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class = (permissions.IsAuthenticated,)

class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class = (permissions.IsAuthenticated,)
