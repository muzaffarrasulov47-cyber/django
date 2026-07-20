from .views import BookListApiView,CarListApiView,PersonListApiView
from django.urls import path

urlpatterns = [
    path('book/', BookListApiView.as_view()),
    path('car/', CarListApiView.as_view()),
    path('person/', PersonListApiView.as_view()),
]