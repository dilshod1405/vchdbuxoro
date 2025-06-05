from rest_framework import generics
from .serializers import (
    InformationSerializer,
    ServiceSerializer,
    MessageSerializer
)
from .models import (
    Information,
    Service,
    Message
)

# Get all information
class InformationListView(generics.ListAPIView):
    queryset = Information.objects.all().order_by('-created_at')
    serializer_class = InformationSerializer
    
# Get information by ID
class InformationDetailView(generics.RetrieveAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    lookup_field = 'id'
    
# Get all services
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
# Get service by ID
class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id'
    
# Create a new message
class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def perform_create(self, serializer):
        serializer.save()  # Save the message instance
