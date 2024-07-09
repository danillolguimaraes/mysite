import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert b'HELLO WORLD EBAC, EXERCISE FOR DJANGO VIEWS 09/07/2024 12h41 BY : DANILLONEO' in response.content
