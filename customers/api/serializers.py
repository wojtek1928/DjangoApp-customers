from rest_framework import serializers

from customers.models import Customer, PostalAddress


class PostalAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalAddress
        exclude = ['id']


class CustomerSerializer(serializers.ModelSerializer):
    address = PostalAddressSerializer()

    class Meta:
        model = Customer
        fields = ['name', 'vat_id_number',
                  'creation_date', 'address']

    # Adding field with link to edit/delete customer data in API
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        URI = self.context['request'].build_absolute_uri()
        representation['Link to details of customer'] = f"{URI}{instance.id}"
        return representation

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = PostalAddress.objects.create(**address_data)
        customer = Customer.objects.create(
            name=validated_data['name'],
            vat_id_number=validated_data['vat_id_number'],
            address=address)
        return customer

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = instance.address

        instance.name = validated_data.get('name', instance.name)
        instance.vat_id_number = validated_data.get(
            'vat_id_number', instance.vat_id_number)
        instance.save()

        address.street = address_data.get('street', address.street)
        address.house_number = address_data.get(
            'house_number', address.house_number)

        address.apartment_number = address_data.get(
            'apartment_number', address.apartment_number)

        address.city = address_data.get('city', address.city)
        address.postal_code = address_data.get(
            'postal_code', address.postal_code)
        address.save()

        return instance
