from datetime import datetime, timezone, timedelta
from unittest import TestCase

import jwt

from convergence.security.access_control_layer import AccessControlLayer

dummy_signing_key = """
-----BEGIN EC PRIVATE KEY-----
MIHcAgEBBEIBmacvo4lGyiT8FHveUi1KTgqyR+JvXyPkjzR1eqIcGx0bRmtxH3Wf
SQO6U3Jdj9l6O+m1KrzQV/KQR8fZqUHfWACgBwYFK4EEACOhgYkDgYYABAD9zwbl
fm14AWpLNObBT9CPcxxc+HBcQHn0JsC05KX1tAsXuKSASV2JNORWVvk7v+qD8ib1
oI76kSesAnAjXiZJ8wH5pKOmVOMFRgEDJsD/3f546eE6Yig0TzjVbtioFT6i/gRR
svTzwet8Sx6NYLt4h2rdzgrnreJq9lGK5zego4VUyA==
-----END EC PRIVATE KEY-----
""".strip()


def issue_dummy_jwt(authorities=None, is_service_jwt=False, return_payload=False):
    authorities = [] if authorities is None else authorities
    authorities = [authorities] if not isinstance(authorities, list) else authorities

    payload = {
        "sub": 'jwt_subject',
        "iss": 'jwt_issuer',
        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=1),
        "authorities": authorities
    }

    if is_service_jwt:
        payload["is_inter_service_call"] = True

    encoded_jwt = jwt.encode(payload, dummy_signing_key, algorithm="ES512")
    if not return_payload:
        return encoded_jwt
    else:
        return encoded_jwt, payload


class MockRequest:
    def __init__(self):
        self.headers = {}


class TestAccessControlLayer(TestCase):
    def test_allow_all(self):
        request = MockRequest()
        acl = AccessControlLayer()

        self.assertTrue(acl.is_authorized('@acl.allow_all()', request, None))  # noqa
        self.assertTrue(acl.is_authorized('@acl.allow_all()', request, {}))  # noqa
        self.assertFalse(acl.is_authorized('@acl.allow_all() and @false', request, {}))  # noqa

    def test_user_is_not_signed_in(self):
        acl = AccessControlLayer()

        request = MockRequest()
        jwt = issue_dummy_jwt()
        request.headers['Authorization'] = f'Bearer {jwt}'
        self.assertFalse(acl.is_authorized('@acl.not_signed_in()', request, {}))  # noqa
        self.assertTrue(acl.is_authorized('@acl.not_signed_in()', request, None))  # noqa

    def test_user_is_signed_in(self):
        acl = AccessControlLayer()

        request = MockRequest()
        jwt = issue_dummy_jwt()
        request.headers['Authorization'] = f'Bearer {jwt}'
        self.assertTrue(acl.is_authorized('@acl.is_signed_in()', request, {}))  # noqa
        self.assertFalse(acl.is_authorized('@acl.is_signed_in()', request, None))  # noqa

    def test_user_has_authority(self):
        acl = AccessControlLayer()

        request = MockRequest()
        jwt, token = issue_dummy_jwt(authorities='authority::dummy_authority', return_payload=True)
        request.headers['Authorization'] = f'Bearer {jwt}'
        self.assertTrue(acl.is_authorized('@acl.has_authority("authority::dummy_authority")', request, token))  # noqa
        self.assertTrue(acl.is_authorized("@acl.has_authority('authority::dummy_authority')", request, token))  # noqa
        self.assertFalse(acl.is_authorized('@acl.has_authority("authority::another_dummy_authority")', request, token))  # noqa
