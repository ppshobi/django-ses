from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class DeepThoughtView(View):

    def get(self, request):
        return HttpResponse(42)