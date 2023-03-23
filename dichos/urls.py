from django.urls import path
# from .views import  DichoDetailView, DichoListView,
from .views import DichoDetail, DichoList

urlpatterns= [
    path('', DichoList.as_view(), name='dicho_list'),
    path('<int:pk>/', DichoDetail.as_view(), name='dicho_detail')

]

# urlpatterns = [
#     path('', DichoListView.as_view(), name='dicho_list'),
#     path('<int:pk>/', DichoDetailView.as_view(), name="dicho_detail"),
# ]
