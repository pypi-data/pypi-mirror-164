.. module: lymph

.. _lymph:

Detailed API
============

The human lymph system (or rather parts of it) are modelled as directed graphs here. Hence, a :class:`System` consists of multiple :class:`Node` and :class:`Edge` instances, which are represented by a python class each.

Recently, we added the convenience class :class:`BilateralSystem` that automatically creates a symmetric graph for the ipsilateral and contralateral network. It also allows to fix sperad parameters to be set symmetrically.

Lymph system
------------

.. autoclass:: lymph.Unilateral
   :members:

Bilateral lymph system
----------------------

.. autoclass:: lymph.Bilateral
   :members:

Bilateral lymphatic system with midline extension
-------------------------------------------------

.. autoclass:: lymph.MidlineBilateral
    :members:

Edge
----

Represents a lymphatic drainage pathway and therefore are spread probability. It is represented by the simplest possible class suitable for the task.

.. autoclass:: lymph.Edge
   :members:

Node
----

Represents a lymph node level (LNL) or rather a random variable associated with it. It encodes the microscopic involvement of the LNL and - if involved - might spread along outgoing edges.

The probability for a healthy node to become involved is - for performance purposes - not computed by a method of the :class:`Node` class, but rather in a cached function outside:

.. autofunction:: lymph.node_trans_prob

.. autoclass:: lymph.Node
   :members:

Utils
-----

We provide some additional utility functions and classes that aren't necessary for the inference or risk estimation per se, but make life just a little bit easier.

Especially for reproducability of inference rounds there are some neat functions that interact with the HDF5 file format that allows to store quite some metadata. Head over to :doc:`this tutorial <sampling>` to get an idea of how this could be helpful.

.. autofunction:: lymph.utils.lyprox_to_lymph

.. autoclass:: lymph.utils.EnsembleSampler
    :members:

.. autoclass:: lymph.utils.HDF5Mixin
    :members:

.. autofunction:: lymph.utils.system_from_hdf5

.. autofunction:: lymph.utils.fast_binomial_pmf

.. autofunction:: lymph.utils.change_base

.. autofunction:: lymph.utils.comp_state_dist

.. autofunction:: lymph.utils.draw_diagnose_times

.. autofunction:: lymph.utils.draw_from_simplex