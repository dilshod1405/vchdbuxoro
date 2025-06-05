from django.urls import path
from .views import (
    InformationListView,
    InformationDetailView,
    ServiceListView,
    ServiceDetailView,
    MessageCreateView
)

urlpatterns = [
    path('information/', InformationListView.as_view(), name='information-list'),
    path('information/<int:id>/', InformationDetailView.as_view(), name='information-detail'),
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<int:id>/', ServiceDetailView.as_view(), name='service-detail'),
    path('messages/', MessageCreateView.as_view(), name='message-create'),
]