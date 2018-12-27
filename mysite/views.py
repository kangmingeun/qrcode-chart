from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse

from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.views.generic import CreateView, TemplateView
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse_lazy
# from django.contrib.auth.models import User

# Create your views here.

User = get_user_model()


def index(request):
    template = loader.get_template('index/index.html')
    value = request.GET.get('value')
    buy = request.GET.get('buy')
    sell = request.GET.get('sell')
    context = {

        'latest_question_list': "test",
        "value" : value,
        "buy" : buy,
        "sell" : sell,
    }
    return HttpResponse(template.render(context, request))
    


# def intro(request):
#     template = loader.get_template('intro.html')
#     context = {
#         'latest_question_list': "test",
#     }
#     return HttpResponse(template.render(context, request))


# def map(request):
#     template = loader.get_template('map.html')
#     context = {
#         'latest_question_list': "test",
#     }
#     return HttpResponse(template.render(context, request))

# check logged user
# class LoginRequiredMixin(object):
#     @classmethod
#     def as_view(cls, **initkwargs):
#         view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
#         return login_required(view)
