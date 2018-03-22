import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def get_input_data(request):
    if request.method == 'POST':
        _url = request.data['inputURL']
        try:
            code = requests.get(_url)
            text = code.text
            soup = BeautifulSoup(text)
            all_images = []
            a = soup.findAll('img')
            images = [x['src'] for x in soup.findAll('img') if x.get('src')]
            for img in images:
                if img[0:4] == 'http':
                    all_images.append(img)
                else:
                    all_images.append(urljoin(_url, img))
            return Response({"all_images":all_images})
        except Exception as e:
            return Response({"error_desc":"Something went wrong.",status:404})