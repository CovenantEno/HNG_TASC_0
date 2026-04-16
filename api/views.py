import requests
from django.http import JsonResponse
from datetime import datetime

def classify_name(request):
    name = request.GET.get('name')

    if not name:
        return JsonResponse({
            "status": "error",
            "message": "Name parameter is required"
        }, status=400)

    if not isinstance(name, str):
        return JsonResponse({
            "status": "error",
            "message": "Name must be a string"
        }, status=422)

    try:
        response = requests.get(f"https://api.genderize.io?name={name}")
        data = response.json()
    except Exception:
        return JsonResponse({
            "status": "error",
            "message": "External API call failed"
        }, status=502)

    gender = data.get("gender")
    probability = data.get("probability")
    count = data.get("count")


    if gender is None or count == 0:
        return JsonResponse({
            "status": "error",
            "message": "No prediction available for the provided name"
        }, status=422)

    sample_size = count

    is_confident = probability >= 0.7 and sample_size >= 100

    processed_at = datetime.utcnow().isoformat() + "Z"

    return JsonResponse({
        "status": "success",
        "data": {
            "name": name.lower(),
            "gender": gender,
            "probability": probability,
            "sample_size": sample_size,
            "is_confident": is_confident,
            "processed_at": processed_at
        }
    })