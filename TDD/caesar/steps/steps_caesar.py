# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:35:02 2019

@author: GaryR
"""

# file:features/steps/steps.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave   import given, when, then
from hamcrest import assert_that, equal_to
from caesar	  import caesar


@given('I have a key shift of {shift}')
def step_given_character_shift(context, shift):
	context.shift = int(shift)
	context.caesar = caesar(context.shift)


@when('I encrypt the text {text}')
def step_when_encrypting(context,text):
	context.cipher = context.caesar.cipherText(text)

	
@then('it should create the ciphertext {cipherText}')
def step_then_(context, cipherText):
    assert_that(context.cipher, equal_to(cipherText))
 
 
@when('I decrypt the ciphertext {cipher}')
def step_when_encrypting(context,cipher):
	context.plain = context.caesar.originalText(cipher)

	
@then('it should create the text {text}')
def step_then_(context, text):
    assert_that(context.plain, equal_to(text))
    
