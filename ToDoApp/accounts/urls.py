from django.contrib import admin
from django.urls import path

from .views import *
# from django.contrib.auth.views import password_reset
# from .views import (
#     #
#     LoginView,
#     LogoutView,
#     home,
#     register,
#     profile,
#     edit_profile,
#     change_password,
#     PasswordResetView,
#     PasswordResetDoneView
# )
# from django.contrib.auth.views import LoginView



# app_name = 'Login_page'

urlpatterns = [

    path('',home),
    path('login/', LoginView.as_view(),name = 'login'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    path('register/',register ,name = 'register'),
    path('profile/',profile, name = 'profile'),
    path('profile/edit',edit_profile, name = 'edit_profile'),
    path('profile/change-password',change_password, name = 'change-password'),
    path('password-reset/',PasswordResetView.as_view(), name = 'password-reset'),
    path('password-reset/done/',PasswordResetDoneView.as_view(), name = 'password-reset-done'),
    path('password-reset/comfirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password-reset-confirm')



]
