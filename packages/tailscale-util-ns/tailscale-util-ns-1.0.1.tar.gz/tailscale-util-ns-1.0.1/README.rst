tailscale-util-ns
=================

|PyPI version| |Downloads| |MIT license| |tailscale|

This is a tailscale plugin for getting IP Address of specific device.

Installation
------------

::

   pip install tailscale-util-ns

Usage
-----

How to get auth url to login?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

       from tailscale_ns.tailscale_device_ip import TailScaleDeviceIp

       if TailScaleDeviceIp.needs_login():
           TailScaleDeviceIp.log('Login using web browser with URL: ' + TailScaleDeviceIp.auth_url())

How to up Tailscale?
~~~~~~~~~~~~~~~~~~~~

.. code:: python

       from tailscale_ns.tailscale_device_ip import TailScaleDeviceIp

       TailScaleDeviceIp.prepare()

How to get IP Address of device?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

       from tailscale_ns.tailscale_device_ip import TailScaleDeviceIp

       print(TailScaleDeviceIp.get_ip_for_device(device_name='device name'))

Author
------

Nishith Shah - `github <https://github.com/nishithcitc>`__

License
-------

This project is licensed under the `MIT license </LICENSE>`__.

.. |PyPI version| image:: https://badge.fury.io/py/tailscale-util-ns.svg
   :target: https://badge.fury.io/py/tailscale-util-ns
.. |Downloads| image:: https://pepy.tech/badge/tailscale-util-ns
   :target: https://pepy.tech/project/tailscale-util-ns
.. |MIT license| image:: http://img.shields.io/badge/license-MIT-brightgreen.svg
   :target: /LICENSE
.. |tailscale| image:: https://img.shields.io/badge/tailscale-%3E%3D0.2.0-blue.svg
   :target: https://img.shields.io/badge/tailscale-%3E%3D0.2.0-blue.svg
