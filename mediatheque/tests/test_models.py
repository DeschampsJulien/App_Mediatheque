import pytest
from member.models import Member


@pytest.mark.django_db  
def test_member_model():
    book = Member.objects.create(
                first_name = "Jules Verne",
                last_name = "20 milles lieues sous les mers",
                email="jdeschamps34@yahoo.fr"
                )
    expected_value = "Jules Verne | 20 milles lieues sous les mers | jdeschamps34@yahoo.fr"
    assert str(book) == expected_value

    