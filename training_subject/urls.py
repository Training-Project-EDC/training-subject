from django.urls import path
from django.views.generic.base import RedirectView

from .admin_site import training_subject_admin

app_name = 'training_subject'

urlpatterns = [
    path('admin/', training_subject_admin.urls),
    path('', RedirectView.as_view(url='admin/'), name='home_url'),
]
