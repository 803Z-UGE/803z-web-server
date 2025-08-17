from equipments.models import Equipment, Category, SubCategory, Reservation

from django.contrib import admin
from unfold.admin import ModelAdmin


@admin.register(Equipment)
class EquipmentAdminClass(ModelAdmin):
    pass

@admin.register(Category)
class CategoryGroupAdminClass(ModelAdmin):
    pass

@admin.register(SubCategory)
class EquipmentCategoryAdminClass(ModelAdmin):
    pass

@admin.register(Reservation)
class ReservationAdminClass(ModelAdmin):
    pass
