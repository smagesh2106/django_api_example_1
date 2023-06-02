from django.urls import path
from .views import BookListView

urlpatterns = [
    path("ui/books/", BookListView.as_view(), name="home"),
]