# Barbara King test_fib.py

import pytest
import fib

def test_0():
    assert fib.fibonacci(0) == 0

def test_1():
    assert fib.fibonacci(1) == 1

def test_2():
    assert fib.fibonacci(2) == 1

def test_3():
    assert fib.fibonacci(3) == 2

def test_8():
    assert fib.fibonacci(8) == 21

def test_10():
    assert fib.fibonacci(10) == 55

def test_12():
    assert fib.fibonacci(12) == 144

def test_14():
    assert fib.fibonacci(14) == 377

def test_15():
    assert fib.fibonacci(15) == 610

def test_20():
    assert fib.fibonacci(20) == 6765


