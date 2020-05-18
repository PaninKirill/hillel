from time import time

from students.tasks import url_logger


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):  # request.path, request.method, execution_time (diff),

        execution_start = time()

        response = self.get_response(request)

        execution_end = time()
        execution_time = execution_end - execution_start

        if request.path.startswith('/admin/'):
            url_logger.delay(request.method, request.path, execution_time)

        return response
