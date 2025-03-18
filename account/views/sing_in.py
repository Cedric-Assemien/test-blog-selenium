from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login

# Create your views here.
User = get_user_model()

# page inscription
def sing_in(request):
    error = False
    message=''
    if request.method == 'POST':
        email =request.POST.get('email',None)
        password = request.POST.get('password',None)
        user = User.objects.filter(email=email).first()
        if user:
            if user.is_active==True:
                if user:
                    auth_user = authenticate(username=user.username, password=password)
                    if auth_user:
                        login(request, auth_user)
                        return redirect('index')
                    else:
                        error = True
                        message = "mot de passe incorrecte"
                        print("mot de passe incorrecte")
                else:
                    error = True
                    message = "L'utilisateur n'existe pas !"
                    print("L'utilisateur n'existe pas !")
            else:
                error = True
                message = "votre compte n'est pas actif"
                print("votre compte n'est pas actif")
        else:
            error = True
            message = "Veuillez vérifier vos informations"
    
    data={
    'sing_in_active' :'active',
    'message' : message,
    'error': error,
    }
    return render(request,"account/login.html",data)