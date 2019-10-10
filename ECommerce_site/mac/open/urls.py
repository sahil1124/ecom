from django.conf.urls import url
# from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as  auth_views


app_name='open'

urlpatterns =[
    url(r'login/$',auth_views.LoginView.as_view(template_name='open/login.html'),name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'signup/$',views.Signup.as_view(),name='signup'),
    url(r'password_change/$', views.change_password, name='password_change'),
    url(r'password_change_done/$', views.change_password_done, name='password_change_done'),
    url(r'password_reset/$', auth_views.PasswordResetView.as_view(template_name='open/password_reset.html'), name='password_reset'),
    url(r'password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='open/password_reset_done.html'), name='password_reset_done'),
    url(r'password_reset/confirm/<uidb64>/<token>/$', auth_views.PasswordResetConfirmView.as_view(template_name='open/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'password_reset/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='open/password_reset_complete.html'), name='password_reset_complete'),
]
