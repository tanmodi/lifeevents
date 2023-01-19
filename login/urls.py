from django.urls import path
from . import views
urlpatterns = [
    path('userregister',views.userregister,name='userregister'),
    path('main',views.main,name='main'),
    path('success',views.success,name='success'),
    path('login',views.login,name='login'),
    path('multilogin',views.multilogin,name='multilogin'),
    path('genmotp',views.genmotp,name='genmotp'),
    path('otp',views.otp,name='otp'),
    path('veriotp',views.veriotp,name='veriotp'),
    path('geneotp',views.geneotp,name='geneotp'),
    path('eotp',views.eotp,name='eotp'),
    path('verieotp',views.verieotp,name='verieotp'),
    path('password',views.password,name='password'),
    path('verilogin',views.verilogin,name='verilogin'),
    path('dsuccess',views.dsuccess,name='dsuccess'),
    path('logout',views.logout,name='logout'),
    path('uabout',views.uabout,name='uabout'),
    path('ucontact',views.ucontact,name='ucontact'),
    path('ufaq',views.ufaq,name='ufaq'),
    path('ublog',views.ublog,name='ublog'),
    path('ureply',views.ureply,name='ureply'),
    path('usearchcity',views.usearchcity,name='usearchcity'),
    path('usearchpro',views.usearchpro,name='usearchpro'),
    path('usearchresult',views.usearchresult,name='usearchresult'),
    path('uspeaker',views.uspeaker,name='uspeaker'),
    path('register',views.register,name='register'),
    path('mail',views.mail,name='mail'),
    #path('comfirm',views.)
]
