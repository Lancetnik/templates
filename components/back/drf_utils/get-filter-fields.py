from rest_framework.views import APIView
from rest_framework.response import Response

from .models import SomeModel


class GetFilterParams(APIView):
    def get(self, request, fieldname):
        if fieldname == 'fields': data = {i.name for i in SomeModel._meta.fields}
        else: data = SomeModel.objects.all().values_list(fieldname, flat=True).distinct()
        return Response(data)

# urls: 'filter-params/<str:fieldname>/'