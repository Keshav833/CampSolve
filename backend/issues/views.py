from django.shortcuts import render, redirect , get_object_or_404
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

def issue_detail(request, issue_id):
    issue = get_object_or_404(Issue, id = issue_id)

    return render(
        request , 
        "issues/issue_detail.html",
        {"issue":issue}
    )

def edit_issue(request, issue_id):
    issue = get_object_or_404(Issue, id = issue_id)

    if request.method == "POST":
        form = IssueForm(request.POST,instance=issue)

        if form.is_valid():
            form.save()
            return redirect("issue-detail",issue_id = issue.id)

    else:
        form = IssueForm(instance=issue)

    return render(
        request,
        "issues/edit_issue.html",
        {"form":form ,"issue":issue}
    )

def delete_issue(request, issue_id):
    issue = get_object_or_404(Issue, id = issue_id)

    if request.method == "POST":
        issue.delete()
        return redirect("issue-list")

    return render(
        request,
        "issues/delete_issue.html",
        {"issue":issue}
    )
    