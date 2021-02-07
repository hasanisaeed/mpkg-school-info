# my_app/views.py
from django.http import JsonResponse
from .models import School


def school_json(request):
    results = {
        "Schools": [],
    }

    for school in School.objects.all():
        line = [str(school), []]
        for item in school.student_set.all():
            line[1].append(str(item))

        results["Schools"].append(line)

    return JsonResponse(results)


