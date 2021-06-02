from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import SomeItem
from .serializers import SomeItemSerializer
from .filters import SomeItemFilter


class SomeItemListView(generics.ListAPIView):
    queryset = SomeItem.objects.all()
    serializer_class = SomeItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SomeItemFilter


class GetSomeItemsFileView(SomeItemListView):
    def list(self, request, file_format):
        queryset = self.filter_queryset(self.get_queryset())
        return send_file(file_format, queryset)


import os
import json
import uuid

from django.http import HttpResponse
from wsgiref.util import FileWrapper

from django_pandas.io import read_frame

from .serializers import SomeItemSerializer


def _create_file_response(filename: str) -> HttpResponse:
    file_format = filename.split('.')[-1]
    with open(filename, 'rb') as file:
        content = f'application/{file_format}'
        response = HttpResponse(
                FileWrapper(file),
                content_type=content
            )
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response

def _create_file(filename: str, queryset) -> None:
    if filename.endswith('xlsx'):
        read_frame(queryset).to_excel(filename)
    elif filename.endswith('csv'):
        read_frame(queryset).to_csv(filename)
    elif filename.endswith('json'):
        with open(filename, 'w') as outfile:
            json.dump(SomeItemSerializer(queryset, many=True).data, outfile, indent=4, ensure_ascii=False)

def send_file(file_format: str, queryset) -> HttpResponse:
    assert file_format in ['xlsx', 'json', 'csv']
    filename = f'{uuid.uuid4()}.{file_format}'
    _create_file(filename, queryset)
    response = _create_file_response(filename)
    os.remove(filename)
    return response


# req: openpyxl django-pandas
# urls: 'file/<str:file_format>/'