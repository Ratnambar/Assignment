from django.urls import path
from QuestionViewerApp.views import GroupListView,QuestionView,view_by_cat_button

urlpatterns = [
    path('', GroupListView.as_view(), name="dashboard"),
    path('<int:id>/', view_by_cat_button, name="detail"),
    path('query', QuestionView.as_view(), name="query")
]