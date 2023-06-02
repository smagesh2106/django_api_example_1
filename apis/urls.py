from django.urls import path
from .views import BookAPIList, BookAPIDetail

urlpatterns = [
    path("", BookAPIList.as_view(), name="book_list"),
    path("<int:pk>/", BookAPIDetail.as_view(), name="book_detail"),
]
