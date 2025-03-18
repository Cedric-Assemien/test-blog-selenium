from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Create your views here.
User = get_user_model()

def update_password(request, token, user_id):
    print(f"Token: {token}, User ID: {user_id}")
    user = None
    message = ""
    success = False
    error = False

    try:
        decode_user_id = int(urlsafe_base64_decode(user_id).decode('utf-8'))
        user = User.objects.filter(id=decode_user_id).first()
        

        if user is None:
            message = "Utilisateur introuvable."
            error = True
        elif not default_token_generator.check_token(user, token):
            message = "Lien de réinitialisation invalide ou expiré."
            error = True
        else:
            if request.method == "POST":
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')

                if password1 and password2:
                    if password1 == password2:
                        try:
                            validate_password(password1, user)
                            user.set_password(password1)
                            user.is_active=True
                            user.save()
                            
                            success = True
                            message = "Votre mot de passe a été modifié avec succès !"
                        except ValidationError as e:
                            error = True
                            message = " ".join(e.messages)
                    else:
                        error = True
                        message = "Les mots de passe ne correspondent pas."
                else:
                    error = True
                    message = "Veuillez remplir les deux champs de mot de passe."

    except (ValueError, TypeError, OverflowError):
        message = "Lien de réinitialisation invalide."
        error = True

    context = {
        'success': success,
        'message': message,
        'user': user,
        'error': error,
    }

    return render(request, "account/update_password.html", context)