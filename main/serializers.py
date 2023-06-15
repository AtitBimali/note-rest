from rest_framework import serializers
from .models import Note,SharedNote


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class SharedNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedNote
        fields = "__all__"