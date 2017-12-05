pyramid_csrf_multi_scheme
=========================

This script enables two separate cookie tokens on each request, bound to the scheme: a SECURE HTTPS only cookie and a mixed-use insecure http token (that is also available on https).

If the current scheme is HTTPS:
	only the SECURE HTTPS token will be considered
	HOWEVER calls to generate a new token will reset both the SECURE HTTPS and the insecure http tokens.

If the current scheme is insecure http:
	the SECURE HTTPS tokens are ignored as they are not even available, and only the insecure http token is considered.

Why?
----

If an app supports both HTTP and HTTPS endpoints in parts, there is a desire to shield the SECURE HTTPS token from the insecure http traffic.


License
-------

Most of this is just code lightly edited from Pyramid, and therefore available under Pyramid's licensing terms.
