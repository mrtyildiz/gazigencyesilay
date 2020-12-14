from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Etkinlik
from .models import Team
from .models import Yessem
def index(request):
    return render(request,'index.html')

def about(request):
    Etkinlik_all = Etkinlik.objects.all()
    return render(request,'about.html', {'Etkinlik_all':Etkinlik_all})

def team(request):
    Team_all = Team.objects.all()
    return render(request, 'team.html',{'Team_all':Team_all})

def yessem2020(request):
    Yessem_all = Yessem.objects.all()
    return render(request, 'yessem.html',{'Yessem_all':Yessem_all})