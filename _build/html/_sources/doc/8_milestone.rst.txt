

============
Strings in C
============


****************
Class 6: Strings
****************


---------------------------------------------------
asg_a0001 : String - Change the case of a sentence.
---------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``alter_case("Hello World")`` which converts the case of the characters. The first character should be capital, second one small, third one Captial and so on. Special characters are counted as a character but no operation is performed on them.


'''''''
Samples
'''''''
========  =====================================  ==========  ==========
  Number  Explanation                            Input       Output
========  =====================================  ==========  ==========
       1  Check for a general case.              HelloWorld  HeLlOwOrLd
       2  Check for all "lowercase" characters.  helloworld  HeLlOwOrLd
       3  Check for all "UPPERCASE" characters.  HELLOWORLD  HeLlOwOrLd
========  =====================================  ==========  ==========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``string alter_case_1(input)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  =============  ======  ========================  =========
  Number  Type           Name    Explanation               Remarks
========  =============  ======  ========================  =========
       1  String Object  input   String to be worked upon
========  =============  ======  ========================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =============  ======  ==============================  =========
  Number  Type           Name    Explanation                     Remarks
========  =============  ======  ==============================  =========
       1  String Object  NA      String with the case converted
========  =============  ======  ==============================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


--------------------------------------
asg_a2208 : String - Reverse a string.
--------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``my_str_reverse()`` which will reverse a string passed to it.


'''''''
Samples
'''''''
========  ================================================  =============  =============
  Number  Explanation                                       Input          Output
========  ================================================  =============  =============
       1  Reverse a string with odd number of characters.   radar          radar
       2  Reverse a string with even number of characters.  hello, world!  !dlrow ,olleh
       3  Reverse a blank string.
========  ================================================  =============  =============


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``str myreverse(str string)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  ======  ======  ======================  =========
  Number  Type    Name    Explanation             Remarks
========  ======  ======  ======================  =========
       1  str     string  String to be reversed.
========  ======  ======  ======================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  ======  ======  ================  =========
  Number  Type    Name    Explanation       Remarks
========  ======  ======  ================  =========
       1  str     NA      Reversed string.
========  ======  ======  ================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


-----------------------------------------------------------------------
asg_a0013 : String - Toggle the case of all the characters in a string.
-----------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``toggle_case()`` which takes input a string and toggles the case of all the characters in the string.


'''''''
Samples
'''''''
========  =================================================  ===============  ===============
  Number  Explanation                                        Input            Output
========  =================================================  ===============  ===============
       1  Check for basic functionality.                     HelloWorld       hELLOwORLD
       2  Check for functionality with spaces.               Hello World      hELLO wORLD
       3  Check for functionality with special characters.   Hello @#$ World  hELLO @#$ wORLD
       4  Check for functionality with blank string.
       5  Check for functionality with alphanumeric string.  He12Wo           hE12wO
========  =================================================  ===============  ===============


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``str toggle_case(str string)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  ======  ======  ========================================  =========
  Number  Type    Name    Explanation                               Remarks
========  ======  ======  ========================================  =========
       1  str     string  The string whose case has to be toggled.
========  ======  ======  ========================================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  ======  ======  ============================================================  =========
  Number  Type    Name    Explanation                                                   Remarks
========  ======  ======  ============================================================  =========
       1  str     NA      The returned string with the case of the characters toggled.
========  ======  ======  ============================================================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


----------------------------------------------------------------------------------------
asg_a0753 : String2 - Insert the word "Hello" in the middle of the words in an sentence.
----------------------------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``insert_hello()`` which inserts the word ``Hello`` in between of each word present in the passed . (Eg. How are You? -> How Hello are Hello You Hello?)


'''''''
Samples
'''''''
========  =============  =======  ========
Number    Explanation    Input    Output
========  =============  =======  ========
========  =============  =======  ========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``str insert_hello(str sentence)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  ======  ========  ===================  =========
  Number  Type    Name      Explanation          Remarks
========  ======  ========  ===================  =========
       1  str     sentence  The input sentence.
========  ======  ========  ===================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  ======  ======  ========================  =========
  Number  Type    Name    Explanation               Remarks
========  ======  ======  ========================  =========
       1  str     NA      The resulting String is.
========  ======  ======  ========================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


------------------------------------------------------------------------
asg_a0937 : String - Add two binary numbers which are stored as strings.
------------------------------------------------------------------------


'''''''''''
Description
'''''''''''




'''''''
Samples
'''''''
========  =====================================  ==========  ==========
  Number  Explanation                            Input       Output
========  =====================================  ==========  ==========
       1  Check for a general case.              HelloWorld  HeLlOwOrLd
       2  Check for all "lowercase" characters.  helloworld  HeLlOwOrLd
       3  Check for all "UPPERCASE" characters.  HELLOWORLD  HeLlOwOrLd
========  =====================================  ==========  ==========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``string alter_case_1(input)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  =============  ======  ========================  =========
  Number  Type           Name    Explanation               Remarks
========  =============  ======  ========================  =========
       1  String Object  input   String to be worked upon
========  =============  ======  ========================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =============  ======  ==============================  =========
  Number  Type           Name    Explanation                     Remarks
========  =============  ======  ==============================  =========
       1  String Object  NA      String with the case converted
========  =============  ======  ==============================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


---------------------------------------------------
asg_a2209 : String - Check a string for palindrome.
---------------------------------------------------


'''''''''''
Description
'''''''''''

Define a function ``is_palindrome()`` that recognizes palindromes (i.e.  words that look the same written backwards). For example, ``is_palindrome("radar")`` should return ``Success``. In case of blank strings it should return ``Success``


'''''''
Samples
'''''''
========  ==========================================  ===========  ========
  Number  Explanation                                 Input        Output
========  ==========================================  ===========  ========
       1  Check for a palindrome string odd numbered  "radar"      True
       2  Check for a non-palindrome string.          Hello World  False
       3  Check for a blank string.                                False
       4  Check for a even length string.             HEYYEH       True
========  ==========================================  ===========  ========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``boolean is_palindrome(str string)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  ======  ======  =======================================  =========
  Number  Type    Name    Explanation                              Remarks
========  ======  ======  =======================================  =========
       1  str     string  The string to be tested for palindrome.
       2  int     num2    The second number.
========  ======  ======  =======================================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =======  ======  ==========================================================================  =========
  Number  Type     Name    Explanation                                                                 Remarks
========  =======  ======  ==========================================================================  =========
       1  boolean  NA      ``True`` or ``False`` depending on wether the string is palindrome or not.
========  =======  ======  ==========================================================================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


----------------------------------------------------------------------------------
asg_a0003 : String - Program to have alternate case in a string, like "hElLoWoRlD"
----------------------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``alter_case_2("Hello World")`` which converts the case of the characters. The first character should be small.


'''''''
Samples
'''''''
========  ======================================================  ==================  ==================
  Number  Explanation                                             Input               Output
========  ======================================================  ==================  ==================
       1  See if the function works correctly.                    HelloWorld          hELLOwORLD
       2  See if it works correctly on all lowercase characters.  helloworld          hELLOWORLD
       3  See if it works correctly on all Uppercase chars        HELLOWORLD          helloworld
       4  See if it works correctly on blank strings.
       5  See if it works correctly on special characters.        Hello!Wo#rl%  5 4d  hELLO!wO#RL%  5 4D
========  ======================================================  ==================  ==================


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``string alter_case_2(input)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  =============  ======  ========================  =========
  Number  Type           Name    Explanation               Remarks
========  =============  ======  ========================  =========
       1  String Object  input   String to be worked upon
========  =============  ======  ========================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =============  ======  ==============================  =========
  Number  Type           Name    Explanation                     Remarks
========  =============  ======  ==============================  =========
       1  String Object  NA      String with the case converted
========  =============  ======  ==============================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


------------------------------------------------------------------
asg_a0016 : String - Function to check if character is a consonant
------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``is_consonant()`` that takes a character and checks if the character is a consonant or not.


'''''''
Samples
'''''''
========  =================================================  =======  ========
  Number  Explanation                                        Input    Output
========  =================================================  =======  ========
       1  Check if function is working.                      A        False
       2  Check if function is working.                      B        True
       3  Check if function is working for numeric.          2        False
       4  Check if function is working for special symbols.  #        False
       5  Check if function is working for blank input.               False
========  =================================================  =======  ========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``boolean is_consonant(str character)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  ======  =========  ====================  =========
  Number  Type    Name       Explanation           Remarks
========  ======  =========  ====================  =========
       1  char    character  The input character.
========  ======  =========  ====================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =======  ======  ==============================================================  =========
  Number  Type     Name    Explanation                                                     Remarks
========  =======  ======  ==============================================================  =========
       1  boolean  NA      ``True`` if the character is a consonant else return ``False``
========  =======  ======  ==============================================================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


-----------------------------------------------------------------------------
asg_a0873 : String - Write a function to remove all the spaces from a string.
-----------------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``trim_string()`` to remove all the spaces from a string. All spaces include leading spaces, trailing spaces and the spaces in between the words.


'''''''
Samples
'''''''
========  =====================================  =========================  ====================
  Number  Explanation                            Input                      Output
========  =====================================  =========================  ====================
       1  Check if it works in the simple case.  Hello World! How are you.  HelloWordl!Howareyou
========  =====================================  =========================  ====================


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``str trim_string(str string)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  ======  ======  ==========================================  =========
  Number  Type    Name    Explanation                                 Remarks
========  ======  ======  ==========================================  =========
       1  str     string  The string whose spaces has to be removed.
========  ======  ======  ==========================================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  ======  ======  ============================================  =========
  Number  Type    Name    Explanation                                   Remarks
========  ======  ======  ============================================  =========
       1  str     NA      The returned string with the spaces removed.
========  ======  ======  ============================================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


-------------------------------------------------
asg_a2204 : String - Find the length of a string.
-------------------------------------------------


'''''''''''
Description
'''''''''''

Define a function ``my_str_len()`` that computes the length of a given of string.


'''''''
Samples
'''''''
========  ========================  ===========  ========
  Number  Explanation               Input          Output
========  ========================  ===========  ========
       1  Check for a string        hello world        11
       2  Check for a blank string                      0
========  ========================  ===========  ========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``int mylen(str string)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  ======  ======  ========================  =========
  Number  Type    Name    Explanation               Remarks
========  ======  ======  ========================  =========
       1  int     string  String to be worked upon
========  ======  ======  ========================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  ======  ======  ============================  =========
  Number  Type    Name    Explanation                   Remarks
========  ======  ======  ============================  =========
       1  int     NA      Length of the passed string.
========  ======  ======  ============================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


----------------------------------------------------------------------------------
asg_a0755 : String - Find if the other string is a sub-string of the other string.
----------------------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``is_sub_string()`` which returns -1 if the string is not a sub-string, else returns 0.


'''''''
Samples
'''''''
========  =====================================  ==========  ==========
  Number  Explanation                            Input       Output
========  =====================================  ==========  ==========
       1  Check for a general case.              HelloWorld  HeLlOwOrLd
       2  Check for all "lowercase" characters.  helloworld  HeLlOwOrLd
       3  Check for all "UPPERCASE" characters.  HELLOWORLD  HeLlOwOrLd
========  =====================================  ==========  ==========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``string alter_case_1(input)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  =============  ======  ========================  =========
  Number  Type           Name    Explanation               Remarks
========  =============  ======  ========================  =========
       1  String Object  input   String to be worked upon
========  =============  ======  ========================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =============  ======  ==============================  =========
  Number  Type           Name    Explanation                     Remarks
========  =============  ======  ==============================  =========
       1  String Object  NA      String with the case converted
========  =============  ======  ==============================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


----------------------------------------------------------------------------------------------
asg_a0758 : String - Parse a string and find the number of vowels, spaces, special characters.
----------------------------------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``find_information`` which parses a string and finds the numbers of vowels, spaces and special characters. Only the following character needs to be counted !@#$%^&*_


'''''''
Samples
'''''''
========  =====================================  ==========  ==========
  Number  Explanation                            Input       Output
========  =====================================  ==========  ==========
       1  Check for a general case.              HelloWorld  HeLlOwOrLd
       2  Check for all "lowercase" characters.  helloworld  HeLlOwOrLd
       3  Check for all "UPPERCASE" characters.  HELLOWORLD  HeLlOwOrLd
========  =====================================  ==========  ==========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``string alter_case_1(input)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  =============  ======  ========================  =========
  Number  Type           Name    Explanation               Remarks
========  =============  ======  ========================  =========
       1  String Object  input   String to be worked upon
========  =============  ======  ========================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =============  ======  ==============================  =========
  Number  Type           Name    Explanation                     Remarks
========  =============  ======  ==============================  =========
       1  String Object  NA      String with the case converted
========  =============  ======  ==============================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


---------------------------------------------------------------
asg_a0004 : String - Find the lowercase characters in a string.
---------------------------------------------------------------


'''''''''''
Description
'''''''''''


Write a function ``find_lowercase("HelloWorld")`` which returns a string
with lowercase characters present in the string.



'''''''
Samples
'''''''
========  ===================================================  ===================  ==========
  Number  Explanation                                          Input                Output
========  ===================================================  ===================  ==========
       1  Check if the function works                          Hello World          elloorld
       2  Check if it works if all the characters are capital  HELLOWORLD
       3  Check if it works for all the characters small       helloworld           helloworld
       4  Check if special chars are removed                   Hell o ! @#$% world  elloworld
========  ===================================================  ===================  ==========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``string find_lowercase(input)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  =============  ======  ========================  =========
  Number  Type           Name    Explanation               Remarks
========  =============  ======  ========================  =========
       1  String Object  input   String to be worked upon
========  =============  ======  ========================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =============  ======  ==============================  =========
  Number  Type           Name    Explanation                     Remarks
========  =============  ======  ==============================  =========
       1  String Object  NA      String with the case converted
========  =============  ======  ==============================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


-----------------------------------------
asg_a0935 : String - Add two Hex Strings.
-----------------------------------------


'''''''''''
Description
'''''''''''




'''''''
Samples
'''''''
========  =====================================  ==========  ==========
  Number  Explanation                            Input       Output
========  =====================================  ==========  ==========
       1  Check for a general case.              HelloWorld  HeLlOwOrLd
       2  Check for all "lowercase" characters.  helloworld  HeLlOwOrLd
       3  Check for all "UPPERCASE" characters.  HELLOWORLD  HeLlOwOrLd
========  =====================================  ==========  ==========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``string alter_case_1(input)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  =============  ======  ========================  =========
  Number  Type           Name    Explanation               Remarks
========  =============  ======  ========================  =========
       1  String Object  input   String to be worked upon
========  =============  ======  ========================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =============  ======  ==============================  =========
  Number  Type           Name    Explanation                     Remarks
========  =============  ======  ==============================  =========
       1  String Object  NA      String with the case converted
========  =============  ======  ==============================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


----------------------------------------------
asg_a2205 : String - Check character for vowel
----------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``is_vowel(char c)`` a string (of length 1) and returns True if it is a vowel, False otherwise.


'''''''
Samples
'''''''
========  ============================  =======  ========
  Number  Explanation                   Input    Output
========  ============================  =======  ========
       1  Check for a vowel             a        True
       2  Check for a vowel             e        True
       3  Check for a vowel             i        True
       4  Check for a upper case vowel  A        True
       5  Check for a vowel             o        True
========  ============================  =======  ========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``boolean is_vowel(str string)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  ======  ======  =========================  =========
  Number  Type    Name    Explanation                Remarks
========  ======  ======  =========================  =========
       1  str     string  String to be worked upon.
========  ======  ======  =========================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =======  ======  ========================================================================  =========
  Number  Type     Name    Explanation                                                               Remarks
========  =======  ======  ========================================================================  =========
       1  boolean  NA      True if the string if of single character and that character is a vowel.
========  =======  ======  ========================================================================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


-------------------------------------------------
asg_a2212 : String - Generate n times a character
-------------------------------------------------


'''''''''''
Description
'''''''''''

Define a function ``generate_n_chars()`` that takes an integer n and a character c and returns a string, n characters long, consisting only of c:s. For example, generate_n_chars(5, "x") should return the string "xxxxx".


'''''''
Samples
'''''''
========  =========================  ========  ========
  Number  Explanation                Input     Output
========  =========================  ========  ========
       1  Check for a general case.  [5, 'a']  aaaaa
========  =========================  ========  ========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``str generate_n_chars(int n, str string)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  ======  ======  =============================================================  =========
  Number  Type    Name    Explanation                                                    Remarks
========  ======  ======  =============================================================  =========
       1  int     num1    Number of times the character should be reepeated.
       2  str     num2    String of single character. Check if its of single character.
========  ======  ======  =============================================================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  ======  ======  ===================================  =========
  Number  Type    Name    Explanation                          Remarks
========  ======  ======  ===================================  =========
       1  str     NA      String with the character repeated.
========  ======  ======  ===================================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


----------------------------------------------------------------
asg_a0007 : String - Find the upper case characters in a string.
----------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``find_uppercase("Hello")`` which returns a string with all the upper case characters in the string passed.


'''''''
Samples
'''''''
========  =======================================================================  ================  ==========
  Number  Explanation                                                              Input             Output
========  =======================================================================  ================  ==========
       1  Check if the function works.                                             Hello             H
       2  Check if the function works if string has all the upper case charaters.  HELLO WORLD       HELLOWORLD
       3  Check if the function works if string has all the lower case characters  hello world
       4  Check if the function works if string has some special characters.       Hello !@#$ World  HW
========  =======================================================================  ================  ==========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``string alter_case(input)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  =============  ======  ========================  =========
  Number  Type           Name    Explanation               Remarks
========  =============  ======  ========================  =========
       1  String Object  input   String to be worked upon
========  =============  ======  ========================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =============  ======  ==============================  =========
  Number  Type           Name    Explanation                     Remarks
========  =============  ======  ==============================  =========
       1  String Object  NA      String with the case converted
========  =============  ======  ==============================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


-------------------------------------------
asg_a0936 : String - Add two Octal Strings.
-------------------------------------------


'''''''''''
Description
'''''''''''




'''''''
Samples
'''''''
========  =====================================  ==========  ==========
  Number  Explanation                            Input       Output
========  =====================================  ==========  ==========
       1  Check for a general case.              HelloWorld  HeLlOwOrLd
       2  Check for all "lowercase" characters.  helloworld  HeLlOwOrLd
       3  Check for all "UPPERCASE" characters.  HELLOWORLD  HeLlOwOrLd
========  =====================================  ==========  ==========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``string alter_case_1(input)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  =============  ======  ========================  =========
  Number  Type           Name    Explanation               Remarks
========  =============  ======  ========================  =========
       1  String Object  input   String to be worked upon
========  =============  ======  ========================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =============  ======  ==============================  =========
  Number  Type           Name    Explanation                     Remarks
========  =============  ======  ==============================  =========
       1  String Object  NA      String with the case converted
========  =============  ======  ==============================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


---------------------------------------------
asg_a2218 : String - Check palindrome phrases
---------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``check_phrase_palindrome()`` of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami Im a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, Im mad!". Note that punctuation, capitalization, and spacing are being ignored. 


'''''''
Samples
'''''''
========  =============  ================  ========
  Number  Explanation    Input             Output
========  =============  ================  ========
       1                 Rise to vote Sir  True
========  =============  ================  ========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``string alter_case_1(input)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  =============  ======  ========================  =========
  Number  Type           Name    Explanation               Remarks
========  =============  ======  ========================  =========
       1  String Object  input   String to be worked upon
========  =============  ======  ========================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =============  ======  ==============================  =========
  Number  Type           Name    Explanation                     Remarks
========  =============  ======  ==============================  =========
       1  String Object  NA      String with the case converted
========  =============  ======  ==============================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


-----------------------------------------
asg_a0154 : String - left rotate a string
-----------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``rotate_string_left()`` which takes input the number of characters to rotate and rotates the passed string.


'''''''
Samples
'''''''
========  =============  ==================  ===========
  Number  Explanation    Input               Output
========  =============  ==================  ===========
       1                 ["Hello World", 3]  lo WorldHel
========  =============  ==================  ===========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``str rotate_string_left (str string, int n)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  ======  ======  ======================================================  =========
  Number  Type    Name    Explanation                                             Remarks
========  ======  ======  ======================================================  =========
       1  str     string  The string to be worked upon.
       2  int     n       The number of characters you should rotate the string.
========  ======  ======  ======================================================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  ======  ======  ===================  =========
  Number  Type    Name    Explanation          Remarks
========  ======  ======  ===================  =========
       1  str     NA      The rotated string.
========  ======  ======  ===================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage
