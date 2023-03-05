import pytest
from django.contrib.auth.models import User


def test_home_view(client):
    response = client.get(path="/home")
    assert response.status_code == 302


@pytest.mark.django_db
def test_home_view_is_auth(client):

    user = User.objects.create_user('name', 'name@example.com', 'password')
    client.login(username=user.username, password='password')
    response = client.get(path="/home")
    assert response.status_code == 200
    assert 'home/welcome.html' in response.template_name
