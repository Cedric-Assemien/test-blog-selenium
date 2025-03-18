from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode

# Create your views here.
User = get_user_model()

def active_compte(request, token, user_id):
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
            user.is_active=True
            user.save()
            message = "votre compte est actif "
            success = True
    except (ValueError, TypeError, OverflowError):
        message = "Lien de réinitialisation invalide."
        error = True

    context = {
        'success': success,
        'message': message,
        'user': user,
        'error': error,
    }

    return render(request, "account/active_password.html", context)