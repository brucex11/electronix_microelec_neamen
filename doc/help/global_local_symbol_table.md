In Python, the **global symbol table** is a dictionary that holds all the global variables and functions for the current module or script. It is used to store the symbols (names) that are accessible globally, meaning they are available for use throughout the entire script or module. This symbol table is created when a program starts and is deleted when the program terminates.

### Global Symbol Table Details:
- The global symbol table includes:
  - Global variables: Variables declared outside any functions.
  - Functions and classes defined at the top level.
  - Imported modules and their objects.

- The symbol table is typically accessible through Python's built-in function `globals()`. Calling `globals()` returns the global symbol table as a dictionary, where the keys are the names (strings), and the values are the corresponding objects (variables, functions, etc.).

#### Example:
```python
x = 10  # global variable

def my_function():
    y = 5  # local variable
    print(globals())  # prints the global symbol table

my_function()
```

In this example:
- The global symbol table would include `x`, `my_function`, and any other objects defined globally.
- When `globals()` is called inside `my_function`, it will give access to the global symbol table.

#### Global vs. Local Symbol Tables:
- The **local symbol table** stores variables that are specific to a function, method, or class.
- The **global symbol table** stores variables and functions that are accessible throughout the module.

By default, Python looks for names first in the **local** symbol table, then in the **enclosing** symbol tables (if any), and finally in the **global** symbol table.


```
	class_name:str = 'class_dataprep'
	print(globals()[class_name])
	class_ref = globals()[class_name]
	print( f"class-ref: {class_ref}" )
	params = [pcf,lg]
	dinst = class_ref.DataPrep(*params)
```
