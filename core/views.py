from django.http import JsonResponse
from django.shortcuts import render
from core.models import Testing
from core.serializers import TestingSerializer

def testing_view(request):
    items = Testing.objects.all()
    serializer = TestingSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)

def health_check(request):
    return JsonResponse({'status': 'ok'})

def testing_detail_view(request, id):
    try:
        item = Testing.objects.get(id=id)
        serializer = TestingSerializer(item)
        return JsonResponse(serializer.data)
    except Testing.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)