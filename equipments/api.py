from equipments.serializers import EquipmentCategorySerializer, EquipmentSerializer, CategoryGroupSerializer, ReservationSerializer
from equipments.models import Equipment, SubCategory, Category, Reservation
from rest_framework import viewsets
from project.permissions import IsAdminUserOrReadOnly 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from drf_spectacular.utils import extend_schema

@extend_schema(
    operation_id='equipment_list',
    description='List all equipments (public endpoint) or edit them if you are an admin.',
)
class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    authentication_classes = [TokenAuthentication]

@extend_schema(
    operation_id='equipment_category_list',
    description='List all equipment categories (public endpoint) or edit them if you are an admin.',
)
class EquipmentCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = EquipmentCategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    authentication_classes = [TokenAuthentication]

@extend_schema(
    operation_id='category_group_list',
    description='List all category groups (public endpoint) or edit them if you are an admin.',
)
class CategoryGroupViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryGroupSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    authentication_classes = [TokenAuthentication]

@extend_schema(
    operation_id='reservation_list',
    description='List current user\'s reservations and create new ones (authenticated users only)',
)
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)