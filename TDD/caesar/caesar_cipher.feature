Feature: Caesar cipher test

  Scenario: Encrypt shift by 3
    Given I have a key shift of 3
    When  I encrypt the text BRANCH
    Then  it should create the ciphertext EUDQFK
    
  Scenario: Encrypt shift by 5
    Given I have a key shift of 5
    When  I encrypt the text WEASELSARENICE
    Then  it should create the ciphertext BJFXJQXFWJSNHJ
    
  Scenario: Decrypt shift by 3
    Given I have a key shift of 3
    When  I decrypt the ciphertext EUDQFK
    Then  it should create the text BRANCH
    
  Scenario: Decrypt shift by 5
    Given I have a key shift of 5
    When  I decrypt the ciphertext BJFXJQXFWJSNHJ
    Then  it should create the text WEASELSARENICE
    
  Scenario: Encrypt shift by -1
    Given I have a key shift of -1
    When  I encrypt the text STRINGSARELISTSOFCHARACTERS
    Then  it should create the ciphertext RSQHMFRZQDKHRSRNEBGZQZBSDQR
    
  Scenario: Decrypt shift by -1
    Given I have a key shift of -1
    When  I decrypt the ciphertext RSQHMFRZQDKHRSRNEBGZQZBSDQR
    Then  it should create the text STRINGSARELISTSOFCHARACTERS

  Scenario: Encrypt shift by -16
    Given I have a key shift of -16
    When  I encrypt the text IwillweaRmyBesTbooTStothECeremony
    Then  it should create the ciphertext SgsvvgokBwiLocDlyyDCdydrOMobowyxi
    
  Scenario: Decrypt shift by -16
    Given I have a key shift of -16
    When  I decrypt the ciphertext SgsvvgokBwiLocDlyyDCdydrOMobowyxi
    Then  it should create the text IwillweaRmyBesTbooTStothECeremony
	
	
  Scenario: Encrypt shift by 0
    Given I have a key shift of 0
    When  I encrypt the text THEROOTCAUSEOFTHEPROBLEMISLACKOFLOGIC
    Then  it should create the ciphertext THEROOTCAUSEOFTHEPROBLEMISLACKOFLOGIC
    
  Scenario: Decrypt shift by 0
    Given I have a key shift of 0
    When  I decrypt the ciphertext THEROOTCAUSEOFTHEPROBLEMISLACKOFLOGIC
    Then  it should create the text THEROOTCAUSEOFTHEPROBLEMISLACKOFLOGIC
	
  Scenario: Encrypt shift by 13
    Given I have a key shift of 13
    When  I encrypt the text IWOuldLiketoSeeHerinaDRESsthatSuitsher
    Then  it should create the ciphertext VJBhyqYvxrgbFrrUrevanQERFfgungFhvgfure

  Scenario: Decrypt shift by 13
    Given I have a key shift of 13
    When  I decrypt the ciphertext VJBhyqYvxrgbFrrUrevanQERFfgungFhvgfure
    Then  it should create the text IWOuldLiketoSeeHerinaDRESsthatSuitsher


#
# Failures
#

  Scenario: Encrypt shift by A - exception
    Given I have a key shift of A
    When  I encrypt the text IWOuldLiketoSeeHerinaDRESsthatSuitsher
    Then  it should create the ciphertext IWOuldLiketoSeeHerinaDRESsthatSuitsher
	
