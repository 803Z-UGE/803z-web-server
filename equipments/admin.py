from equipments.models import Equipment, Category, SubCategory, Reservation

from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.sections import TableSection


@admin.register(Equipment)
class EquipmentAdminClass(ModelAdmin):
    list_display = ('serial_number', 'name', 'status', 'category')
    ordering = ('serial_number',)
    list_filter = ("category", "status")
    search_fields = ("name", "serial_number")
    # filter_horizontal = (
    #     "groups",
    #     "user_permissions",
    # )
    pass

class SubcategoryTableSection(TableSection):
    verbose_name = "Sous-catégories"  # Displays custom table title
    height = 300  # Force the table height. Ideal for large amount of records
    related_name = "subcategories_set"  # Related model field name
    fields = ["pk", "name"]  # Fields from related model

    # Custom field
    def custom_field(self, instance):
        return instance.pk

@admin.register(Category)
class CategoryAdminClass(ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_sections = [SubcategoryTableSection]
    pass

@admin.register(SubCategory)
class SubCategoryAdminClass(ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'updated_at')
    ordering = ('category',)
    pass

@admin.register(Reservation)
class ReservationAdminClass(ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'created_at', 'updated_at')
    ordering = ('-start_date',)
    filter_horizontal = ('equipment',)
    pass