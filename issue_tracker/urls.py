"""issue_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.http import HttpResponse
from django.template.response import TemplateResponse


def index_view(request):
    """Simple HTML index page that links to the API"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Issue Tracker API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #333; }
            .link { margin: 10px 0; }
            a { color: #007cba; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>Issue Tracker API</h1>
        <p>Welcome to the Issue Tracker REST API.</p>
        <div class="link">
            <a href="/api/">Browse API</a> - Interactive API browser
        </div>
        <div class="link">
            <a href="/admin/">Admin Interface</a> - Django admin
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('issues.urls')),
    url(r'^$', index_view, name='index'),
]
