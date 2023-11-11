=========
isometric
=========

Overview
--------

Geometry on an isometric grid. 

Installation
------------

To install isometric, you can use `pip`. Open your terminal and run:

.. code-block:: bash

    pip install isometric

Usage
-----

.. code-block:: python
    
    from isometric import Displacement
    d = Displacement.by_axis(
        by_axis_0 = 2,
        by_axis_1 = -3,
        by_axis_2 = 7,
    )
    print(d) # Displacement(by_axis_0_and_1=IntPair(p=-5, q=4), by_axis_1_and_2=IntPair(p=-1, q=5), by_axis_2_and_0=IntPair(p=4, q=-1))
    print(d.by_axis_1_and_2) # IntPair(p=-1, q=5)
    print(d.x()) # 3.4641016151377544
    print(d.y()) # -3.0

Axis 0 points towards 12 o'clock i.e. in the same direction as the y-axis.
Axis 1 points towards 10 o'clock.
Axis 2 points towards 8 o'clock.
As the grid is two-dimensional the Displacement-object can be fully expressed with only two axis.

License
-------

This project is licensed under the MIT License.

Credits
-------
- Author: Johannes Programming
- Email: johannes-programming@posteo.org

Thank you for using isometric!