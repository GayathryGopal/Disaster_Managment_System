from django.urls import path
from flood import views
urlpatterns=[
    path('',views.home),
    path('hm',views.home),
    path('cp',views.camp),
    path('viewmore',views.mores),
    path('ad',views.addperson),
    path('req',views.requirement),
    path('req1',views.requ1),
    path('reqmore',views.reqmore),



]