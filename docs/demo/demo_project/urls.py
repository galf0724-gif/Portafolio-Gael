from django.contrib import admin
from django.urls import path
from demo_project.catalog.views import ProductListView, ImportView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='home'),
    path('import/', ImportView.as_view(), name='import'),
]
