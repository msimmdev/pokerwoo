from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from upload.models import AvatarUpload

@require_POST
@csrf_exempt
def avatarUpload(request):
    instance = AvatarUpload(file=request.FILES['avatarupload'])
    instance.save()
    file_item = request.FILES['avatarupload']
    data = {
        "name": file_item.name,
        "size": file_item.size,
        "type": file_item.content_type,
        "url": 'https://d3jc1sdxhnw81f.cloudfront.net/' + instance.file.name
    }
    return JsonResponse(data)
