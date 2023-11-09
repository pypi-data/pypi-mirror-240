import traceback

from convergence.dto.base_dto import FailureInfoDTO, create_api_response
import convergence.helpers.errors as errors


class ManagedApiError(BaseException):
    def __init__(self, status_code, code, message):
        self.status_code = status_code
        self.code = code
        self.message = message


def run_api_method(service, http_response, func):
    api_response = None
    try:
        api_response = create_api_response(func())
    except BaseException as ex:
        # TODO: Log this
        traceback.print_exc()
        api_response = create_internal_error_response(service, errors.API_INTERNAL_ERROR, ex)

    http_response.status_code = api_response.header.status_code
    return api_response


def create_internal_error_response(service, code: str, ex: BaseException):
    failure = FailureInfoDTO()
    message = str(ex)

    if isinstance(ex, ManagedApiError):
        failure.code = ex.code
        failure.message = ex.message
        failure.status_code = ex.status_code

        return create_api_response(failure)
    elif service.get_configuration('application.mode') == 'production':
        message = "An unexpected error happened during API execution"

    failure.code = code
    failure.message = message
    failure.status_code = 500

    return create_api_response(failure)


def convert_object_to_dict(obj):
    if not hasattr(obj, "__dict__"):
        return obj
    result = {}
    for key, val in obj.__dict__.items():
        if key.startswith("_"):
            continue
        element = []
        if isinstance(val, list):
            for item in val:
                element.append(convert_object_to_dict(item))
        else:
            element = convert_object_to_dict(val)
        result[key] = element
    return result
