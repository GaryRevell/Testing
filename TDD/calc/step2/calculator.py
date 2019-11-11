class calculator:

	def add(self,oper1,oper2):
		return oper1 + oper2

	def subtract(self,oper1,oper2):
		return oper1 - oper2

	def multiply(self,oper1,oper2):
		return oper1 * oper2

	def divide(self,oper1,oper2):
		return oper1 / oper2

	def factorial(self,oper1):
		def fact(num):
			return 1 if num == 1 else num * fact(num-1)
        
		return fact(oper1)
    
	def reciprocal(self,oper1):
		return 1/oper1
    
