from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response


User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # qs_count = User.objects.all().count()
        labels = ["사용자", "숙박", "레저", "음식"]
        labels_second = ['10대', '20대','30대','40대','50대','60대']
        default_items = [70, 45, 35, 25]
        default1_items = [70, 20 ,20, 10, 15,5]
        data = {
                "labels": labels,
                "default": default_items,
                "labels_second" : labels_second,
                "default1": default1_items,
        }
        return Response(data)



