from django.shortcuts import render
from django.http import HttpResponse

import json
 
def qrcode(request):
    return render(request, 'qr_index.html', ({}))

def transfer(request):
    print("결제되었음")
