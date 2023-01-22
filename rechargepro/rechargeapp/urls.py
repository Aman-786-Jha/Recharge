from django.urls import path 
from . import views 


urlpatterns = [
    path('index/',views.index,name='index'),
    path('true5g',views.true5g,name='true5g'),
    path('contactus/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('register/createData/',views.createData,name='craeteData'),
    path('login/login/',views.loginpage,name='loginpage'),
    path('logout/',views.logout,name='logout'),
    path('contactus/contact/',views.contactdetail,name='contactdetail'),
    path('login/login/afterlogin/',views.afterlogin,name='afterlogin'),
    path('index/subscribe/',views.subscribe,name='subscribe'),
    path('login/login/afterlogin/carddetails/',views.carddetails,name='carddetails'),
    path('allplans/',views.Allplans,name='allplans'),

    #API endpoint
    path('recommendedplans/',views.RecommendedPlans),
    path('hero-plans/',views.HeroPlans),
    path('otherplans/',views.OtherPlans)
    
]
