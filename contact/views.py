import csv
import os

from django.conf import settings

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Contact
from .serializers import ContactCSVSerializer, ContactSerializer


def upload_contact_csv(file_path):
    base_path = settings.BASE_DIR
    full_file = os.path.join(str(base_path), str(file_path))
    with open(full_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for column in csv_reader:
            Contact.objects.update_or_create(
                first_name=column['first_name'],
                last_name=column['last_name'],
                email=column['email']
            )


class ContactView(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactUploadView(APIView):
    serializer_class = ContactCSVSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = ContactCSVSerializer(data=request.data)

        if serializer.is_valid():
            csv_file_path = serializer.validated_data['csv']
            upload_contact_csv(csv_file_path)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
