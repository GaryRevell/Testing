import pytest
from caesar import caesar

#
# Default test data consisting of pairs of plain & encrypted text
#
testData = [("ABC","FGH"),("GARY","LFWD"),("CAT","HFY"),("DEF","IJK"),("AEROPLANE","FJWTUQFSJ")]


"""
	Declare fixture that returns the caesar object instantiation 
"""
@pytest.fixture
def create_engine():
	return caesar(5)

"""
	Test that the caesar encryption object has been created
"""
def test_engine_created(create_engine):
	assert create_engine is not None

"""
	Test that the text passed is encrypted into the expected cipher text
"""
@pytest.mark.parametrize("text,cipher", testData)
def test_encryption(text,cipher,create_engine):
	assert create_engine.cipherText(text) == cipher

"""
	Text that the cipher text passed is decrypted into the plain text
"""
@pytest.mark.parametrize("text,cipher", testData)
def test_decryption(text,cipher,create_engine):
	assert create_engine.originalText(cipher) == text


