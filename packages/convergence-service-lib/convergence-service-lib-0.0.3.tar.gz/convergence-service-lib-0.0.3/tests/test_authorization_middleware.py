import asyncio
import encodings.utf_8
import json
from unittest import TestCase
from mock.mock import Mock, patch, MagicMock

from convergence.convergence_service import ConvergenceEndpointInfo
from convergence.helpers import errors
from convergence.security.access_control_layer import AccessControlLayer
from convergence.security.authorization_filter import AuthorizationMiddleware
from .test_acl import issue_dummy_jwt

TEST_EC_KEY = """
-----BEGIN EC PRIVATE KEY-----
MIHcAgEBBEIBmacvo4lGyiT8FHveUi1KTgqyR+JvXyPkjzR1eqIcGx0bRmtxH3Wf
SQO6U3Jdj9l6O+m1KrzQV/KQR8fZqUHfWACgBwYFK4EEACOhgYkDgYYABAD9zwbl
fm14AWpLNObBT9CPcxxc+HBcQHn0JsC05KX1tAsXuKSASV2JNORWVvk7v+qD8ib1
oI76kSesAnAjXiZJ8wH5pKOmVOMFRgEDJsD/3f546eE6Yig0TzjVbtioFT6i/gRR
svTzwet8Sx6NYLt4h2rdzgrnreJq9lGK5zego4VUyA==
-----END EC PRIVATE KEY-----
""".strip()


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


class TestAuthorizationMiddleware(TestCase):
    def test_invalid_authorization_header_no_jwt(self):
        ep_authorization_rule = '@acl.allow_all()'
        expect_next_call = False

        headers = {
            'Authorization': 'Bearer something_invalid'
        }

        response = self.call_request_on_filter(ep_authorization_rule, expect_next_call, headers)
        self.assert_failure(response, errors.INVALID_AUTHORIZATION_TOKEN, 401)

    def test_invalid_authorization_header_invalid_jwt(self):
        ep_authorization_rule = '@acl.allow_all()'
        expect_next_call = False

        headers = {
            'Authorization': 'Bearer ey.uy.io'
        }

        response = self.call_request_on_filter(ep_authorization_rule, expect_next_call, headers)
        self.assert_failure(response, errors.INVALID_AUTHORIZATION_TOKEN, 401)

    def test_no_authorization_rule(self):
        ep_authorization_rule = '@acl.allow_all()'
        expect_next_call = True

        self.call_request_on_filter(ep_authorization_rule, expect_next_call, {})

    def test_no_authorization_rule_with_valid_jwt(self):
        ep_authorization_rule = '@acl.allow_all()'
        expect_next_call = True

        headers = {
            'Authorization': f'Bearer {issue_dummy_jwt()}'
        }

        self.call_request_on_filter(ep_authorization_rule, expect_next_call, headers)

    def test_authorization_failure(self):
        ep_authorization_rule = '@acl.has_authority("authority::dummy_authority")'
        expect_next_call = False

        headers = {
            'Authorization': f'Bearer {issue_dummy_jwt(authorities="dummy_another_authority")}'
        }

        response = self.call_request_on_filter(ep_authorization_rule, expect_next_call, headers)
        self.assert_failure(response, errors.INVALID_AUTHORIZATION_TOKEN, 403)

    def call_request_on_filter(self, ep_authorization_rule, expect_next_call, headers):
        app = Mock()
        service = Mock()
        request = Mock()
        next_call = AsyncMock()
        sut = AuthorizationMiddleware(app=app, service=service)  # noqa
        sut.signing_key = TEST_EC_KEY

        ep_info = ConvergenceEndpointInfo('', '', ep_authorization_rule, ep_authorization_rule is None)
        with patch.object(service, 'get_endpoint_info') as pathed_ep, \
                patch.object(service, 'acl', AccessControlLayer()), \
                patch.object(request, 'headers', headers), \
                patch.object(request, 'scope', {'path': '/api/endpoint', 'method': 'GET'}):
            pathed_ep.return_value = ep_info

            response = asyncio.run(sut.dispatch(request, next_call))  # noqa
            self.assertEqual(next_call.called, 1 if expect_next_call else 0)

            return response

    def assert_failure(self, response, expected_error_code, expected_status_code):
        content = encodings.utf_8.decode(response.body)[0]
        obj = json.loads(content)

        error_code = obj['header']['code']
        status_code = obj['header']['status_code']
        self.assertEqual(expected_error_code, error_code)
        self.assertEqual(expected_status_code, status_code)
