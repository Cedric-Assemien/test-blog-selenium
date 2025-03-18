from django.urls import path
from account.views.register import register
from account.views.sing_in import sing_in
from account.views.log_out import log_out
from account.views.forgot_password import forgot_password
from account.views.update_password import update_password
from account.views.active_compte import active_compte

urlpatterns = [
    path('register', register,name='register'),
    path('sing_in', sing_in,name='sing_in'),
    path('log_out', log_out,name='log_out'),
    path('forgot-password', forgot_password, name='forgot_password'),
    path('update-password/<str:token>/<str:user_id>', update_password, name='update_password'),
    path('update-password/<str:token>/<str:user_id>/active', active_compte, name='active_compte'),
]
