from django.shortcuts import render
from decimal import Decimal

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

def add(request):
    if request.method=="POST":
        number1=request.POST.get('n1','')
        number2=request.POST.get('n2','')
        
        if not number1 or not number2:
            return render(request,"error.html")
        num1=Decimal(number1)
        num2=Decimal(number2)
        result=num1+num2
        return render(request,"result.html",{'res':result})
    else:
        return render(request,"error.html")

