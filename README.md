# Testing

Test Driven Development code examples using pytest and behave for Behavioural Driven Development.

Uses a simple Caesar cipher class to demonstrate how to use pytest for TDD & BDD

From the TDD/caesar directory you can execute the following commands:

$ pytest -v

============================= test session starts =============================
platform win32 -- Python 3.5.6, pytest-3.8.1, py-1.6.0, pluggy-0.11.0 -- C:\Users\Anaconda3\python.exe
cachedir: .pytest_cache
benchmark: 3.2.2 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: C:\Users\Google Drive\Python\TDD\caesar, inifile:
plugins: remotedata-0.3.0, openfiles-0.4.0, doctestplus-0.4.0, benchmark-3.2.2, bdd-3.2.1, arraydiff-0.2
collected 11 items

steps/test_caesar.py::test_engine_created PASSED                         [  9%]
steps/test_caesar.py::test_encryption[ABC-FGH] PASSED                    [ 18%]
steps/test_caesar.py::test_encryption[GARY-LFWD] PASSED                  [ 27%]
steps/test_caesar.py::test_encryption[CAT-HFY] PASSED                    [ 36%]
steps/test_caesar.py::test_encryption[DEF-IJK] PASSED                    [ 45%]
steps/test_caesar.py::test_encryption[AEROPLANE-FJWTUQFSJ] PASSED        [ 54%]
steps/test_caesar.py::test_decryption[ABC-FGH] PASSED                    [ 63%]
steps/test_caesar.py::test_decryption[GARY-LFWD] PASSED                  [ 72%]
steps/test_caesar.py::test_decryption[CAT-HFY] PASSED                    [ 81%]
steps/test_caesar.py::test_decryption[DEF-IJK] PASSED                    [ 90%]
steps/test_caesar.py::test_decryption[AEROPLANE-FJWTUQFSJ] PASSED        [100%]

========================== 11 passed in 0.10 seconds ==========================

$ behave -v

Using defaults:
scenario_outline_annotation_schema {name} -- @{row.id} {examples.name}
   default_tags
 default_format pretty
    log_capture True
        summary True
  show_snippets True
          stage None
        dry_run False
  logging_level 20
  steps_catalog False
          color False
   show_timings True
 stdout_capture True
    show_source True
       userdata {}
 stderr_capture True
          junit False
 logging_format %(levelname)s:%(name)s:%(message)s
   show_skipped True
Using default path "./features"
Trying base directory: C:\Users\Google Drive\Python\TDD\caesar\features
Trying base directory: C:\Users\Google Drive\Python\TDD\caesar
Feature: Caesar cipher test # caesar_cipher.feature:1

  Scenario: Encrypt shift by 3                  # caesar_cipher.feature:3
    Given I have a key shift of 3               # steps/steps_caesar.py:17
    When I encrypt the text BRANCH              # steps/steps_caesar.py:23
    Then it should create the ciphertext EUDQFK # steps/steps_caesar.py:28

  Scenario: Encrypt shift by 5                          # caesar_cipher.feature:8
    Given I have a key shift of 5                       # steps/steps_caesar.py:17
    When I encrypt the text WEASELSARENICE              # steps/steps_caesar.py:23
    Then it should create the ciphertext BJFXJQXFWJSNHJ # steps/steps_caesar.py:28

  Scenario: Decrypt shift by 3            # caesar_cipher.feature:13
    Given I have a key shift of 3         # steps/steps_caesar.py:17
    When I decrypt the ciphertext EUDQFK  # steps/steps_caesar.py:33
    Then it should create the text BRANCH # steps/steps_caesar.py:38

  Scenario: Decrypt shift by 5                    # caesar_cipher.feature:18
    Given I have a key shift of 5                 # steps/steps_caesar.py:17
    When I decrypt the ciphertext BJFXJQXFWJSNHJ  # steps/steps_caesar.py:33
    Then it should create the text WEASELSARENICE # steps/steps_caesar.py:38

  Scenario: Encrypt shift by -1                                      # caesar_cipher.feature:23
    Given I have a key shift of -1                                   # steps/steps_caesar.py:17
    When I encrypt the text STRINGSARELISTSOFCHARACTERS              # steps/steps_caesar.py:23
    Then it should create the ciphertext RSQHMFRZQDKHRSRNEBGZQZBSDQR # steps/steps_caesar.py:28

  Scenario: Decrypt shift by -1                                # caesar_cipher.feature:28
    Given I have a key shift of -1                             # steps/steps_caesar.py:17
    When I decrypt the ciphertext RSQHMFRZQDKHRSRNEBGZQZBSDQR  # steps/steps_caesar.py:33
    Then it should create the text STRINGSARELISTSOFCHARACTERS # steps/steps_caesar.py:38

  Scenario: Encrypt shift by -16                                           # caesar_cipher.feature:33
    Given I have a key shift of -16                                        # steps/steps_caesar.py:17
    When I encrypt the text IwillweaRmyBesTbooTStothECeremony              # steps/steps_caesar.py:23
    Then it should create the ciphertext SgsvvgokBwiLocDlyyDCdydrOMobowyxi # steps/steps_caesar.py:28

  Scenario: Decrypt shift by -16                                     # caesar_cipher.feature:38
    Given I have a key shift of -16                                  # steps/steps_caesar.py:17
    When I decrypt the ciphertext SgsvvgokBwiLocDlyyDCdydrOMobowyxi  # steps/steps_caesar.py:33
    Then it should create the text IwillweaRmyBesTbooTStothECeremony # steps/steps_caesar.py:38

  Scenario: Encrypt shift by 0                                                 # caesar_cipher.feature:44
    Given I have a key shift of 0                                              # steps/steps_caesar.py:17
    When I encrypt the text THEROOTCAUSEOFTHEPROBLEMISLACKOFLOGIC              # steps/steps_caesar.py:23
    Then it should create the ciphertext THEROOTCAUSEOFTHEPROBLEMISLACKOFLOGIC # steps/steps_caesar.py:28

  Scenario: Decrypt shift by 0                                           # caesar_cipher.feature:49
    Given I have a key shift of 0                                        # steps/steps_caesar.py:17
    When I decrypt the ciphertext THEROOTCAUSEOFTHEPROBLEMISLACKOFLOGIC  # steps/steps_caesar.py:33
    Then it should create the text THEROOTCAUSEOFTHEPROBLEMISLACKOFLOGIC # steps/steps_caesar.py:38

  Scenario: Encrypt shift by 13                                                 # caesar_cipher.feature:54
    Given I have a key shift of 13                                              # steps/steps_caesar.py:17
    When I encrypt the text IWOuldLiketoSeeHerinaDRESsthatSuitsher              # steps/steps_caesar.py:23
    Then it should create the ciphertext VJBhyqYvxrgbFrrUrevanQERFfgungFhvgfure # steps/steps_caesar.py:28

  Scenario: Decrypt shift by 13                                           # caesar_cipher.feature:59
    Given I have a key shift of 13                                        # steps/steps_caesar.py:17
    When I decrypt the ciphertext VJBhyqYvxrgbFrrUrevanQERFfgungFhvgfure  # steps/steps_caesar.py:33
    Then it should create the text IWOuldLiketoSeeHerinaDRESsthatSuitsher # steps/steps_caesar.py:38

  Scenario: Encrypt shift by A - exception                                      # caesar_cipher.feature:69
    Given I have a key shift of A                                               # steps/steps_caesar.py:17
      Traceback (most recent call last):
        File "c:\users\anaconda3\lib\site-packages\behave\model.py", line 1329, in run
          match.run(runner.context)
        File "c:\users\anaconda3\lib\site-packages\behave\matchers.py", line 98, in run
          self.func(context, *args, **kwargs)
        File "steps\steps_caesar.py", line 19, in step_given_character_shift
          context.shift = int(shift)
      ValueError: invalid literal for int() with base 10: 'A'

    When I encrypt the text IWOuldLiketoSeeHerinaDRESsthatSuitsher              # None
    Then it should create the ciphertext IWOuldLiketoSeeHerinaDRESsthatSuitsher # None


Failing scenarios:
  caesar_cipher.feature:69  Encrypt shift by A - exception

0 features passed, 1 failed, 0 skipped
12 scenarios passed, 1 failed, 0 skipped
36 steps passed, 1 failed, 2 skipped, 0 undefined
Took 0m0.031s
