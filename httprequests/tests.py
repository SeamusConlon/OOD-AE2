from django.test import TestCase
from httprequests.models import HexBase, HexRegular, HexLimiter, HexFactory

class HexTesting(TestCase):
    def test_smoke(self):
        assert 3 + 3 == 6
        assert 3 * 3 == 9
        assert 3 ** 3 == 27
        assert type(3.141) == float
        
    def test_base_class(self):
        test_object = HexBase(200,150,100)
        assert test_object.b == 100
        assert isinstance(test_object,HexBase)==True
        
    def test_regular_converter(self):
        assert HexRegular(255,255,255).result() == 'FFFFFF'
        assert HexRegular(15,15,15).result() == '0F0F0F'
        assert HexRegular(171,193,35).result() == 'ABC123'
        assert HexRegular(50,28,186).result() == '321CBA'
        
    def test_refined_converter(self):
        assert HexLimiter(10,160,259).result() == '0AA0FF'
        assert HexLimiter(-255,15947,157).result() == '00FF9D'
        assert HexLimiter(187,-111,188).result() == 'BB00BC'
        assert HexLimiter(237,11,-15).result() == 'ED0B00'
        
    def test_factory(self):
        assert HexFactory(171,195,33).factory_result() == 'ABC321'
        assert HexFactory(222,239,86).factory_result() == 'DEEF56'
        assert HexFactory(224,244,858).factory_result() == 'E0F4FF'
