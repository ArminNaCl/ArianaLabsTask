from django.shortcuts import render
from apply.models import Apply
from apply.API import ApplySerializer
from rest_framework import generics, mixins

# Create your views here.

class ApplyList(generics.ListCreateAPIView):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer


