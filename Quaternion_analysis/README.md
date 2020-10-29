# Transcribing Complex Analysis Lecture Notes to Quaternions

Big effort to _quickly_ transform notes to quaternion form as it will force me
to learn it better. Done in Jupyter notebooks so code can be run.

In some ways, this should look like a trivial and uninteresting exercise. The
following changes are made consistently:

x -> t
y i -> R I

The impact is in the _physical_ interpretation. The real number t _is_ time.
The three imaginaries in R I _is_ a 3-vector in space.

The amount of work needed to be done for the math, the physics, and the
programming for analytic animations is too large a mountain to think about.
Consider the work here baby steps, but steps none-the-less.

## Python Library

Created by D. Sweetser. There are 2 classes: Q for the quaternion algebra that
Hamilton would have recognized, and Qs for quaternion series, required to
create a Hilbert vector space of quaternions.

To test, run:

pytest -v --disable-warnings test_Qs.py
