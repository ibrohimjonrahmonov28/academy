from django.shortcuts import render
from .models import Shop,Category,Barber
# Create your views here.
def get_shop(request):
    shops=Shop.objects.all()
    context={"shops":shops}
    return render(request, "main.html",context=context)

def get_category(request, shop_id):
    categories=Category.objects.filter(shop_id=shop_id)
    context={"categories":categories}
    return render(request, "second.html",context=context)

def get_barber(request, barber_id):
    barbers=Barber.objects.filter(barber_id=barber_id)
    context={"barbers":barbers}
    return render(request, "tirty.html",context=context)

def get_add(request):
    return render(request,"add.html")

    
# TODO savol nimaga get groups ga pk qoyilsa idlarni aralishtirib yuboryapti 
# 