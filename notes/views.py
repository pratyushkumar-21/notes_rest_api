from django.shortcuts import render
from rest_framework import generics
from notes.models import Notes
from notes.serializers import NotesSerializer

# Create your views here.
class NotesListCreateAPIView(generics.ListCreateAPIView):
    queryset=Notes.objects.all()
    serializer_class=NotesSerializer

class NotesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Notes.objects.all()
    serializer_class=NotesSerializer
    lookup_field='id'
