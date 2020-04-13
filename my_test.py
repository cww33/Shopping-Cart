from shopping_cart import to_usd
from shopping_cart import taxtotal
from shopping_cart import total
from shopping_cart import subtotal
from shopping_cart import taxpercentage

#subtotal=100
#taxtotal=8.75

def test_to_usd():
    result= to_usd(73498.82 )
    assert result == " $73,498.82"

def test_taxtotal():
    result= taxtotal
    assert result == subtotal*taxpercentage

def test_total():
    result= subtotal+taxtotal
    assert result == total

