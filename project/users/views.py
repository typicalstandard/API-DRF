from rest_framework import viewsets
from .models import Link
from .serializers import LinkSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Link
from .serializers import LinkSerializer
from rest_framework.permissions import IsAuthenticated
import requests
from bs4 import BeautifulSoup

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        url = serializer.validated_data['url']
        title, description, image, link_type = self.extract_metadata(url)
        serializer.save(user=self.request.user, title=title, description=description, image=image, link_type=link_type)

    def extract_metadata(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('meta', property='og:title') or soup.find('title')
        description = soup.find('meta', property='og:description') or soup.find('meta', attrs={'name': 'description'})
        image = soup.find('meta', property='og:image')
        link_type = soup.find('meta', property='og:type')

        title_content = title['content'] if title and title.has_attr('content') else title.string if title else ''
        description_content = description['content'] if description and description.has_attr('content') else ''
        image_content = image['content'] if image else ''
        link_type_content = link_type['content'] if link_type else 'website'

        return title_content, description_content, image_content, link_type_content



