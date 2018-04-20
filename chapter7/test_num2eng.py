# Barbara King
# test_num2eng.py

import pytest
import num2eng4

def test_negative():
    assert num2eng4.num_to_english(-5) == "Invalid"

def test_zero():
    assert num2eng4.num_to_english(0) == "zero"

def test_one():
    assert num2eng4.num_to_english(1) == "one"

def test_nine():
    assert num2eng4.num_to_english(9) == "nine"

def test_ten():
    assert num2eng4.num_to_english(10) == "ten"

def test_11():
    assert num2eng4.num_to_english(11) == "eleven"

def test_19():
    assert num2eng4.num_to_english(19) == "nineteen"

def test_20():
    assert num2eng4.num_to_english(20) == "twenty"

def test_21():
    assert num2eng4.num_to_english(21) == "twenty-one"

def test_33():
    assert num2eng4.num_to_english(33) == "thirty-three"

def test_55():
    assert num2eng4.num_to_english(55) == "fifty-five"

def test_59():
    assert num2eng4.num_to_english(59) == "fifty-nine"

def test_70():
    assert num2eng4.num_to_english(70) == "seventy"

def test_77():
    assert num2eng4.num_to_english(77) == "seventy-seven"

def test_80():
    assert num2eng4.num_to_english(80) == "eighty"

def test_88():
    assert num2eng4.num_to_english(88) == "eighty-eight"

def test_90():
    assert num2eng4.num_to_english(90) == "ninety"

def test_99():
    assert num2eng4.num_to_english(99) == "ninety-nine"

def test_100():
    assert num2eng4.num_to_english(100) == "one-hundred"

def test_101():
    assert num2eng4.num_to_english(101) == "Invalid"
