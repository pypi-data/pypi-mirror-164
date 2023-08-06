tweetlimiter
=================================

Package to estimate the rate of a message stream and to limit the number of
message.

Quickstart
==========

Install the package using pip

.. code-block:: console

   $ pip install tweetlimiter


Usage:

.. code-block:: python

    import tweetlimiter as tl

    limiter = tl.Limiter(target=1, damp_rate=0.1)

    for msg in stream():  # loop over messages
        decision = limiter.filter(msg.time, msg.followers)
        if decision:
            pass  # process

Links
=====

 * `GitLab Repository <https://gitlab.sauerburger.com/frank/tweetlimiter>`_
 * `tweetlimiter on PyPi <https://pypi.org/project/tweetlimiter>`_
