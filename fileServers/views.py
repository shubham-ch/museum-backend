from django.views.static import serve
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
# Create your views here.
from .serializers import FileSerializer
from .models import GeneralFile
from .filters import FileFilter
from rest_framework.decorators import api_view,permission_classes


class GeneralFileViewSet(CreateModelMixin,
                         ListModelMixin,
                         RetrieveModelMixin,
                         UpdateModelMixin,
                         DestroyModelMixin,
                         GenericViewSet,
                         ):
    serializer_class = FileSerializer
    queryset = GeneralFile.objects.all()
    filterset_class = FileFilter

class ServeFile(APIView):

    def get(self,request, path):
        return serve(request, path, settings.MEDIA_ROOT)    

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def ServeFile(request, path):
#     return serve(request, path, settings.MEDIA_ROOT)
