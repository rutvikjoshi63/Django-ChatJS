from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import PITAirportTrainFact
import random
from django.db.models import Count
from django.db.models.functions import TruncDate


def hello(request):
    return HttpResponse("Hello World from PIT Airport Train App!")


def facts_json(request):
    data = list(PITAirportTrainFact.objects.values())
    return JsonResponse(data, safe=False)


def random_fact_page(request):
    facts = PITAirportTrainFact.objects.all()
    if not facts.exists():
        return HttpResponse("No fun facts yet!", status=404)

    fact = random.choice(facts)
    return render(request, "random_fact_page.html", {"fact": fact})


def random_fact_json(request):
    facts = PITAirportTrainFact.objects.all()
    if not facts.exists():
        return JsonResponse({"error": "No fun facts found"}, status=404)

    fact = random.choice(facts)
    return JsonResponse(
        {
            "id": fact.id,
            "fun_fact": fact.funFact,
            "date_added": fact.dateAdded,
        }
    )


def facts_chart(request):
    # Group facts by date and hour and count them
    facts_by_hour = (
        PITAirportTrainFact.objects.extra(
            select={"hour": "strftime('%%Y-%%m-%%d %%H:00', dateAdded)"}
        )
        .values("hour")
        .annotate(count=Count("id"))
        .order_by("hour")
    )

    return render(request, "facts_chart.html", {"facts_by_date": facts_by_hour})
