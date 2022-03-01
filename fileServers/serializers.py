from rest_framework import serializers
from .models import GeneralFile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=GeneralFile
        fields=["general_file"]

    def create(self, validated_data):
        file_name = validated_data["general_file"].name
        instance = GeneralFile.objects.create(**validated_data, file_name=file_name, file_type=file_name.split(".")[1])
        return instance
