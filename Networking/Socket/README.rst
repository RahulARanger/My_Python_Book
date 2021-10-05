==================
Socket Programming
==================

I personally wanted to learn socket Programming for IPC [1]_.
Scripts are of form *server_number.py* and its corresponding client *client_number.py*.

Work Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: sockets-tcp-flow.webp
    :alt: Work Flow

Scripts
~~~~~~~

1. using the basic low level socket_ library, it introduces us to basics
2. then we can use the normal TCP server using socket_ module. But we can it's only for small scale ipc
3. using `Listener and Clients from Multiprocessing`_, it's easy to send variable length messages

References
~~~~~~~~~~~

* GitBook_

.. _GitBook: https://www.gitbook.com/book/erlerobotics/erle-robotics-python-gitbook-free
.. _socket: https://docs.python.org/3/library/socket.html
.. _`Listener and Clients from Multiprocessing`: https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.connection

.. [1] Inter-Process Communication