from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('blog/', include("blog.urls")),
    path('admin/', admin.site.urls),


]