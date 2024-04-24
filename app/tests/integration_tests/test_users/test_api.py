import pytest
from httpx import AsyncClient


# async_client
# post - json
# get - params
@pytest.mark.parametrize("email, password, status_code", [
    ("Ivan@van.com", "Ivan", 200),
    ("Ivan@van.com", "Ivanovich", 409),
    ("adcde", "Ivanovich", 422),
])
async def test_register_user(async_client: AsyncClient, email, password, status_code):
    response = await async_client.post("auth/register", json={
        "email": email,
        "password": password
    })
    assert response.status_code == status_code


@pytest.mark.parametrize("email, password, status_code", [
    ("ivan@test.com", "pass", 200),
    ("test@test.com", "_---_", 401),
    ("test@test.com", "pass", 200),
    ("t@test.com", "pass", 401),
])
async def test_login_user(async_client: AsyncClient, email, password, status_code):
    response = await async_client.post("auth/login", json={
        "email": email,
        "password": password
    })
    assert response.status_code == status_code
