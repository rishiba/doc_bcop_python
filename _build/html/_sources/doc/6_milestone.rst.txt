

======
Arrays
======


***************
Class 4: Arrays
***************


-------------------------------------------------------------------------
asg_a0650 : Array - Find the sum of all the elements stored in the array?
-------------------------------------------------------------------------


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
asg_a2210 : Array - Check for value in given array.
---------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``is_member()`` that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.) 


'''''''
Samples
'''''''
========  ============================  =================  ========
  Number  Explanation                   Input              Output
========  ============================  =================  ========
       1  Check if function is correst  [2, [1, 2, 3, 4]]  True
========  ============================  =================  ========


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``boolean is_member([ANY] value, [list of ANY] mylist)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  ===========  ======  ===========================================================  =========
  Number  Type         Name    Explanation                                                  Remarks
========  ===========  ======  ===========================================================  =========
       1  list of ANY  mylist  List of elements. The list can have data of multiple types.
========  ===========  ======  ===========================================================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  =======  ======  ==============================================  =========
  Number  Type     Name    Explanation                                     Remarks
========  =======  ======  ==============================================  =========
       1  boolean  NA      ``True`` or ``False`` depending on the result.
========  =======  ======  ==============================================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


-------------------------------------------------------------------------------------
asg_a0920 : Array - Convert a number like 123456 to an array as { 1, 2, 3, 4, 5, 6 }.
-------------------------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``convert_number_to_array()``  which takes input an integer and splits up the digits to store it into an array. Each element of the array has respective digits of the input number. The function should return the resulted array


'''''''
Samples
'''''''
========  =========================  =======  ===============
  Number  Explanation                  Input  Output
========  =========================  =======  ===============
       1  Check for a general case.    12345  [1, 2, 3, 4, 5]
========  =========================  =======  ===============


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


-------------------------------------------------------------------------------------
asg_a0921 : Array - Convert a number like 123456 to an array as { 6, 5, 4, 3, 2, 1 }.
-------------------------------------------------------------------------------------


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


-----------------------------------------------------------------------------
asg_a0651 : Array - Find the product of all the elements stored in the array.
-----------------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``product_of_array(int arr)`` which multiplies all the elements of the array and returns the multiplied result value. The function takes an array as input. Return 0 if the array is empty.


'''''''
Samples
'''''''
========  ==================================  ==============  ========
  Number  Explanation                         Input             Output
========  ==================================  ==============  ========
       1  Check for a general case.           [10, 20, 2, 4]      1600
       2  Check when zero as an input number  [10, 20, 0, 4]         0
       3  Check for empty array               []                     0
========  ==================================  ==============  ========


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


--------------------------------------------------------------------
asg_a0652 : Array - Find the maximum and minimum element of an array
--------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``find_min_max(int arr)`` which returns the minimum and maximum element contained in a 1 D array. An integer array is passed as input to the function.  Return 0 if successful. If the array is empty then return -1.


'''''''
Samples
'''''''
========  ==================================  ==================  =========
  Number  Explanation                         Input               Output
========  ==================================  ==================  =========
       1  Check for a general case.           [10, 20, 2, 4]      [2, 20]
       2  Check when zero as an input number  [10, 20, 0, 4]      [0, 20]
       3  Check for empty array               []                  0
       4  Check for negative values           [-20, -10, -5, -1]  [-20, -1]
========  ==================================  ==================  =========


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


-------------------------------------------------------------------------------------------------------------------------------------------------------
asg_a0656 : Array - Fill an array with the multiples of 3, then remove the numbers which are divisible by 5. Fill the empty spaces so generated with -1
-------------------------------------------------------------------------------------------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``fill_array(int n)`` which fills the array of n length with multiples of 3. Then remove those elements which are divisible by 5. This would leave you with few empty spaces in the array. Fill these empty spaces with -1. Return the finally generated array.


'''''''
Samples
'''''''
========  ==================================  =======  =====================================
  Number  Explanation                         Input    Output
========  ==================================  =======  =====================================
       1  Check for a general case.           [5]      [3, 6, 9, 12, -1]
       2  Check when zero as an input number  [10]     [3, 6, 9, 12, -1, 18, 21, 24, 27, -1]
       3  Check for empty array               [0]      0
========  ==================================  =======  =====================================


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


------------------------------------------------------------------------------------
asg_a2207 : Array - Perform sum and multiplication of multiple elements in an array.
------------------------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Define a function ``sum_and_multiply()`` which multiplies the elements in an array as well as adds all the elements in an array and returns the final sum and product. Return 0 if successful. If the array is of length 0 then return -1.


'''''''
Samples
'''''''
========  ====================================================  ===========================  ====================
  Number  Explanation                                           Input                                      Output
========  ====================================================  ===========================  ====================
       1  Sum works correctly.                                  [1, 2, 3, 4]                                   10
       2  Sum works correctly for negative numbers.             [1, -1, 2, -2, 4]                               4
       3  Multiplication works correctly.                       [1, 2, 3, 4, 5]                               120
       4  Multiplication works correctly for negative numbers.  [1, -2, 3, 4]                                 -24
       5  Multiplication works correctly for large numbers.     [1000000, 2000000, 9000000]  18000000000000000000
========  ====================================================  ===========================  ====================


''''''''
Function
''''''''


^^^^^^^^^^^^^^^^^^
Function Signature
^^^^^^^^^^^^^^^^^^

``int mysum((list of integers) int_list)``


^^^^^^^^^^^^^^^^^^
Function Arguments
^^^^^^^^^^^^^^^^^^
========  ================  ========  ===================================  =========
  Number  Type              Name      Explanation                          Remarks
========  ================  ========  ===================================  =========
       1  list of integers  int_list  List of integers to be worked upon.
========  ================  ========  ===================================  =========


^^^^^^^^^^^^
Return Value
^^^^^^^^^^^^
========  ======  ======  ==============================  =========
  Number  Type    Name    Explanation                     Remarks
========  ======  ======  ==============================  =========
       1  int     NA      Sum of the elements of a list.
========  ======  ======  ==============================  =========


''''''''''''''''''''
Function Placeholder
''''''''''''''''''''

::


.. raw:: latex

    \clearpage


--------------------------------------------------------------
asg_a2425 : Array - Count the odd numbers in the even indexes.
--------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``count_odd_at_even()`` which stores the odd numbers in the array in another array, and also returns the length of the returning array. If the array is of length 0 return -1, else return 0.


'''''''
Samples
'''''''
========  ==================================  ===============  ========
  Number  Explanation                         Input              Output
========  ==================================  ===============  ========
       1  Check for a general case.           [1, 2, 2, 4, 4]         1
       2  Check when zero as an input number  [1, 2, 0, 4]            1
       3  Check for empty array               []                      0
========  ==================================  ===============  ========


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


-----------------------------------------------
asg_a0926 : Array - Convert a octal to decimal.
-----------------------------------------------


'''''''''''
Description
'''''''''''




'''''''
Samples
'''''''
========  ===============================  =======  ========
  Number  Explanation                      Input      Output
========  ===============================  =======  ========
       1  Check if the function is proper  [3]             5
       2  Check if the function is proper  [12]            0
========  ===============================  =======  ========


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


------------------------------------------------
asg_a0930 : Array - Convert a binary to decimal.
------------------------------------------------


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
asg_a0934 : Array - Convert a octal to binary.
----------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``convert_octal_to_binary()``.


'''''''
Samples
'''''''
========  ===============================  =======  ========
  Number  Explanation                      Input      Output
========  ===============================  =======  ========
       1  Check if the function is proper  [3]             5
       2  Check if the function is proper  [12]            0
========  ===============================  =======  ========


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


-----------------------------------------------------
asg_a0923 : Array - Convert a decimal to hexadecimal.
-----------------------------------------------------


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


-----------------------------------------------------
asg_a0927 : Array - Convert a hexadecimal to decimal.
-----------------------------------------------------


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


-----------------------------------------------
asg_a0925 : Array - Convert a decimal to octal.
-----------------------------------------------


'''''''''''
Description
'''''''''''




'''''''
Samples
'''''''
========  ===============================  =======  ========
  Number  Explanation                      Input      Output
========  ===============================  =======  ========
       1  Check if the function is proper  [3]             5
       2  Check if the function is proper  [12]            0
========  ===============================  =======  ========


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


------------------------------------------------
asg_a0929 : Array - Convert a decimal to binary.
------------------------------------------------


'''''''''''
Description
'''''''''''




'''''''
Samples
'''''''
========  ===============================  =======  ========
  Number  Explanation                      Input      Output
========  ===============================  =======  ========
       1  Check if the function is proper  [3]             5
       2  Check if the function is proper  [12]            0
========  ===============================  =======  ========


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


------------------------------------------------------------
asg_a0924 : Array - Convert a decimal to a number in base 6.
------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``convert_decimal_to_base_6()`` will convert the passed number to a number represented in base 6.


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
asg_a0928 : Array - Convert a hexadecimal to octal.
---------------------------------------------------


'''''''''''
Description
'''''''''''




'''''''
Samples
'''''''
========  ===============================  =======  ========
  Number  Explanation                      Input      Output
========  ===============================  =======  ========
       1  Check if the function is proper  [3]             5
       2  Check if the function is proper  [12]            0
========  ===============================  =======  ========


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


----------------------------------------------------
asg_a0932 : Array - Convert a binary to hexadecimal.
----------------------------------------------------


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


---------------------------------------------------------------------------------------
asg_a0664 : Array - Write a program to find all the prime numbers in a range of 1 to N.
---------------------------------------------------------------------------------------


'''''''''''
Description
'''''''''''

Write a function ``generate_prime_numbers()`` which will generate numbers from 1 to N and put it in an array. If the length of array passed is less than the numbers generated then return -1, else return 0.


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


------------------------------------------------------------------------------------
asg_a0277 : Loop - Write a function ``print_pattern_04()`` which prints the pattern.
------------------------------------------------------------------------------------


'''''''''''
Description
'''''''''''


::
    
    HELLOXHELLO
    HELLO HELLO
    HELL   ELLO
    HEL     LLO
    HE       LO
    H         O
    HE       LO
    HEL     LLO
    HELL   ELLO
    HELLO HELLO
    HELLOXHELLO



'''''''
Samples
'''''''
========  =============  =======  ========
  Number  Explanation    Input    Output
========  =============  =======  ========
       1                          #
========  =============  =======  ========


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
