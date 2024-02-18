# Project-1-Point

Using unittest to implement a point class and pass the established test cases. 

## Assignment:

- Similar to the last assignment the workflow is as usual:
    1. Before you edit any file, carefully read the comments inside each file.
    2. Test your program locally; revise and re-test as needed. 
    3. Commit and push your changes to your own repository.
    4. The `credentials.ini` file is not provided, but you have to create one yourself and submit it to
       [Blackboard](https://lms.qu.edu.sa/) as we have seen in project-0.

- Create a file named `point.py`. Create class Point, with a constructor (initializer) method that takes two integers,
  `x` and `y`, and stores them as instance variables `self.x` and `self.y`. Please note that the file name and the
  class name are case-sensitive. When you have completed this step, test case `test_initializing_a_point` should pass.
- Add a method `move` that takes two integer arguments, `dx` and `dy`. This method should increase `self.x` by `dx` and
  increase `self.y` by `dy`. (If `dx` or `dy` are negative, the result will be decreasing `self.x` and/or `self.y`).
  When you have completed this step, the test case `test_moving_a_point` should pass.
- Create a method with the special name `__eq__` which takes, in addition to `self`, another point object.
  This method should return a boolean. If the `x` and `y` fields of the `self` object and the other `Point` object are
  equal, `__eq__` should return `True`, otherwise, it should return `False`.
  When you have completed this step, both test cases `test_points_equality` and `test_points_inequality` should pass.
- At this stage, you have defined `Point` objects that can be created, moved, and compared for equality. But if you
  print a `Point` object, you will get a fairly unfriendly representation like `<point.Point object at 0x10b8aabe0>`.
  Test case `test_point_str` expects the string representation of a `Point` object with `x` component `10` and `y`
  component `12` to look like `(10, 12)`. To accomplish this, you will define another special method called `__str__`.
  The `__str__` method takes only the `self` object as an argument, and it returns the preferred string representation
  of that object.
- When you have completed these steps, all the test cases should pass. Note that this is not an ironclad guarantee
  that your code is correct. We will use a few more tests, which we do not share with you, in grading.
  Our extra tests help ensure that you are really solving the problem and not taking shortcuts that provide correct
  results only for the known tests.
- In addition to passing all test cases, you should also adhere to our coding style principles. You should always refer
  to the coding style cheat sheet. However, one of the most essential representations we agreed on is to give the hints
  types. For example, when we say a `self` method `foo` should take two integers `x` and `y`, and return a string.
  The expected method signature should look like this `def foo(self, x: int, y: int) -> str:`.
  As always, when in doubt, check the [PEP8](https://peps.python.org/pep-0008/) instructions.
  To double-check your work use the following two commands.
    - `pylint --attr-naming-style any --argument-naming-style any <file_name.py>`
    - `flake8 --select="ANN001,ANN201,ANN202,ANN203,ANN204,ANN205,ANN206" --suppress-none-returning <file_name.py>`

## Reminders

- The `credentials.ini` file MUST include your full information. And must be named correctly.
- DO NOT push any changes to your repo after the deadline. When we clone
  your repo given the key, we will check when was the last update on your
  repository. If you made any changes passed the deadline you will immediately 
  get 20% deducted.

## Grading Rubric

- **[70 Points]** For passing all OUR tests. As stated in the assignment instructions, we will have our own additional
  test cases that test the same core functionalities but make sure you're not taking any shortcuts. Passing all of them
  guarantees you will get 70 points.
- **[20 Points]** For following the given coding style as given in the cheat sheet and PEP8.
- **[10 Points]** For submitting a correct `credentials.ini` file to Blackboard. Please note that these are not core
  tasks related to the assignment, but we give an easy 10 points for the effort.

# All Rights Reserved

This is the work of Ziyad Alsaeed. Any copy or distribution of this
repository or a fork of it in a way other than the instruction provided
above will subject you to legal proceedings.