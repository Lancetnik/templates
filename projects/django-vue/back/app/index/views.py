from rest_framework import views
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


class IndexView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(template_name="index.html")
