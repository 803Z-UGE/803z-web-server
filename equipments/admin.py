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
    height = 300  # Force the table height. Ideal for large amount of records
    related_name = "subcategories"  # Related model field name
    fields = ["name", "category", "id"]  # Fields from related model

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

class EquipmentTableSection(TableSection):
    height = 300  # Force the table height. Ideal for large amount of records
    related_name = "equipment"  # Related model field name
    fields = ["serial_number", "name", "available"]  # Fields from related model

    # Custom field
    def available(self, instance):
        return instance.status == 'available'
        # Return True if there are no validated reservations for this equipment during the reservation's dates
        # reservation = instance
        # equipment = reservation.equipment
        # start_date = reservation.start_date
        # end_date = reservation.end_date

        # # Check for overlapping validated reservations
        # overlapping = equipment.reservation_set.filter(
        #     validated=True,
        #     start_date__lt=end_date,
        #     end_date__gt=start_date
        # ).exclude(pk=reservation.pk).exists()

        # return not overlapping

@admin.register(Reservation)
class ReservationAdminClass(ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'created_at', 'updated_at')
    ordering = ('-start_date',)
    filter_horizontal = ('equipment',)
    list_sections = [EquipmentTableSection]
    pass