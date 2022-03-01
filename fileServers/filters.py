from django_filters import rest_framework as filters
from .models import GeneralFile
from rest_framework.permissions import IsAuthenticated

class FileFilter(filters.FilterSet):

    permission_classes = [IsAuthenticated]

    file_name=filters.CharFilter(field_name="file_name")

    class Meta:
        model= GeneralFile
        fields=(
            "file_name",
        )
