from django.urls import path 
from .views import ProfileListView , ProfileDetailView

urlpatterns = [
    path('profiles/', ProfileListView.as_view(), name = 'profile-list-view' ),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name = 'zibun' ),

]