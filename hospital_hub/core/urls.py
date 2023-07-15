from django.urls import path

from core import views


urlpatterns = [
    path('', views.home,name="home"),
    path("login/",views.loginpage,name="login"),
    path("logout",views.logoutUser,name="logout"),
    path("signup/",views.signuppage,name="signup"),
     path("dashbord/",views.dashbord,name="dashbord"),
     path("detail/<int:id>",views.detail,name="detail"),
     path("add-hospital/",views.add_Hospital,name="add-hospital")
]