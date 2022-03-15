import pytest
from src.index import *

@pytest.hookimpl
class Test_stat():

    def test_stat_1(self):
        result = stat_1()
        assert result % 2 == 0
    
    def test_stat_2(self):
        result = stat_2()
        assert result % 2 == 0
    
    def test_stat_3(self):
        result = stat_3()
        assert result % 2 == 0
    
    def test_stat_4(self):
        result = stat_4()
        assert result % 2 == 0
    
    def test_stat_5(self):
        result = stat_5()
        assert result % 2 == 0
    
    def test_stat_6(self):
        result = stat_6()
        assert result % 2 == 0
    
    def test_stat_7(self):
        result = stat_7()
        assert result % 2 == 0
    
    def test_stat_8(self):
        result = stat_8()
        assert result % 2 == 0
    
    def test_stat_9(self):
        result = stat_9()
        assert result % 2 == 0
    
    def test_stat_10(self):
        result = stat_10()
        assert result % 2 == 0