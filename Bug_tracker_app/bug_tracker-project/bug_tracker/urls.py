
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts import views
import company_head.views as chviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('manageproject/', include('manage_project.urls')),
    path('companyhead/', include('company_head.urls')),
    path('profiles/', include('profiles.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
