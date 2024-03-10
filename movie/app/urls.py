from django.contrib import admin
from django.urls import path
from app import views
app_name = "app"

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.MovieList.as_view(),name="home"),
    # path('addmore',views.addmore,name="addmore"),
    path('addmore/',views.Movieadd.as_view(),name="addmore"),
    # path('details/<int:p>',views.details,name="details"),
    path('m/<int:pk>',views.MovieDetail.as_view(),name="details"),
    # path('update/<int:p>', views.update, name="update"),
    path('update/<int:pk>',views.Movieupdate.as_view(),name="update"),
    # path('delete/<int:p>', views.delete, name="delete"),
    path('delete/<int:pk>',views.Moviedelete.as_view(),name="delete"),
]
