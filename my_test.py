from shopping_cart import to_usd
from shopping_cart import taxtotal
from shopping_cart import total
from shopping_cart import subtotal
from shopping_cart import taxpercentage


def test_to_usd():
    result= to_usd(73498.82 )
    assert result == " $73,498.82"
    assert to_usd(9.9) == " $9.90"
   
def test_taxtotal():
    result= taxtotal
    assert result == subtotal*taxpercentage

def test_total():
    result= subtotal+taxtotal
    assert result == total



