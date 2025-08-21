from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["GET"])
def health_check(request):
    """
    Health check endpoint for production monitoring.
    Returns basic system status information.
    """
    from django.db import connection
    from django.conf import settings
    
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        health_status = {
            "status": "healthy",
            "database": "connected",
            "debug": settings.DEBUG,
            "allowed_hosts": settings.ALLOWED_HOSTS,
            "timestamp": "2024-01-01T00:00:00Z"  # You can make this dynamic
        }
        return JsonResponse(health_status, status=200)
        
    except Exception as e:
        health_status = {
            "status": "unhealthy",
            "error": str(e),
            "debug": settings.DEBUG
        }
        return JsonResponse(health_status, status=500)