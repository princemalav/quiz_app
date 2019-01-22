from django.conf.urls import url
from . import views

app_name = 'quiz_app'
urlpatterns = [
    url(r'homepage',views.homepageview,name='homepage'),
    url(r'register',views.register,name='register'),
    url(r'login',views.user_login,name='login')
]
