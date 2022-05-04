from django.http import JsonResponse
from django.views.generic import View
from .models import Post


class PublicPostJSONView(View):

    def get(self, request, *args, **kwargs):
        msgs = Post.objects.public_posts().values(
            "posted_by_id", "message"
        )[:5]
        return JsonResponse(list(msgs), safe=False)
