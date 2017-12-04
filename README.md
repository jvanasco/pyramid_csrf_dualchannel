pyramid_csrf_dualchannel
=================

This script enables two separate cookie tokens on each request: a https only and a mixed-use https/http token.

If the current scheme is https, only the https token will be valid HOWEVER Calls to generate new tokens will reset both http and https tokens.
If the current scheme is http, the https tokens are ignored.

Why?
----

If an app supports both HTTP and HTTPS endpoints in parts, there is a desire to shield the https token from http traffic.


License
-------

Most of this is just code lightly edited from Pyramid, and therefore available under Pyramid's licensing terms.