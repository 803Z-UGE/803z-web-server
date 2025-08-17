from equipments.models import Equipment, SubCategory, Category, Reservation
from rest_framework import serializers

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        exclude = ('note',)
        read_only_fields = ('created_at', 'updated_at')

class EquipmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class CategoryGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("La date de début doit être antérieure à la date de fin.")
        return data