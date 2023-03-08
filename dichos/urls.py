from django.urls import path
from .views import (
    DichoDetailView,
    DichoListView,
)

urlpatterns = [
    path('', DichoListView.as_view(), name='dicho_list'),
    path('<int:pk>/', DichoDetailView.as_view(), name="dicho_detail"),
]
