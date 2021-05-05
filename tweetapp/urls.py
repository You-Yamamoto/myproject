from .views import signupfunc, loginfunc , listfunc , logoutfunc , detailfunc , readfunc , BoardCreate 
from django.urls import path 

urlpatterns = [
    path('signup/', signupfunc, name = 'signup' ),
    path('' , loginfunc, name = 'login'),
    path('list/' , listfunc, name = 'list'),
    path('logout/' , logoutfunc, name = 'logout'),
    path('detail/<int:pk>', detailfunc, name = 'detail' ),
    path('read/<int:pk>' , readfunc, name = 'read'),
    path('create/' , BoardCreate.as_view(), name = 'create'),
    
]