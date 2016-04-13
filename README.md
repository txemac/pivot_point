# Pivot point

Suppose you have an array with integer values, e.g. [1, 3, 2, ­2, 2, 4]. You can trust the numbers are small enough that integer overflow issues will not come up (although negative numbers may be included).

A pivot point is an index in the array such that the two sides are "balanced": i.e. that all the values before the pivot point add up to the same as the ones after.

In our example, the first value 2 (index 2) is a pivot point because 1 + 3 = ­2 + 2 + 4. The second value 2 (index 4) is also a pivot point because 1 + 3 + 2 + ­2 = 4.

This function returns the index of all pivot points. In the above example [2, 4]. If there is no pivot point, return ­1.

This should work for any array passed to the function, although again you can assume it’s small enough to not deal with overflow issues.

# Run
To run unit test suite, install 'nose', eg. using 'pip': 

    pip install -r ./requirements.txt
    
Run tests:

    nosetests -v

# Author
Jose Bermudez

[www.josebermudez.co.uk](http://www.josebermudez.co.uk)

[info@josebermudez.co.uk](mailto: info@josebermudez.co.uk)