from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apply.views import ApplyList


urlpatterns = [
    path('apply/',ApplyList.as_view(),name='applylist-url')
]


urlpatterns = format_suffix_patterns(urlpatterns)