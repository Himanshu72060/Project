
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.addshow, name='addandshow'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='updatedata')
]

urlpatterns += static(settings.STATIC_URL, document=settings.STATIC_ROOT)
