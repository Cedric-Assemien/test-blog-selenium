from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.db.models import Q

# Create your views here.
User = get_user_model()

# page inscription
def register(request):
    error = False
    message=''
    if request.method == 'POST':
        name = request.POST.get('name',None)
        email = request.POST.get('email',None)
        password1 = request.POST.get('password1',None)
        password2 = request.POST.get('password2',None)
        print(f"mon :{name} , email:{email} , mdp1:{password1}, mdp2:{password2}")
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False:
            if password1 != password2:
                error = True
                message = "Les deux mot de passe ne sont pas les même 🤦!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"
        
        # register
        if error == False:
            user = User(
                username = name,
                email = email,
            )
            user.save()

            user.password = password1
            user.set_password(user.password)
            user.is_active = False
            user.save()

            return redirect('sing_in')

    data={
    'register_active' :'active',
    'message' : message,
    'error': error,
    }
    
    return render(request,"account/register.html",data)