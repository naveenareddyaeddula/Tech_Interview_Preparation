# Top 50 Python Interview Questions for 3-4 Years Experience

## THEORETICAL QUESTIONS (25)

### Core Python Concepts

1. **Explain the difference between mutable and immutable objects in Python. Give examples.**
   
   **Answer:**
   - **Mutable objects** can be changed after creation: lists, dictionaries, sets, bytearray
   - **Immutable objects** cannot be changed after creation: strings, tuples, frozensets, integers, floats
   - **Implications:**
     - Mutable objects are passed by reference; changes inside functions affect the original object
     - Immutable objects are effectively passed by value
     - Immutable objects can be dictionary keys; mutable objects cannot
   
   ```python
   # Mutable example
   list1 = [1, 2, 3]
   list2 = list1
   list2.append(4)
   print(list1)  # [1, 2, 3, 4] - both reference same object
   
   # Immutable example
   str1 = "hello"
   str2 = str1
   str2 = str2 + " world"
   print(str1)  # "hello" - original unchanged
   ```

2. **What are decorators? Write a simple decorator example.**
   
   **Answer:**
   Decorators are functions that take another function/class as input and extend its behavior without permanently modifying it. They use the @ syntax.
   
   ```python
   def my_decorator(func):
       def wrapper(*args, **kwargs):
           print(f"Before calling {func.__name__}")
           result = func(*args, **kwargs)
           print(f"After calling {func.__name__}")
           return result
       return wrapper
   
   @my_decorator
   def say_hello(name):
       print(f"Hello, {name}!")
   
   say_hello("Alice")
   # Output:
   # Before calling say_hello
   # Hello, Alice!
   # After calling say_hello
   ```
   
   Common use cases: logging, authentication, timing, caching, validation

3. **Explain the Global Interpreter Lock (GIL) and its implications.**
   
   **Answer:**
   - **GIL** is a mutex that protects access to Python objects in CPython, allowing only one thread to execute Python bytecode at a time
   - **Why it exists:** Simplifies memory management and makes single-threaded programs faster
   - **Implications:**
     - Multithreading doesn't provide true parallelism for CPU-bound tasks
     - Multithreading works well for I/O-bound tasks (network, file operations)
     - For CPU-bound tasks, use multiprocessing instead
   
   ```python
   # CPU-bound: Use multiprocessing
   from multiprocessing import Pool
   
   # I/O-bound: Threading is fine
   import threading
   ```

4. **What is a generator? How does it differ from a regular function?**
   
   **Answer:**
   Generators are functions that use `yield` to return values one at a time, creating an iterator. They use lazy evaluation.
   
   ```python
   # Regular function - returns all at once
   def get_numbers():
       result = []
       for i in range(1000000):
           result.append(i)
       return result
   
   # Generator - yields one at a time
   def get_numbers_gen():
       for i in range(1000000):
           yield i
   
   # Benefits: Memory efficient, can generate infinite sequences
   ```
   
   **Differences:**
   - Generators use less memory (don't store all values)
   - Generators are lazy (compute values on demand)
   - Generators can represent infinite sequences
   - Generators can only be iterated once

5. **Explain list comprehension and generator expressions. What's the difference?**
   
   **Answer:**
   - **List comprehension** creates a complete list in memory
   - **Generator expression** creates an iterator that generates values on demand
   
   ```python
   # List comprehension - creates full list
   list_comp = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
   
   # Generator expression - lazy evaluation
   gen_exp = (x**2 for x in range(5))  # generator object
   
   # Memory usage: generator uses much less for large datasets
   # Generator expression syntax uses () instead of []
   ```

6. **What are *args and **kwargs? Provide usage examples.**
   
   **Answer:**
   - ***args** collects positional arguments as a tuple
   - ****kwargs** collects keyword arguments as a dictionary
   
   ```python
   def my_function(*args, **kwargs):
       print(f"args: {args}")
       print(f"kwargs: {kwargs}")
   
   my_function(1, 2, 3, name="Alice", age=30)
   # Output:
   # args: (1, 2, 3)
   # kwargs: {'name': 'Alice', 'age': 30}
   
   # Use case: forwarding arguments
   def wrapper(*args, **kwargs):
       return original_function(*args, **kwargs)
   ```

7. **Explain monkey patching in Python. Is it a good practice?**
   
   **Answer:**
   Monkey patching is dynamically modifying classes/modules at runtime.
   
   ```python
   # Example
   import datetime
   original_now = datetime.datetime.now
   
   def mock_now():
       return datetime.datetime(2020, 1, 1)
   
   datetime.datetime.now = mock_now
   ```
   
   **Pros:** Useful for testing and quick fixes
   **Cons:** Makes code unpredictable, harder to debug, breaks maintainability
   **Best practice:** Use only in tests with mocking libraries (unittest.mock, pytest)

8. **What is the difference between shallow copy and deep copy?**
   
   **Answer:**
   - **Shallow copy** copies the object but references to nested objects remain the same
   - **Deep copy** recursively copies the object and all nested objects
   
   ```python
   import copy
   
   original = [[1, 2], [3, 4]]
   
   shallow = copy.copy(original)
   shallow[0][0] = 999
   print(original)  # [[999, 2], [3, 4]] - affected!
   
   deep = copy.deepcopy(original)
   deep[0][0] = 999
   print(original)  # [[1, 2], [3, 4]] - not affected
   ```

9. **Explain closures and how they work in Python.**
   
   **Answer:**
   A closure is a function that references variables from its outer scope. The inner function "closes over" the variables.
   
   ```python
   def outer(x):
       def inner(y):
           return x + y  # x is from outer scope
       return inner
   
   add_five = outer(5)
   print(add_five(3))  # 8
   
   # Use case: function factories, callbacks
   def multiplier(n):
       def multiply(x):
           return x * n
       return multiply
   
   times_three = multiplier(3)
   print(times_three(10))  # 30
   ```

10. **What are metaclasses? What problem do they solve?**
    
    **Answer:**
    Metaclasses are "classes of classes" - they define how a class behaves. Everything in Python is an object, including classes.
    
    ```python
    # Classes are instances of type (the default metaclass)
    class MyClass:
        pass
    
    print(type(MyClass))  # <class 'type'>
    
    # Custom metaclass example
    class CustomMeta(type):
        def __new__(mcs, name, bases, dct):
            dct['custom_attr'] = True
            return super().__new__(mcs, name, bases, dct)
    
    class MyClass(metaclass=CustomMeta):
        pass
    
    print(MyClass.custom_attr)  # True
    ```
    
    **Use cases:** ORM frameworks (Django), API frameworks, enforcing class design patterns

11. **Explain property decorators (@property). When should you use them?**
    
    **Answer:**
    Properties allow you to use getter/setter logic while maintaining attribute-like syntax.
    
    ```python
    class Circle:
        def __init__(self, radius):
            self._radius = radius
        
        @property
        def radius(self):
            return self._radius
        
        @radius.setter
        def radius(self, value):
            if value <= 0:
                raise ValueError("Radius must be positive")
            self._radius = value
        
        @property
        def area(self):
            return 3.14 * self._radius ** 2
    
    c = Circle(5)
    print(c.area)  # 78.5 - looks like attribute access
    c.radius = 10  # Calls setter
    ```
    
    **Use cases:** Encapsulation, validation, computed properties

12. **What is the purpose of __init__.py in packages?**
    
    **Answer:**
    - Makes a directory a Python package
    - Executed when the package is imported
    - Can initialize package-level variables and functions
    - Optional in Python 3.3+ (namespace packages)
    
    ```python
    # mypackage/__init__.py
    print("Package imported!")
    from .module1 import func1
    from .module2 import func2
    
    __all__ = ['func1', 'func2']
    ```

13. **Explain virtual environments and why they're important.**
    
    **Answer:**
    Virtual environments isolate Python dependencies for different projects.
    
    ```bash
    # Create
    python -m venv venv
    
    # Activate (Linux/Mac)
    source venv/bin/activate
    
    # Activate (Windows)
    venv\Scripts\activate
    ```
    
    **Benefits:**
    - Avoid version conflicts between projects
    - Reproducible deployments
    - Easy dependency management with requirements.txt
    - Keep system Python clean

14. **What is the difference between is and == in Python?**
    
    **Answer:**
    - **`==`** checks value equality (calls `__eq__` method)
    - **`is`** checks identity (same object in memory)
    
    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    
    print(a == b)  # True - same values
    print(a is b)  # False - different objects
    print(a is c)  # True - same object
    
    # Edge case: small integers are cached
    x = 256
    y = 256
    print(x is y)  # True (CPython optimization)
    
    x = 257
    y = 257
    print(x is y)  # False (not cached)
    ```

15. **Explain the Python MRO (Method Resolution Order). How is it determined?**
    
    **Answer:**
    MRO determines the order in which methods are searched in a hierarchy of classes (important with multiple inheritance).
    
    ```python
    class A:
        def method(self):
            print("A")
    
    class B(A):
        def method(self):
            print("B")
    
    class C(A):
        def method(self):
            print("C")
    
    class D(B, C):
        pass
    
    d = D()
    d.method()  # "B"
    
    print(D.mro())
    # [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
    
    # Use super() to call parent method
    class B(A):
        def method(self):
            super().method()
            print("B")
    ```
    
    Uses C3 linearization algorithm. View with `ClassName.__mro__`

16. **What are context managers? How do you create one?**
    
    **Answer:**
    Context managers manage resource setup and cleanup using `with` statement.
    
    ```python
    # Built-in example
    with open('file.txt') as f:
        data = f.read()
    # File automatically closed
    
    # Create custom context manager
    class MyContextManager:
        def __enter__(self):
            print("Setting up")
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("Cleaning up")
            return False  # Don't suppress exceptions
    
    with MyContextManager() as mcm:
        print("Using resource")
    
    # Or using decorator
    from contextlib import contextmanager
    
    @contextmanager
    def my_context():
        print("Setup")
        try:
            yield
        finally:
            print("Cleanup")
    
    with my_context():
        print("Using")
    ```

17. **Explain the difference between list, tuple, and set.**
    
    **Answer:**
    
    | Feature | List | Tuple | Set |
    |---------|------|-------|-----|
    | Mutable | Yes | No | Yes |
    | Ordered | Yes | Yes | No |
    | Unique | No | No | Yes |
    | Hashable | No | Yes | No |
    | Duplicates | Allowed | Allowed | Not allowed |
    
    ```python
    # Lists: ordered, mutable, for sequences
    list1 = [1, 2, 2, 3]
    
    # Tuples: ordered, immutable, for fixed data
    tuple1 = (1, 2, 3)
    dict_keys = {tuple1: "value"}  # Can be dict key
    
    # Sets: unordered, unique, for membership testing
    set1 = {1, 2, 3}
    print(2 in set1)  # O(1) lookup
    ```

18. **What is duck typing in Python?**
    
    **Answer:**
    "If it walks like a duck and quacks like a duck, then it's a duck." Focus on behavior, not type.
    
    ```python
    # Don't check type
    if isinstance(obj, MyClass):
        obj.method()
    
    # Just use it
    try:
        obj.method()
    except AttributeError:
        pass
    
    # Example
    def process(obj):
        return obj.read()  # Works for file, StringIO, socket, etc.
    ```
    
    **Benefits:** Flexibility, polymorphism without inheritance

19. **Explain lambda functions and their limitations.**
    
    **Answer:**
    Lambda functions are anonymous functions defined with single expression.
    
    ```python
    # Basic syntax: lambda arguments: expression
    square = lambda x: x ** 2
    print(square(5))  # 25
    
    # Use with map, filter, sorted
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x**2, numbers))
    
    # Sorted by key
    students = [('Alice', 25), ('Bob', 20)]
    sorted(students, key=lambda x: x[1])
    ```
    
    **Limitations:**
    - Only single expression (no statements)
    - Can't contain loops, if statements
    - Hard to debug
    - Less readable than named functions
    
    **Best practice:** Use for simple, one-off functions only

20. **What is PEP 8? What are key style guidelines?**
    
    **Answer:**
    PEP 8 is Python's style guide for code formatting and conventions.
    
    **Key guidelines:**
    - 4 spaces for indentation (not tabs)
    - Max line length: 79 characters (docstrings/comments: 72)
    - Two blank lines between top-level functions/classes
    - One blank line between methods
    
    ```python
    # Naming conventions
    my_variable = 10  # lowercase with underscores
    MyClass = object  # CapWords for classes
    CONSTANT = 100    # UPPERCASE for constants
    _private = None   # Leading underscore for internal
    
    # Imports
    import os
    import sys
    from collections import OrderedDict
    
    # Whitespace
    x = 1  # around operators
    func(a, b)  # after commas
    ```
    
    Tools: `black`, `flake8`, `pylint` for enforcing PEP 8

21. **Explain async/await in Python. How does it work?**
    
    **Answer:**
    Async/await allows concurrent I/O-bound operations without threads.
    
    ```python
    import asyncio
    
    async def fetch_data(delay):
        print(f"Start fetching ({delay}s)")
        await asyncio.sleep(delay)
        print(f"Done fetching")
        return "data"
    
    async def main():
        # Run concurrently
        results = await asyncio.gather(
            fetch_data(1),
            fetch_data(2),
            fetch_data(1)
        )
        print(results)
    
    asyncio.run(main())
    # Total time: ~2 seconds (not 4)
    ```
    
    **How it works:**
    - Event loop runs one coroutine at a time
    - When await is encountered, event loop can switch to another coroutine
    - Perfect for I/O-bound operations

22. **What is the difference between append(), extend(), and insert() for lists?**
    
    **Answer:**
    
    ```python
    lst = [1, 2, 3]
    
    # append(): adds single element at end
    lst.append(4)
    print(lst)  # [1, 2, 3, 4]
    
    lst.append([5, 6])
    print(lst)  # [1, 2, 3, 4, [5, 6]]
    
    # extend(): adds multiple elements at end
    lst = [1, 2, 3]
    lst.extend([4, 5])
    print(lst)  # [1, 2, 3, 4, 5]
    
    # insert(): adds element at specific position
    lst = [1, 2, 3]
    lst.insert(1, 'X')
    print(lst)  # [1, 'X', 2, 3]
    ```

23. **Explain slicing in Python. What does [::-1] do?**
    
    **Answer:**
    Slicing creates a subset of a sequence using `[start:stop:step]`
    
    ```python
    s = "Hello"
    
    s[1:4]      # "ell" - indices 1, 2, 3
    s[:3]       # "Hel" - from start to index 3
    s[2:]       # "llo" - from index 2 to end
    s[::2]      # "Hlo" - every 2nd character
    s[::-1]     # "olleH" - reverse!
    s[1:4:2]    # "el" - indices 1, 3
    
    # Negative indices
    s[-1]       # "o" - last character
    s[-3:]      # "llo" - last 3 characters
    ```

24. **What are Python's built-in string methods? Name 10 commonly used ones.**
    
    **Answer:**
    
    ```python
    s = "  Hello World  "
    
    s.strip()           # "Hello World" - remove whitespace
    s.lower()           # "  hello world  "
    s.upper()           # "  HELLO WORLD  "
    s.replace("o", "0") # "  Hell0 W0rld  "
    s.split()           # ['Hello', 'World'] - split by whitespace
    " ".join(['a', 'b']) # "a b" - join list
    s.find("World")     # 7 - find substring index (-1 if not found)
    s.startswith("  ")  # True
    s.endswith("  ")    # True
    s.format(name="Alice") # "Hello {name}" → "Hello Alice"
    s.count("l")        # 3 - count occurrences
    ```

25. **Explain exception handling in Python. What's the difference between except Exception and except BaseException?**
    
    **Answer:**
    
    ```python
    # Exception hierarchy
    BaseException
    ├── SystemExit
    ├── KeyboardInterrupt
    ├── GeneratorExit
    └── Exception
        ├── StopIteration
        ├── ValueError
        ├── KeyError
        └── ...
    
    # Difference
    try:
        # code
    except Exception as e:       # Catches most exceptions
        print(f"Error: {e}")
    except BaseException as e:   # Catches everything including SystemExit
        print(f"Serious error: {e}")
    
    # Best practice
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print("No error occurred")
    finally:
        print("Cleanup code always runs")
    
    # Create custom exceptions
    class CustomError(Exception):
        pass
    
    raise CustomError("Something went wrong")
    ```

---

## CODING QUESTIONS (25)

### Beginner to Intermediate Level

26. **Reverse a string without using slicing.**
    
    **Answer:**
    ```python
    def reverse_string(s):
        result = ""
        for char in s:
            result = char + result
        return result
    
    # Better approach
    def reverse_string_v2(s):
        result = []
        for i in range(len(s) - 1, -1, -1):
            result.append(s[i])
        return "".join(result)
    
    print(reverse_string("hello"))  # "olleh"
    ```
    
    **Time Complexity:** O(n²) for v1, O(n) for v2
    **Space Complexity:** O(n)

27. **Check if a number is a palindrome.**
    
    **Answer:**
    ```python
    def is_palindrome(num):
        s = str(abs(num))  # Handle negative numbers
        return s == s[::-1]
    
    # Without using slicing
    def is_palindrome_v2(num):
        s = str(abs(num))
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    print(is_palindrome(121))    # True
    print(is_palindrome(-121))   # True
    print(is_palindrome(123))    # False
    ```
    
    **Time Complexity:** O(n) where n is number of digits
    **Space Complexity:** O(n)

28. **Find the second largest element in a list.**
    
    **Answer:**
    ```python
    # Simple approach
    def second_largest(lst):
        unique_lst = list(set(lst))
        unique_lst.sort()
        return unique_lst[-2]
    
    # Better approach - O(n)
    def second_largest_v2(lst):
        if len(lst) < 2:
            return None
        
        largest = second = float('-inf')
        for num in lst:
            if num > largest:
                second = largest
                largest = num
            elif num > second and num != largest:
                second = num
        return second
    
    print(second_largest([3, 1, 4, 1, 5, 9, 2]))  # 5
    ```
    
    **Time Complexity:** O(n)
    **Space Complexity:** O(1)

29. **Remove duplicates from a list while maintaining order.**
    
    **Answer:**
    ```python
    # Using dict (preserves order in Python 3.7+)
    def remove_duplicates_v1(lst):
        return list(dict.fromkeys(lst))
    
    # Using set with manual ordering
    def remove_duplicates_v2(lst):
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    # Using list comprehension trick
    def remove_duplicates_v3(lst):
        seen = set()
        return [x for x in lst if not (x in seen or seen.add(x))]
    
    print(remove_duplicates_v1([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]
    ```
    
    **Time Complexity:** O(n)
    **Space Complexity:** O(n)

30. **Implement a function that flattens a nested list.**
    
    **Answer:**
    ```python
    # Recursive approach
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))  # Recursive call
            else:
                result.append(item)
        return result
    
    # Iterative approach with stack
    def flatten_iterative(lst):
        result = []
        stack = [lst]
        while stack:
            for item in stack.pop():
                if isinstance(item, list):
                    stack.append(item)
                else:
                    result.append(item)
        return result
    
    # Using generator
    def flatten_gen(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten_gen(item)
            else:
                yield item
    
    nested = [1, [2, 3, [4, 5]], 6]
    print(flatten(nested))  # [1, 2, 3, 4, 5, 6]
    ```
    
    **Time Complexity:** O(n)
    **Space Complexity:** O(n)

31. **Count the frequency of each character in a string.**
    
    **Answer:**
    ```python
    # Dict comprehension
    def char_frequency_v1(s):
        return {char: s.count(char) for char in set(s)}
    
    # Counter (best approach)
    from collections import Counter
    def char_frequency_v2(s):
        return dict(Counter(s))
    
    # Manual approach
    def char_frequency_v3(s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        return freq
    
    print(char_frequency_v1("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    ```
    
    **Time Complexity:** O(n)
    **Space Complexity:** O(k) where k is unique characters

32. **Find the longest common prefix in a list of strings.**
    
    **Answer:**
    ```python
    # Horizontal scanning
    def longest_common_prefix_v1(strs):
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    
    # Vertical scanning
    def longest_common_prefix_v2(strs):
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
    
    # Zip approach
    def longest_common_prefix_v3(strs):
        if not strs:
            return ""
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs)
    
    print(longest_common_prefix_v1(["flower", "flow", "flight"]))  # "fl"
    ```
    
    **Time Complexity:** O(n * m) where n is number of strings, m is length
    **Space Complexity:** O(1)

33. **Merge two sorted lists into a single sorted list.**
    
    **Answer:**
    ```python
    # Simple approach
    def merge_sorted_v1(list1, list2):
        return sorted(list1 + list2)
    
    # Two-pointer approach (optimal)
    def merge_sorted_v2(list1, list2):
        result = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        result.extend(list1[i:])
        result.extend(list2[j:])
        return result
    
    print(merge_sorted_v2([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
    ```
    
    **Time Complexity:** O(n + m)
    **Space Complexity:** O(n + m)

34. **Find all pairs in a list that sum to a target value.**
    
    **Answer:**
    ```python
    # Using set
    def find_pairs_v1(lst, target):
        seen = set()
        pairs = set()
        for num in lst:
            complement = target - num
            if complement in seen:
                pairs.add((min(num, complement), max(num, complement)))
            seen.add(num)
        return list(pairs)
    
    # Using two-pointer (works if sorted)
    def find_pairs_v2(lst, target):
        lst = sorted(lst)
        pairs = []
        left, right = 0, len(lst) - 1
        while left < right:
            total = lst[left] + lst[right]
            if total == target:
                pairs.append((lst[left], lst[right]))
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
        return pairs
    
    print(find_pairs_v1([1, 5, 7, -1, 5], 6))  # {(1, 5)}
    ```
    
    **Time Complexity:** O(n)
    **Space Complexity:** O(n)

35. **Implement FizzBuzz.**
    
    **Answer:**
    ```python
    # Basic approach
    def fizzbuzz_v1(n):
        for i in range(1, n + 1):
            output = ""
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            print(output or i)
    
    # One-liner approach
    def fizzbuzz_v2(n):
        for i in range(1, n + 1):
            print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)
    
    # Return list instead of printing
    def fizzbuzz_v3(n):
        return ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i) 
                for i in range(1, n + 1)]
    
    fizzbuzz_v1(15)
    # Output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
    ```
    
    **Time Complexity:** O(n)
    **Space Complexity:** O(1)

36. **Check if a string is an anagram of another.**
    
    **Answer:**
    ```python
    # Using sorted
    def is_anagram_v1(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    
    # Using Counter
    from collections import Counter
    def is_anagram_v2(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    
    # Using dict
    def is_anagram_v3(s1, s2):
        if len(s1) != len(s2):
            return False
        char_count = {}
        for char in s1.lower():
            char_count[char] = char_count.get(char, 0) + 1
        for char in s2.lower():
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        return True
    
    print(is_anagram_v1("listen", "silent"))  # True
    print(is_anagram_v1("hello", "world"))    # False
    ```
    
    **Time Complexity:** O(n log n) for sorted, O(n) for Counter
    **Space Complexity:** O(n)

37. **Find the most frequent element in a list.**
    
    **Answer:**
    ```python
    from collections import Counter
    
    # Using Counter (best)
    def most_frequent_v1(lst):
        return Counter(lst).most_common(1)[0][0]
    
    # Using max with key
    def most_frequent_v2(lst):
        return max(set(lst), key=lst.count)
    
    # Manual approach
    def most_frequent_v3(lst):
        max_count = 0
        max_element = None
        for item in set(lst):
            count = lst.count(item)
            if count > max_count:
                max_count = count
                max_element = item
        return max_element
    
    print(most_frequent_v1([1, 1, 1, 2, 3, 3]))  # 1
    ```
    
    **Time Complexity:** O(n)
    **Space Complexity:** O(n)

38. **Implement a simple Fibonacci function.**
    
    **Answer:**
    ```python
    # Recursive (inefficient - exponential time)
    def fib_recursive(n):
        if n <= 1:
            return n
        return fib_recursive(n - 1) + fib_recursive(n - 2)
    
    # Recursive with memoization
    def fib_memo(n, cache={}):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
        return cache[n]
    
    # Iterative (best)
    def fib_iterative(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    print(fib_iterative(10))  # 55
    ```
    
    **Time Complexity:** O(2^n) recursive, O(n) iterative
    **Space Complexity:** O(n) recursive, O(1) iterative

39. **Rotate a list by k positions.**
    
    **Answer:**
    ```python
    # Simple slicing
    def rotate_v1(lst, k):
        k = k % len(lst)
        return lst[-k:] + lst[:-k]
    
    # Reverse algorithm
    def rotate_v2(lst, k):
        k = k % len(lst)
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        reverse(lst, 0, len(lst) - 1)
        reverse(lst, 0, k - 1)
        reverse(lst, k, len(lst) - 1)
        return lst
    
    # In-place rotation
    def rotate_v3(lst, k):
        k = k % len(lst)
        lst[:] = lst[-k:] + lst[:-k]
    
    print(rotate_v1([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
    ```
    
    **Time Complexity:** O(n)
    **Space Complexity:** O(1) for in-place, O(n) for slicing

40. **Find the missing number in an array of 1 to n.**
    
    **Answer:**
    ```python
    # Using sum formula
    def find_missing_v1(lst):
        n = len(lst) + 1
        expected_sum = n * (n + 1) // 2
        return expected_sum - sum(lst)
    
    # Using XOR (bit manipulation)
    def find_missing_v2(lst):
        xor_all = 0
        for i in range(1, len(lst) + 2):
            xor_all ^= i
        for num in lst:
            xor_all ^= num
        return xor_all
    
    # Using set
    def find_missing_v3(lst):
        return set(range(1, len(lst) + 2)) - set(lst)
    
    print(find_missing_v1([1, 2, 4, 5]))  # 3
    ```
    
    **Time Complexity:** O(n)
    **Space Complexity:** O(1) for sum approach, O(n) for set

### Intermediate to Advanced Level

41. **Implement a function that returns the longest substring without repeating characters.**
    
    **Answer:**
    ```python
    def longest_substring(s):
        char_index = {}
        max_length = 0
        start = 0
        
        for i, char in enumerate(s):
            if char in char_index:
                # Move start to avoid repeating char
                start = max(start, char_index[char] + 1)
            char_index[char] = i
            max_length = max(max_length, i - start + 1)
        
        return max_length
    
    # Return the actual substring
    def longest_substring_str(s):
        char_index = {}
        max_length = 0
        start = 0
        best_start = 0
        
        for i, char in enumerate(s):
            if char in char_index:
                start = max(start, char_index[char] + 1)
            char_index[char] = i
            if i - start + 1 > max_length:
                max_length = i - start + 1
                best_start = start
        
        return s[best_start:best_start + max_length]
    
    print(longest_substring("abcabcbb"))    # 3
    print(longest_substring_str("abcabcbb")) # "abc"
    ```
    
    **Time Complexity:** O(n)
    **Space Complexity:** O(min(n, m)) where m is charset size

42. **Write a decorator that caches function results (memoization).**
    
    **Answer:**
    ```python
    # Simple decorator
    def cache(func):
        cached = {}
        def wrapper(*args):
            if args in cached:
                return cached[args]
            result = func(*args)
            cached[args] = result
            return result
        return wrapper
    
    # With functools.wraps
    from functools import wraps
    def cache_v2(func):
        cached = {}
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cached:
                return cached[key]
            result = func(*args, **kwargs)
            cached[key] = result
            return result
        return wrapper
    
    # Using functools.lru_cache
    from functools import lru_cache
    @lru_cache(maxsize=128)
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)
    
    @cache
    def expensive_function(n):
        print(f"Computing {n}")
        return n ** 2
    
    print(expensive_function(5))  # Computing 5, prints 25
    print(expensive_function(5))  # prints 25 (cached)
    ```

43. **Implement a function that groups anagrams together.**
    
    **Answer:**
    ```python
    def group_anagrams(words):
        anagrams = {}
        for word in words:
            key = "".join(sorted(word))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        return list(anagrams.values())
    
    # Using defaultdict
    from collections import defaultdict
    def group_anagrams_v2(words):
        anagrams = defaultdict(list)
        for word in words:
            key = tuple(sorted(word))
            anagrams[key].append(word)
        return list(anagrams.values())
    
    print(group_anagrams(["eat", "tea", "ate", "bat", "tab"]))
    # [["eat", "tea", "ate"], ["bat", "tab"]]
    ```
    
    **Time Complexity:** O(n * k log k) where k is max word length
    **Space Complexity:** O(n * k)

44. **Write a function that finds if a string is a valid parentheses combination.**
    
    **Answer:**
    ```python
    def is_valid_parentheses(s):
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack or pairs[stack.pop()] != char:
                    return False
        return len(stack) == 0
    
    # Alternative approach
    def is_valid_parentheses_v2(s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
    
    print(is_valid_parentheses("()[]{}"))       # True
    print(is_valid_parentheses("([{}])"))       # True
    print(is_valid_parentheses("([)]"))         # False
    ```
    
    **Time Complexity:** O(n)
    **Space Complexity:** O(n)

45. **Implement a function that returns the longest palindromic substring.**
    
    **Answer:**
    ```python
    def longest_palindrome(s):
        if not s:
            return ""
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # Length
        
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            # Odd length palindromes
            len1 = expand_around_center(i, i)
            # Even length palindromes
            len2 = expand_around_center(i, i + 1)
            
            length = max(len1, len2)
            if length > max_len:
                max_len = length
                start = i - (length - 1) // 2
        
        return s[start:start + max_len]
    
    print(longest_palindrome("babad"))     # "bab" or "aba"
    print(longest_palindrome("cbbd"))      # "bb"
    ```
    
    **Time Complexity:** O(n²)
    **Space Complexity:** O(1)

46. **Write a generator that yields Fibonacci numbers.**
    
    **Answer:**
    ```python
    def fibonacci_generator(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    
    # Infinite generator
    def fibonacci_infinite():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    # Usage
    for num in fibonacci_generator(10):
        print(num)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    
    # With infinite generator
    gen = fibonacci_infinite()
    for _ in range(5):
        print(next(gen))  # 0, 1, 1, 2, 3
    ```

47. **Implement a simple LRU (Least Recently Used) cache.**
    
    **Answer:**
    ```python
    from collections import OrderedDict
    
    class LRUCache:
        def __init__(self, capacity):
            self.cache = OrderedDict()
            self.capacity = capacity
        
        def get(self, key):
            if key not in self.cache:
                return -1
            self.cache.move_to_end(key)
            return self.cache[key]
        
        def put(self, key, value):
            if key in self.cache:
                self.cache.move_to_end(key)
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
    
    # Using functools.lru_cache
    from functools import lru_cache
    @lru_cache(maxsize=128)
    def my_function(x):
        return x ** 2
    
    # Test
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))      # 1
    cache.put(3, 3)
    print(cache.get(2))      # -1 (evicted)
    ```
    
    **Time Complexity:** O(1) for get and put
    **Space Complexity:** O(capacity)

48. **Write a function that finds the intersection of two lists.**
    
    **Answer:**
    ```python
    # Using set intersection
    def intersection_v1(list1, list2):
        return list(set(list1) & set(list2))
    
    # Two-pointer (requires sorted)
    def intersection_v2(list1, list2):
        list1.sort()
        list2.sort()
        result = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] == list2[j]:
                if not result or result[-1] != list1[i]:
                    result.append(list1[i])
                i += 1
                j += 1
            elif list1[i] < list2[j]:
                i += 1
            else:
                j += 1
        return result
    
    # Using list comprehension with set
    def intersection_v3(list1, list2):
        set2 = set(list2)
        return [x for x in set(list1) if x in set2]
    
    print(intersection_v1([1, 2, 2, 1], [2, 2]))  # [2]
    ```
    
    **Time Complexity:** O(n + m)
    **Space Complexity:** O(min(n, m))

49. **Implement a function that checks if a linked list has a cycle.**
    
    **Answer:**
    ```python
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None
    
    # Floyd's cycle detection (tortoise and hare)
    def has_cycle(head):
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    # Find cycle start
    def find_cycle_start(head):
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    
    # Test
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Create cycle
    
    print(has_cycle(node1))  # True
    ```
    
    **Time Complexity:** O(n)
    **Space Complexity:** O(1)

50. **Write a function that returns all permutations of a string.**
    
    **Answer:**
    ```python
    from itertools import permutations
    
    # Using itertools (simplest)
    def get_permutations_v1(s):
        return ["".join(p) for p in permutations(s)]
    
    # Recursive backtracking
    def get_permutations_v2(s):
        if len(s) <= 1:
            return [s]
        
        perms = []
        for i, char in enumerate(s):
            remaining = s[:i] + s[i+1:]
            for perm in get_permutations_v2(remaining):
                perms.append(char + perm)
        return perms
    
    # With duplicates handling
    def get_permutations_v3(s):
        def backtrack(chars, current, result):
            if len(current) == len(chars):
                result.append("".join(current))
                return
            for i in range(len(chars)):
                if chars[i] not in current or current.count(chars[i]) < chars.count(chars[i]):
                    current.append(chars[i])
                    backtrack(chars, current, result)
                    current.pop()
        
        result = []
        backtrack(list(s), [], result)
        return result
    
    print(get_permutations_v1("ABC"))  # All 6 permutations
    ```
    
    **Time Complexity:** O(n!)
    **Space Complexity:** O(n!)

---

## Additional Tips for Interview Success

### Before the Interview
- Review data structures: lists, dictionaries, sets, queues, stacks
- Practice problem-solving with LeetCode or HackerRank
- Understand time and space complexity (Big O notation)
- Be ready to explain your thought process

### During the Interview
- Ask clarifying questions before coding
- Discuss edge cases and constraints
- Explain your approach before implementing
- Write clean, readable code with proper naming
- Test your code with examples
- Discuss time and space complexity trade-offs

### Key Topics to Master
- **Data Structures**: lists, tuples, dictionaries, sets, queues, stacks
- **Algorithms**: sorting, searching, recursion, dynamic programming, graphs
- **OOP**: inheritance, polymorphism, encapsulation, abstraction
- **Libraries**: collections, itertools, functools, datetime, os, sys
- **Testing**: unit tests with unittest or pytest
- **Performance**: profiling, optimization, caching

### Python-Specific Topics
- String manipulation and formatting
- File I/O operations
- Regular expressions
- Error handling and custom exceptions
- Multithreading and multiprocessing
- SQL and database connections
- REST APIs and web frameworks (Flask, Django)
- Package management (pip, conda)

Good luck with your interview preparation!
