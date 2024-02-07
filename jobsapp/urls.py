from django.urls import path, include
# from .views import index
from .views.home import HomeView, JobListView, JobDetailsView, SearchView, favorite
app_name = "jobs"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("jobs/", JobListView.as_view(), name="jobs"),
    path("jobs/<int:id>/", JobDetailsView.as_view(), name="jobs-detail"),
    path("search/", SearchView.as_view(), name="search"),
    path("favorite/", favorite, name="favorite"),


]
   