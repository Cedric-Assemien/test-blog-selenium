from django.shortcuts import render

def about(request):
    datas = {
        "active_about": 'active'
    }

    return render(request, 'about.html', datas)