from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Issue
from .forms import IssueForm

def issue_list(request):

    issues = Issue.objects.all()

    
    return render(
        request,
        "issues/issue_list.html",
          {"issues":issues}
    )

def create_issue( request):
    if request.method == "POST":
        form = IssueForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("issue-list")

    else:
        form = IssueForm()

    return render(
        request,
        "issues/create_issue.html",
        {"form":form}
    )


