import pytest
from calculator import calculator

#
# Default test data consisting
# Each tuple contains - (operand1 , operator, operand2, result)
#

testData = [(2,"+",3,5),(100,"+",1000,1100),(10,"-",3,7),(411,"-",311,100),(11,"*",11,121),
			(4,"*",500,2000),(11,"/",2,5.5),(2500,"/",50,50),
			(5,"!",0,120),(7,"!",0,5040),(10,"_",0,0.1),(0.25,"_",0,4)]
		   
		   
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
 	Test using the operators and operands held in the test data list
"""
@pytest.mark.parametrize("op1,operator,op2,result", testData)
def test_operation(op1,operator,op2,result,create_calculator):
	if operator == "+":
 		assert create_calculator.add(op1,op2) == result
	elif operator == "-":
		assert create_calculator.subtract(op1,op2) == result
	elif operator == "*":
		assert create_calculator.multiply(op1,op2) == result
	elif operator == "/":
		assert create_calculator.divide(op1,op2) == result
	elif operator == "!":
		assert create_calculator.factorial(op1) == result
	elif operator == "_":
		assert create_calculator.reciprocal(op1) == result
	else:
		raise ValueError("Invalid operator: "+operator)	
	
	
