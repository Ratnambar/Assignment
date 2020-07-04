from django.forms import ModelForm
from QuestionViewerApp.models import Question


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ['question', 'comment', 'group']