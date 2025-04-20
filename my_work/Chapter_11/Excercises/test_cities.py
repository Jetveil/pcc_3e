from city_functions import get_city_country


def test_city_country():
    """Проходит ли формат типа: Moscow Russia?"""
    location = get_city_country('moscow', 'russia')
    assert location == "Moscow Russia"
