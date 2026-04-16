import requests
from django.http import JsonResponse
from datetime import datetime, timezone

def classify_name(request):
    try:
        name = request.GET.get("name")

        if not name:
            return JsonResponse(
                {"status": "error", "message": "Missing name parameter"},
                status=400
            )

        if not isinstance(name, str):
            return JsonResponse(
                {"status": "error", "message": "Name must be a string"},
                status=422
            )

        response = requests.get(
            "https://api.genderize.io",
            params={"name": name},
            timeout=5
        )
        response.raise_for_status()

        data = response.json()

        gender = data.get("gender")
        probability = data.get("probability")
        count = data.get("count")

        if gender is None or count == 0:
            return JsonResponse(
                {"status": "error", "message": "No prediction available for the provided name"},
                status=422
            )

        is_confident = probability >= 0.7 and count >= 100

        result = {
            "status": "success",
            "data": {
                "name": name,
                "gender": gender,
                "probability": probability,
                "sample_size": count,
                "is_confident": is_confident,
                "processed_at": datetime.now(timezone.utc).isoformat()
            }
        }

        res = JsonResponse(result)
        res["Access-Control-Allow-Origin"] = "*"
        return res

    except requests.RequestException:
        return JsonResponse(
            {"status": "error", "message": "Upstream service unavailable"},
            status=502
        )

    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=500
        )