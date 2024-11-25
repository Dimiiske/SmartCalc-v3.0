# SmartCalc v3.0

## SmartCalc v3.0 implementation

You need to implement SmartCalc v3.0:

- The program must be developed in Python 3.11.
- The program code must be in the src folder.
- You must stick to Google Code Style when writing code.
- You need to develop a desktop application.
- Prepare the installer, which will install the application to the system with the standard settings (installation path, creating shortcut).
- Prepare an implementation with a graphical user interface for either Linux or Mac OS, based on any GUI library or framework (GUI layer implementation in HTML/CSS/JS is acceptable).
- The program must be implemented using the MVVM or MVP pattern, and:
  - there should be no business logic code in the view code;
  - there must be no interface code in the model, presenter and view model.
- The "core" of the calculator in the form of an algorithm for the formation and calculation of the Polish notation and various computational functions connect as a dynamic library in C/C++ from the SmartCalc v1.0 or SmartCalc v2.0 projects.
- The model should be a "core" with a wrapper in Python.
- The model must have the full functionality of the calculator so that it can be used in the future without the other layers.
- Prepare full coverage of the methods in the model layer with unit tests.
- The application should have a help section with a description of the program interface in random form.
- The program must store the history of operations, allow loading expressions from the history, and clear the entire history.
- The history must be saved between runs of the application.
- Both integers and real numbers can be entered into the program, written either in point or exponential form.
- The calculation should be performed after the complete input of the calculated expression and pressing the `=` symbol.
- Calculation of arbitrary bracketed arithmetic expressions in infix notation.
- Calculate arbitrary parenthesized arithmetic expressions in infix notation with substitution of the _x_ variable as a number.
- Plotting a function defined by an expression in infix notation with the variable _x_ (with coordinate axes, scale markers, and grid with adaptive step):
  - It is not necessary to allow the user to change the scale.
- The definition range and the value range of the functions are limited at least to numbers from -1000000 to 1000000.
- To plot a function, it is also necessary to specify the displayed definition and value ranges.
- The checked accuracy of the fractional part is at least 7 decimal places.
- The user must be able to enter up to 255 characters.
- Bracketed arithmetic expressions in infix notation shall support the following arithmetic operations and mathematical functions:
  - **Arithmetic operators**:

      | Operator name | Infix Notation <br />(Classic) | Prefix notation <br /> (Polish notation) | Postfix notation <br />(Reverse Polish notation) |
      | ------ | ------ | ------ | ------ |
      | Parentheses | (a + b) | (+ a b) | a b + |
      | Addition | a + b | + a b | a b + |
      | Subtraction | a - b | - a b | a b - |
      | Multiplication | a * b | * a b | a b * |
      | Division| a / b | / a b | a b \ |
      | Rasing to the power | a ^ b | ^ a b | a b ^ |
      | Remainder of division | a mod b | mod a b | a b mod |
      | Unary plus | +a | +a | a+ |
      | Unary minus | -a | -a | a- |

      >Please note that the multiplication operator contains a mandatory `*` sign. Processing an expression with the `*` sign omitted is optional and left to the developer's discretion.

      | Function description | Function |
      | ---------------- | ------- |
      | Calculates cosine | cos(x) |
      | Calculates sine | sin(x) |
      | Calculates tangent | tan(x) |
      | Calculates arc cosine | acos(x) |
      | Calculates the arcsine | asin(x) |
      | Calculates arctangent | atan(x) |
      | Calculates square root | sqrt(x) |
      | Calculates natural logarithm | ln(x) |
      | Calculates decimal logarithm | log(x) |
