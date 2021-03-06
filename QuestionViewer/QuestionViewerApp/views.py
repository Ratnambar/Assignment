from django.shortcuts import render
from QuestionViewerApp.models import Group, Question
from django.views.generic import ListView, CreateView
from QuestionViewerApp.forms import QuestionForm
# Create your views here.


class GroupListView(ListView):
    model = Group
    queryset = Group.objects.all()
    template_name = "QuestionViewerApp/dashboard.html"
    context_object_name = "groups"


class QuestionView(CreateView):
    template_name = "QuestionViewerApp/query.html"
    form_class = QuestionForm


class QuestionListView(ListView):
    model = Question
    queryset = Question.objects.all()
    template_name = "QuestionViewerApp/questions-detail.html"
    context_object_name = "questions"


def view_by_cat_button(request, id, *args, **kwargs):
    grp_name = Group.objects.get(id=id)
    groups = Group.objects.all()
    questions = Question.objects.filter(group__id=id)
    context = {
        'grp_name': grp_name,
        'groups': groups,
        'questions': questions
        }
    return render(request, 'QuestionViewerApp/dashboard.html', context)





