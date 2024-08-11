from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django import forms



def calculation(request):
    num1=""
    result=""
    try:
        if request.method == 'POST':
            num1 = int(request.POST.get("input1"))
            
            if num1%2==0:
               result="EVEN"
            else:
                result="ODD"
    except:
        print("ERRROOORRR")

    print(result)
    return render(request,"pages/home.html",{"num1":num1,"result":result})