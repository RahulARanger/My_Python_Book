====================
Asynchronous Process
====================

Process is said to be asynchronous, if it can execute efficiently that is  without wasting any time given a chance.

Refer this nice `analogy <https://realpython.com/async-io-python/#async-io-explained>`_.

.. contents::

Awaitables
-----------

A function that can pause itself is known as awaitables.
It must have ``await``.

Types
~~~~~

* Coroutines
* Tasks
* Futures

Coroutines
----------

They are function capable of interacting with the event loop by pausing/ resuming its state.

Rules
~~~~~

* **For pausing its state, it needs ``await``**
* **For ending it needs return or by default, it ends at the end of function**
* **For starting it needs event loop to start as a task**

.. warning:: A function calling a Coroutine is also a Coroutine.
.. Note:: Coroutine can exist without ``await``

*How is it different from normal function?*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normal functions can't interact with the event loops. But coroutines can.


Asynchronous Generator function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
use this as less as possible, since this was possible recently.
:pep: `525`

Chaining
~~~~~~~~
we can chain coroutines by another function. But that function or object should also be a coroutine.

Tasks
-----

Tasks are items in TO-DO list in event loop.
There are created using the ``gather`` or ``create_task``.

Await
-----

``await`` tells the interpreter to return the control to the event loop. and the event loop selects the free task.

``asyncio.Queue``
-----------------

it's ``join``, ``put``, ``get`` methods are coroutine. Other than this it's same as ``queue.Queue``

Event Loop
----------

Event Loop is somethings like;

.. code:: python

    while True:
        ... # runs tasks

We can use Default Loop is like;

.. code:: python

    import asyncio

    async def sample():
        ...

    asyncio.run(sample())

**In a single Thread, we can have only one running event loop.**

Reference
----------

* `Coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutines>`_
* `What's Coroutine`_

More Reference
---------------
* Basics_

.. _`What's Coroutine`: https://youtu.be/GSiZkP7cI80
.. _Basics : https://youtu.be/iG6fr81xHKA
