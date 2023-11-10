# Eqsolve 
- A mathematical Python package by Zakkai Thomas

## [**Continuation (eqsolvcarlover101 - Deprecated)**](https://pypi.org/project/eqsolvcarlover101)

[![Downloads](https://static.pepy.tech/personalized-badge/eqsolvcarlover101?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Total%20Downloads)](https://pepy.tech/project/eqsolvcarlover101) [![Latest Version](https://img.shields.io/pypi/v/eqsolvcarlover101?label=Latest%20Version)](https://pypi.org/project/eqsolvcarlover101/) ![License](https://img.shields.io/badge/License-BSD-lightgray?label=License)

- [**Website**](https://github.com/Carlover101/equation-solver)
- [**Bug Reports**](https://github.com/Carlover101/equation-solver/issues)
- [**Email**](mailto:zmanmustang2017@gmail.com)
- [**PyPI Page**](https://pypi.org/project/eqsolvcarlover101)
- [**Documentation**](https://carlover101.github.io/equation-solver)


This is a project that solves mathematic equations for you!


# How to Install:

1. Make sure you have Python installed by typing `python3` in the command prompt.
   > If not, go to [python.org](https://python.org) to get the latest release.

2. Enter `pip install eqsolve`.

3. Use `import eqsolve` in your code to begin using the package.

#


## Functions:

1. Quadratic
    - ***eqsolve.quadsolve(eq)***
      > To type a square in python, you need to use a carrot **^** or two astrix **. (Ex. 2x^2 -5x +4)

2. Slope Intercept
    - ***eqsolve.slopeint(x1, y1, x2, y2)***
      > Put in two points, and output an equation in slope-intercept form.

3. Midpoint
    - _**eqsolve.midpoint(x1, y1, x2, y2)**_
      > Put in two points and output the midpoint.

4. Perpendicular Lines
    - ***eqsolve.perpint(eq, intsec)***
      > Put in the slope of a line, and the intersection point, and get the slope-intercept equation of the perpendicular line.

5. Similar Shapes Check
    - ***eqsolve.issim(shape1, shape2)***
      > Takes the lengths of the sides of one shape and the corresponding side lengths of the sides of a second shape.
      > If the shapes are similar, it will return the scale factor.

6. Missing Right Triangle Lengths
   - ***eqsolve.findright(missing, s1, s2)***
     > Finds the missing length of a right triangle.

7. Compounding Intersest
   - ***eqsolve.intcompound(p, r, n, t)***
     > Calculates the amount of money present/money owed after a number of years using the provided interest rate and the number of times it is compounded yearly.

8. Continuously Compounding Interest
   - ***eqsolve.contcompound(p, r, t)***
     > Calculates the amount of money present/money owed after a number of years if the interest provided is compounded continuously.

### Other Commands:

1. Command List
    - ***eqsolve.commands()***

2. Help
    - ***eqsolve.help()***





## Version Info:

### Deprecated:

- V0 - V1.5.2:
    - To use these older versions, go to **Helpful Info** down below.

### Current:

- V1.0.0:
    - Added _**eqsolve.intcompound(p,r,n,t)**_ and _**eqsolve.contcompound(p,r,t)**_ functions.
    - Updated all function descriptions so they work with python's default ***help(...)*** function.
    - Updated all functions to move away from ***input()*** towards proper function notation.
    - Updated **README.md** so it reflects current statistics and project version info.

- V1.0.1:
    - Fixed some errors with the ***README.md*** file.

## Helpful Info:

- For previous versions and version error info, refer to [github (ver: oldest - current)](https://github.com/Carlover101/equation-solver) or [old pypi (ver: oldest - 1.5.1.0)](https://pypi.org/project/eqsolvcarlover101).

## Thanks for using my work!
