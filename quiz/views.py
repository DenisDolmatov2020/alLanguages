from rest_framework import viewsets
from quiz.models import Question, Answer
from my_user.models import User
from quiz.serializers import QuestionSerializer, AnswerSerializer
from my_user.serializers import UserSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
