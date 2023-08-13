from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('associations/', AssociationView.as_view()),
    path('notifications/', NotificationView.as_view()),
    path('memories/', MemoriesView.as_view()),
    # path('message/', message.as_view()),
]
