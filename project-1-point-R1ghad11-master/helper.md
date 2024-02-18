# How to Run the Test Cases

## Using Command Line

Opening the project as it is then typing the following command

```bash
python3 tesr_point.py
```

The result should be something like

```bash
Traceback (most recent call last):
  File "/Users/zalsaeed/Documents/qu/315/lab/project1-point/test_point.py", line 20, in <module>
    import point
ModuleNotFoundError: No module named 'point'
```

What you see above is python telling you that you don't have a file called `point.py`.
If you create the file named `point.py`, then run the same command again, you will get something like the following.

```bash
EEEEE
======================================================================
ERROR: test_initializing_a_point (__main__.TestPoint)
This test should pass when you have defined the
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zalsaeed/Documents/qu/315/lab/project1-point/test_point.py", line 30, in test_initializing_a_point
    pt = point.Point(42,89)
AttributeError: module 'point' has no attribute 'Point'

======================================================================
ERROR: test_moveing_a_point (__main__.TestPoint)
The 'move' method modifies the coordinates of a
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zalsaeed/Documents/qu/315/lab/project1-point/test_point.py", line 39, in test_moveing_a_point
    pt = point.Point(13,22)
AttributeError: module 'point' has no attribute 'Point'

======================================================================
ERROR: test_point_str (__main__.TestPoint)
A point should have a nice string representation
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zalsaeed/Documents/qu/315/lab/project1-point/test_point.py", line 69, in test_point_str
    pt = point.Point(18, 34)
AttributeError: module 'point' has no attribute 'Point'

======================================================================
ERROR: test_points_equality (__main__.TestPoint)
The __eq__ method of Point should equate
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zalsaeed/Documents/qu/315/lab/project1-point/test_point.py", line 49, in test_points_equality
    p1 = point.Point(7, 12)
AttributeError: module 'point' has no attribute 'Point'

======================================================================
ERROR: test_points_inequality (__main__.TestPoint)
Similarly __eq__ method of Point should return False
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zalsaeed/Documents/qu/315/lab/project1-point/test_point.py", line 58, in test_points_inequality
    p1 = point.Point(9,13)
AttributeError: module 'point' has no attribute 'Point'

----------------------------------------------------------------------
Ran 5 tests in 0.000s

FAILED (errors=5)
```

the code above finds that you have a file called `point.py` now, but it cannot find any implemented method or even a class called `Point`.

Now you should start implementing the method in the `point.py` file one by one and running the code after you implement each method. What you will observe (if you do it right) is that the number of failing test cases gets lower each time you implement a request correctly. 

The final result of running the command if you implement all the methods correctly should be something like the following:


```bash
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```


## Using PyCharm

Run the `test_point.py` anyway you want (e.g., From the top menu select Run >> Run ... >> test_point.py). The result you will get in the console of PyCharm should be identical to the one you see in the terminal. For example, 

```bash
Traceback (most recent call last):
  File "/Users/zalsaeed/Documents/qu/315/lab/project1-point/test_point.py", line 20, in <module>
    import point
ModuleNotFoundError: No module named 'point'
```

Now, right-click on the project name and select "New >> Python File". Then give the new file the name `point`. You should see a new file created on your project structure. If you run the `test_point.py` again, you will also see the same message we have seen before.

```bash
EEEEE
======================================================================
ERROR: test_initializing_a_point (__main__.TestPoint)
This test should pass when you have defined the
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zalsaeed/Documents/qu/315/lab/project1-point/test_point.py", line 30, in test_initializing_a_point
    pt = point.Point(42,89)
AttributeError: module 'point' has no attribute 'Point'

======================================================================
ERROR: test_moveing_a_point (__main__.TestPoint)
The 'move' method modifies the coordinates of a
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zalsaeed/Documents/qu/315/lab/project1-point/test_point.py", line 39, in test_moveing_a_point
    pt = point.Point(13,22)
AttributeError: module 'point' has no attribute 'Point'

======================================================================
ERROR: test_point_str (__main__.TestPoint)
A point should have a nice string representation
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zalsaeed/Documents/qu/315/lab/project1-point/test_point.py", line 69, in test_point_str
    pt = point.Point(18, 34)
AttributeError: module 'point' has no attribute 'Point'

======================================================================
ERROR: test_points_equality (__main__.TestPoint)
The __eq__ method of Point should equate
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zalsaeed/Documents/qu/315/lab/project1-point/test_point.py", line 49, in test_points_equality
    p1 = point.Point(7, 12)
AttributeError: module 'point' has no attribute 'Point'

======================================================================
ERROR: test_points_inequality (__main__.TestPoint)
Similarly __eq__ method of Point should return False
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/zalsaeed/Documents/qu/315/lab/project1-point/test_point.py", line 58, in test_points_inequality
    p1 = point.Point(9,13)
AttributeError: module 'point' has no attribute 'Point'

----------------------------------------------------------------------
Ran 5 tests in 0.000s

FAILED (errors=5)
```

the code above finds that you have a file called `point.py` now, but it cannot find any implemented method or even a class called `Point`.

Now you should start implementing the method in the `point.py` file one by one and running the `test_point.py` code after you implement each method. What you will observe (if you do it right) is that the number of failing test cases gets lower each time you implement a request correctly. 

The final result of running the command if you implement all the methods correctly should be something like the following:

```bash
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```
