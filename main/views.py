from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Note,SharedNote
from .serializers import NotesSerializer,SharedNoteSerializer
from rest_framework import filters
from .permissions import IsOwnerOrReadOnly,SharedOwnerOrReadOnly
from django.db.models import Q

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def my_notes(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
    
class ShareNoteViewSet(viewsets.ModelViewSet):
    queryset = SharedNote.objects.all()
    serializer_class = SharedNoteSerializer
    permission_classes = [IsAuthenticated,SharedOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save() 
        
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(Q(receiver=self.request.user) | Q(note__user=self.request.user)) 