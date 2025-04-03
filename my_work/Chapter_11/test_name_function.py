from name_function import get_formatted_name


def test_first_last_name():
    """Поддерживаются имена типа Janis Joplin?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
