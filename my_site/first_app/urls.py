from django.urls import path 
from . import views 
 
 #first_app/
urlpatterns = [
    #  path('',views.simple_view)
    #  path('simple_view',views.simple_view)
    path('sports/',views.sports_view),
    path('finance/',views.finance_view)


   ]