from django.urls import path
from .views import helloview,contact, productdelete,signup,loginview,home,profile,signupview,proall,productview,searchview,aboutview,productdelete,logout

urlpatterns = [
    path('hello/',helloview,name='hello'),
    path('contact/',contact,name='contact'),
    path('signup/',signup,name='signup'),
    path('login/',loginview,name='login'),
    path('home/',home,name='home'),
    path('profile/',profile,name='profile'),
    path('register/',signupview,name='register'),
    path('view/<int:abc>/',productview,name='proview'),
    path('',proall,name='proall'),
    path('search/',searchview,name='search'),
    path('about/',aboutview,name='about'),
    path('del/<int:abc>/',productdelete,name='prodel'),
    path('logout/',logout,name='logout')
]