from django.urls import path, include
# from .views import index
from .views.home import HomeView, JobListView, JobDetailsView, SearchView, favorite
from .views.employee import FavoriteListView, EmployeeMyJobsListView
from .views.employer import (filled, DashboardView, ApplicantsListView,
                            ApplicantPerJobView, AppliedApplicantView,
                            SendResponseView, JobCreateView, JobUpdateView)
app_name = "jobs"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("jobs/", JobListView.as_view(), name="jobs"),
    path("jobs/<int:id>/", JobDetailsView.as_view(), name="jobs-detail"),
    path("search/", SearchView.as_view(), name="search"),
    path("favorite/", favorite, name="favorite"),
    path(
        "employee/",
            include(
                [
                    path("my-applications", EmployeeMyJobsListView.as_view(), name="employee-my-applications"),
                    path("favorites", FavoriteListView.as_view(), name="employee-favorites"),
                ]
            ),
        ),
    path(
        "employer/dashboard/",
        include(
            [
                path("", DashboardView.as_view(), name="employer-dashboard"),
                path("all-applicants/", ApplicantsListView.as_view(), name="employer-all-applicants"),
                path("applicants/<int:job_id>/", ApplicantPerJobView.as_view(), name="employer-dashboard-applicants"),
                path(
                    "applied-applicant/<int:job_id>/view/<int:applicant_id>",
                    AppliedApplicantView.as_view(),
                    name="applied-applicant-view",
                ),
                path("mark-filled/<int:job_id>/", filled, name="job-mark-filled"),
                path("send-response/<int:applicant_id>", SendResponseView.as_view(), name="applicant-send-response"),
                path("jobs/create/", JobCreateView.as_view(), name="employer-jobs-create"),
                path("jobs/<int:id>/edit/", JobUpdateView.as_view(), name="employer-jobs-edit"),
            ]
        ),
    ),
]
   