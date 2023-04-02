import uuid
from django.db import models
from django.core.validators import RegexValidator
from django.dispatch import receiver
from django.db.models.signals import post_delete
from internationalflavor.vat_number import VATNumberField

# Create your models here.


class PostalAddress(models.Model):

    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=20)
    apartment_number = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=6, validators=[RegexValidator(
        r'^\d{2}-\d{3}$', message="Enter the zip code in the format xx-xxx.")])

    def __str__(self):
        return f'{self.street} {self.house_number}{"/"+self.apartment_number if self.apartment_number else ""}, {self.postal_code} {self.city}'


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    vat_id_number = VATNumberField(countries=['PL'], null=True)
    creation_date = models.DateField(auto_now_add=True)
    address = models.OneToOneField(
        PostalAddress, on_delete=models.CASCADE, related_name='customer')

    def __str__(self) -> str:
        return f'{self.name}'

# Decorator that guarantees removal of the address when the client is deleted


@receiver(post_delete, sender=Customer)
def my_delete_function(sender, instance, **kwargs):
    PostalAddress.objects.get(id=instance.address.id).delete()
