import jwt
from jwt import DecodeError
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from starlette.responses import JSONResponse

from convergence.dto.base_dto import ApiResponse
from convergence.helpers import errors
from convergence.helpers.controller_helpers import convert_object_to_dict


class AuthorizationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, **kwargs):
        super().__init__(app)
        self.service = kwargs['service']
        self.signing_key = self.service.get_configuration('security.authentication.secret')
        self.signing_key = self.signing_key.replace('\\n', '\n')

    async def dispatch(self, request: Request, call_next):
        auth_header = request.headers.get('Authorization')

        payload = None
        if auth_header is not None:
            err_code, message, payload = self.__is_valid_authorization_token(auth_header)
            if err_code is not None:
                return self.__invalid_authorization_header(err_code, message)

        path = request.scope.get('path')
        method = request.scope.get('method')
        endpoint_info = self.service.get_endpoint_info(path, method)

        if endpoint_info is None:
            response = self.__not_found_response(path)
        elif endpoint_info.authorization is None or self.is_authorized(endpoint_info, request, payload):
            response = await call_next(request)
        else:
            response = self.__unauthorized_response(path)

        return response

    def is_authorized(self, endpoint_info, request, token_payload):
        acl = self.service.acl
        return acl.is_authorized(endpoint_info.authorization, request, token_payload)

    def __is_valid_authorization_token(self, auth_header):
        err_code = None
        err_message = None

        bearer_length = len('Bearer ')
        if auth_header[0:bearer_length] != 'Bearer ':
            err_code = errors.INVALID_AUTHORIZATION_TOKEN
            err_message = 'Service expects an authorization token in Bearer format.'
            return err_code, err_message, None

        try:
            auth_header = auth_header[bearer_length:]
            result = jwt.decode(auth_header, key=self.signing_key, algorithms="ES512")
            return None, None, result
        except DecodeError as ex:  # noqa
            err_code = errors.INVALID_AUTHORIZATION_TOKEN
            err_message = 'Service expects a valid JWT token.'

            return err_code, err_message, None

    def __invalid_authorization_header(self, err_code, message):
        status_code = 401

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = message
        response.header.code = err_code
        response.header.body_type = 'failure_info'

        response = convert_object_to_dict(response)

        return JSONResponse(response, status_code=status_code)

    def __unauthorized_response(self, path):
        status_code = 403

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = f'The authorization token is invalid for path {path}'
        response.header.code = errors.INVALID_AUTHORIZATION_TOKEN
        response.header.body_type = 'failure_info'

        response = convert_object_to_dict(response)

        return JSONResponse(response, status_code=status_code)

    def __not_found_response(self, path):
        status_code = 404

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = f'Unable to find resource at path {path}'
        response.header.code = errors.API_RESOURCE_NOT_FOUND
        response.header.body_type = 'failure_info'

        response = convert_object_to_dict(response)

        return JSONResponse(response, status_code=status_code)
