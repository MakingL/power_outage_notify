from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from notify.forms import SubscriberModelForm


@csrf_exempt
def add_subscriber(request):
    if request.method == "GET":
        email_form = SubscriberModelForm(request.GET, request.FILES)
        if not email_form.is_valid():
            return JsonResponse({"code": "406", "msg": "Bad request"})
        # 添加 subscriber
        email_form.save()

        return JsonResponse({"code": "200", "msg": "ok"})
    else:
        return HttpResponse(status=406)
