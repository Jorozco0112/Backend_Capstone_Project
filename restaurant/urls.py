from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/user', views.UserView.as_view(), name='user'),
    path('api/menu', views.MenuItemsView.as_view()),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
