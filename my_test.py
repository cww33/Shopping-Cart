from shopping_cart import to_usd
from shopping_cart import taxtotal
from shopping_cart import total
from shopping_cart import subtotal
from shopping_cart import taxpercentage

subtotal=100
taxtotal=8.75

def test_to_usd():
    result= to_usd(123456.78)
    assert result == " $123,456.78"

def test_taxtotal():
    result=subtotal*taxpercentage
    assert result == 8.75

def test_total():
    result= total
    assert result == 108.75

