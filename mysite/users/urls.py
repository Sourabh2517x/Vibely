
from django.urls import path
from . import views
from .views import LogoutGetView,register,edit,ProfileView,personalprofile
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('logout/', LogoutGetView.as_view(template_name='users/index.html'), name="logout"),
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name="login"),
    path('password_change',PasswordChangeView.as_view(template_name='users/password_change.html'),name='password_change'),
    path('password_change/done',PasswordChangeDoneView.as_view(template_name='users/personal.html'),name='password_change_done'),
    path('password_reset',PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path("password_reset/done/", PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
    path("reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name="password_reset_confirm"),
    path("password_reset/complete",PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name="password_reset_complete"),
    path("register/",views.register,name="register"),
    path('edit/',views.edit,name="edit"),
    path('profile/',views.personalprofile,name="profile"),
    path('personal/',views.ProfileView,name="personal"),
    path('<int:id>', views.delete, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)