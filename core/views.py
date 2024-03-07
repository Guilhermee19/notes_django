from rest_framework import generics

from .models import Note
from .serializers import NoteSerializer

class NotesViewSet(generics.ListCreateAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  
class NoteViewSet(generics.RetrieveUpdateDestroyAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer