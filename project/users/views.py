from rest_framework import viewsets
from .models import Link
from .serializers import LinkSerializer
from rest_framework.permissions import IsAuthenticated

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
