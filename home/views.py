from datetime import date

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.forms import CreateNewIssue
from home.models import Issue
from .models import Issue
import json
from django.core import serializers
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.


@login_required(login_url='login')
def home(request):
    issues = Issue.objects.filter(user=request.user)
    context = {'issues': issues}
    return render(request, 'home/home.html', context)


@login_required(login_url='login')
def get_issue_by_id(request, issue_id):
    _issue = model_to_dict(Issue.objects.get(pk=issue_id))
    _issue["create_date"] = str(_issue["create_date"])
    _issue["finish_date"] = _issue["finish_date"] if _issue["finish_date"] is None else str(_issue["finish_date"])
    _issue["start_date"] = _issue["start_date"] if _issue["start_date"] is None else str(_issue["start_date"])
    return HttpResponse(json.dumps(_issue))


@login_required(login_url='login')
def post_new_issue(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        data["create_date"] = date.today()
        data["user_id"] = request.user.id
        _data = Issue()
        _data.__dict__.update(data)
        _data.save()
        result = {"status_code": 1, "status": "success"}
    return HttpResponse(json.dumps(result))


@login_required(login_url='login')
def new_issue(request):
    if request.method == "POST":
        form = CreateNewIssue(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            t.user = request.user
            t.create_date = date.today()
            t.save()
            return redirect('home')
    else:
        form = CreateNewIssue()
    return render(request, 'home/new_issue.html', {"form": form})


@login_required(login_url='login')
def issue(request, issue_id):
    showed_issue = Issue.objects.get(pk=issue_id)
    return render(request, 'home/issue.html', {"issue": showed_issue})


def issue_edit(request, issue_id):
    issue_by_id = Issue.objects.get(pk=issue_id)
    if request.method == "POST":
        form = CreateNewIssue(request.POST, instance=issue_by_id)
        if form.is_valid():
            t = form.save(commit=False)
            t.user = request.user
            t.create_date = date.today()
            t.save()
            return redirect('home')
    else:
        showed_issue = Issue.objects.get(pk=issue_id)
        form = CreateNewIssue(instance=showed_issue)
    return render(request, 'home/new_issue.html', {"form": form})
