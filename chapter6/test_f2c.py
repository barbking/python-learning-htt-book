# Barbara King test_f2c.py

import pytest
import f2c

def test_zero():
    assert f2c.f_to_c(0) == -17.78

def test_freezing():
    assert f2c.f_to_c(32.0) == 0

def test_boiling():
    assert f2c.f_to_c(212) == 100

def test_10():
    assert f2c.f_to_c(10.0) == -12.22

def test_neg10():
    assert f2c.f_to_c(-10.0) == -23.33

def test_20():
    assert f2c.f_to_c(20.0) == -6.67

def test_neg20():
    assert f2c.f_to_c(-20.0) == -28.89

def test_30():
    assert f2c.f_to_c(30.0) == -1.11

def test_neg30():
    assert f2c.f_to_c(-30.0) == -34.44

def test_40():
    assert f2c.f_to_c(40.0) == 4.44

def test_neg40():
    assert f2c.f_to_c(-40.0) == -40.00



