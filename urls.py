from django.urls import path 
from . import views


urlpatterns = [
    path('',views.homepage,name='home'),
    path('farmer/',views.farmer,name='farmer'),
    path('fisherman/',views.fisherman,name='fisherman'),
    path('adminpage/',views.adminpage,name='adminpage'), 
    path('checkuser/',views.checkuser,name='checkuser'),
    path('branchinfo/',views.branchinfo,name='branchinfo') ,
    path('idea/',views.idea,name='idea') ,
    path('specialist/',views.specialist,name='specialist') ,
    path('takeloan/',views.takeloan,name='takeloan') ,
    path('confirmloan/',views.confirmloan,name='confirmloan') ,
    
]
