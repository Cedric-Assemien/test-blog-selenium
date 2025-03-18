from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#page acceuille
@login_required(login_url='sing_in')
def home(request):
    data={
        'home_active' :'active',
    }
    return render(request,"account/home.html",data)