from django.urls import path
from .views import NoteViewSet, NotesViewSet

urlpatterns = [
  path('note/', NotesViewSet.as_view()),
  path('note/<int:pk>/', NoteViewSet.as_view()),
]