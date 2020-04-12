from shopping_cart import to_usd

def test_to_usd():
    result= to_usd(123456.78)
    assert result == " $123,456.78"
