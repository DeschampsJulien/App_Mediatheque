from member.models import Member


def test_book():
    book = Member.objects.create(first_name="Julien", last_name="Deschamps", email="jdeschamps34@yahoo.fr")
    expected_value = "Julien, Deschamps, jdeschamps34@yahoo.fr"
    
    assert (book) == expected_value

    