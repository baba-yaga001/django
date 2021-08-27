from django.shortcuts import render
from .models import Item,Team

# Create your views here.
def index(request):
    items = Item.objects.all()
    teams = Team.objects.all()
    return render(request,'index.html',{'items':items,'teams':teams})