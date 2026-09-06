from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def issue_list(request):

    issues = [
        "Wi-Fi not working in Lab 3",
        "Projector broken in Room 204",
        "Water cooler not working",
    ]

    context = {
        "name":"CamSolve",
        "message":"Campus problem , Solved",
        "issues":issues
    }
    return render(request,"issues/issue_list.html", context)


