from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('category', 'name')
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Equipment(models.Model):
    serial_number = models.CharField(max_length=4, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True, verbose_name="Notes internes (visibles par le staff uniquement)")
    status = models.CharField(max_length=20, choices=[
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('hidden', 'Hidden'),
    ], default='available')
    category = models.ForeignKey(SubCategory, related_name='equipments', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.serial_number} - {self.name}"
    
class EquipmentPicture(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='pictures', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='equipment_pictures/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Picture of {self.equipment.name}"

class Reservation(models.Model):
    equipment = models.ManyToManyField(Equipment, related_name='reservations')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reservations', on_delete=models.RESTRICT)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.equipment.name} réservé par {self.user.first_name} {self.user.last_name} du {self.start_date} au {self.end_date}"