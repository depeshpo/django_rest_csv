from rest_framework.serializers import ModelSerializer


from contact.models import Contact, Contact_CSV


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactCSVSerializer(ModelSerializer):
    class Meta:
        model = Contact_CSV
        fields = '__all__'
