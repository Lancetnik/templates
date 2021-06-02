from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response

from .models import SomeItem
from .serializers import PlotSerializer
from .filters import SomeItemFilter


class DiagramPlotView(generics.ListAPIView):
    queryset = SomeItem.objects.all()
    serializer_class = PlotSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SomeItemFilter

    def list(self, request, column, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = get_column_sum_plot(queryset, column)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BarPlotView(generics.ListAPIView):
    queryset = SomeItem.objects.all()
    serializer_class = PlotSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SomeItemFilter

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = get_months_plot(queryset, 'id')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


from django.db.models.functions import TruncMonth, Cast
from django.db.models import Count, F, DateField

def get_months_plot(queryset, field) -> list:
    # DateField or DateTimeField
    return queryset.annotate(date=Cast('datetime', output_field=DateField()))\
        .values('date').annotate(field=TruncMonth('date'))\
        .values('field').annotate(c=Count(field)).values('field', 'c')\
        .order_by('field')

def get_column_sum_plot(queryset, field) -> list:
    return queryset.values(field).annotate(field=F(field), c=Count(field)).order_by('-c').values('field', 'c')


from rest_framework import serializers

class PlotSerializer(serializers.Serializer):
    field = serializers.CharField(required=False)
    c = serializers.IntegerField()


# urls: 'diagram-plot/<str:column>/'