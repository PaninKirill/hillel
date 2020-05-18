from time import time

from students.models import Logger


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):  # request.path, request.method, execution_time (diff),

        execution_start = time()

        response = self.get_response(request)

        execution_end = time()
        execution_time = execution_end - execution_start

        if request.path.startswith('/admin/'):
            Logger.objects.create(
                method=request.method,
                path=request.path,
                execution_time=execution_time,
            )

        return response
