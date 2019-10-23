from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from notify.models import SubscriberInfoModel


@csrf_exempt
def add_subscriber(request):
    if request.method == "POST":
        # 添加 subscriber
        subscriber_email = request.POST.get("email", default=None)

        if not subscriber_email:
            return JsonResponse({"code": "401", "msg": "Incomplete request data"})

        # 保存到数据库
        SubscriberInfoModel.add_subscriber(email=subscriber_email)

        return JsonResponse({"code": "200", "img": "ok"})
    else:
        return HttpResponse(status=404)
