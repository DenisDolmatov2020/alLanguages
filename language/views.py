from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from language.models import Language

from language.serializers import LanguageSerializer


class LanguageListView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

