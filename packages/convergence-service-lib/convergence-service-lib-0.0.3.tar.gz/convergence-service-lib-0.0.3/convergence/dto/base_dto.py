import abc


class ApiResponseHeader:
    def __init__(self):
        self.body_type: str = 'empty'
        self.status_code: int = 0
        self.code: str = ''
        self.message: str = ''


class ApiResponseBody(abc.ABC):
    @abc.abstractmethod
    def get_response_body_type(self) -> str:
        pass


class ApiResponse:
    def __init__(self):
        self.header = ApiResponseHeader()
        self.body: ApiResponseBody | None = None


class FailureInfoDTO(ApiResponseBody):
    def __init__(self):
        self.status_code: int = 0
        self.code: str = ''
        self.message: str = ''

    def get_response_body_type(self) -> str:
        return 'api_failure'


def __get_list_response_body_type(body):
    result = 'empty'

    if body is not None and len(body) > 0:
        obj = body[0]
        if isinstance(obj, str):
            result = 'list[String]'
        else:
            type = obj.get_response_body_type()
            result = f'list[{type}]'

    return result


def create_api_response(body, status_code=200) -> ApiResponse:
    result = ApiResponse()

    if body is None:
        result.header.status_code = status_code
        result.header.body_type = 'empty'
        result.header.message = 'OK'
    elif isinstance(body, list):
        result.header.body_type = __get_list_response_body_type(body)
        result.header.status_code = status_code
        result.header.code = ''
        result.header.message = 'OK'
        result.body = body
    elif not isinstance(body, ApiResponseBody):
        raise ValueError('Api responses must be a sub class of ApiResponseBody')
    elif isinstance(body, FailureInfoDTO):
        result.header.body_type = body.get_response_body_type()
        result.header.status_code = body.status_code
        result.header.code = body.code
        result.header.message = body.message
    else:
        result.header.body_type = body.get_response_body_type()
        result.header.status_code = status_code
        result.header.code = ''
        result.header.message = 'OK'
        result.body = body

    return result
