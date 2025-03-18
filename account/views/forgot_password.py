from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

def forgot_password(request):
    error = False
    success = False
    message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
    
    context = {
        'success': success,
        'error':error,
        'message':message
    }
    return render(request, "account/forgot_password.html", context)