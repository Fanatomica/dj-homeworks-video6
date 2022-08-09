from rest_framework.viewsets import ModelViewSet

from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle

from advertisements.permissions import IsOwnerOrReadOnly, IsOwnerDraft

from advertisements.models import Advertisement

from advertisements.serializers import AdvertisementSerializer

from advertisements.filters import AdvertisementFilter

from django_filters import rest_framework as filters


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filterset_classes = [AdvertisementFilter,]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['creator']


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly()]
        else:
            return [IsOwnerDraft()]




