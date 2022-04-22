from . import views
from django.urls import path
from django.contrib.auth import views as authViews
from frontend.views import Signup
urlpatterns=[
    path('',views.list,name="list"),
    path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
    path('signup/', Signup, name='signup'),
]