from rest_framework import serializers
from .models import Audio, Charset
import re
from rest_framework.exceptions import ParseError


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('id', 'name', 'transcription', 'annotator', 'transcribed', 'details', 'tags', 'url')



    def update(self, instance, validated_data):
        instance.transcription = validated_data.get('transcription', None)
        instance.name = validated_data.get('name', None)
        instance.url = validated_data.get('url', None)
        instance.transcribed = validated_data.get('transcribed', None)
        instance.details = validated_data.get('details', None)
        instance.tags = validated_data.get('tags', None)
        instance.annotator = validated_data.get('annotator', None)


        charSet = Charset.objects.first()
        if (not (re.match(r"^["+charSet.data+"]+$", instance.transcription))):
            raise ParseError("Invalid characters in transcription")

        if (not (re.match(r"^[A-Z]+$", instance.transcription))):
            instance.transcription = (". ".join(i.capitalize() for i in instance.transcription.split(". ")))

        instance.transcription = ' '.join(instance.transcription.split())
        instance.save()
        return instance



    def create(self, validated_data):
        name = validated_data.get('name', None)
        name = ' '.join(name.split())
        transcription = ''
        validated_data.pop('name')
        validated_data.pop('transcription')
        return Audio.objects.create(name=name, transcription=transcription, **validated_data)
