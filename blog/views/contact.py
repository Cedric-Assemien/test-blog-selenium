from django.shortcuts import render



def contact(request):
    datas = {
        "active_contact": 'active'
    }

    return render(request, 'contact.html', datas)