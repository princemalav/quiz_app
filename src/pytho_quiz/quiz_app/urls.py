from django.conf.urls import url
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'quiz_app'
urlpatterns = [
    url(r'homepage',views.homepageview,name='homepage'),
    url(r'register',views.register,name='register'),
    url(r'login',views.user_login,name='login'),
    url(r'logout',views.user_logout,name='logout'),
    url(r'question',views.question_view,name='question'),
    url(r'answer',views.check_answer,name='answer'),
]
