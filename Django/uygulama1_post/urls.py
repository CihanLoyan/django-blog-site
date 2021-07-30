from django.urls import path
from uygulama1_post.views import *
from home.views import home_view

urlpatterns = [
    path('', postliste_view),
    path('detail/<str:slug>', postdetail_view),
    path('create', postcreate_view),
    path('delete/<int:id>', postdelete_view),
    path('update/<int:id>', postupdate_view),
    path('formDoldur', formdoldur_view),
    path('updateYolla/<int:id>', postupdate_view),
 ]
