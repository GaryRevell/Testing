import pytest
from calculator import calculator

"""
 	Declare fixture that returns the calculator object instantiation 
"""
@pytest.fixture
def create_calculator():
 	return calculator()
 
"""
	Test that the calculator object has been created
"""
def test_calculator_created(create_calculator):
    assert create_calculator is not None
    assert type(create_calculator) == type(calculator())

"""
    Test the addition function
""" 
def test_add(create_calculator):
    assert create_calculator.add(2,3) == 5
    assert create_calculator.add(100,1000) == 1100

"""
    Test the subtract function
""" 
def test_subtract(create_calculator):
    assert create_calculator.subtract(10,3) == 7
    assert create_calculator.subtract(411,311) == 100
    
"""
    Test the multiply function
""" 
def test_multiply(create_calculator):
    assert create_calculator.multiply(11,11) == 121
    assert create_calculator.multiply(4,500) == 2000
    
"""
    Test the divide function
""" 
def test_divide(create_calculator):
    assert create_calculator.divide(11,2) == 5.5
    assert create_calculator.divide(2500,50) == 50

"""
    Test the factorial function
""" 
def test_factorial(create_calculator):
    assert create_calculator.factorial(5) == 120
    assert create_calculator.factorial(7) == 5040

"""
    Test the reciprocal function
""" 
def test_reciprocal(create_calculator):
    assert create_calculator.reciprocal(10) == 0.1
    assert create_calculator.reciprocal(0.25) == 4


