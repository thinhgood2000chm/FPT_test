import time

from django.utils.deprecation import MiddlewareMixin


class CheckMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        duration = time.time() - request.start_time
        responsetime =  '{:.2f}ms'.format(duration*1000)
        with open("time.txt", 'w', encoding='utf-8') as f:
            f.writelines(f"start time: {request.start_time}, response time: {responsetime}")
        return response