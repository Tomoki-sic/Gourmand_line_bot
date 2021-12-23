from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import line_bot_ai.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("line_bot/", line_bot_ai.views.message, name="message"),
    path("admin/", admin.site.urls),
]
