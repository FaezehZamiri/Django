from django.contrib import admin
from django.urls import path ,include
from . import veiws
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from contactus.views import recordproblemform

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', veiws.about),
    path('',recordproblemform),
    path('contactus/',include('contactus.urls')),
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)