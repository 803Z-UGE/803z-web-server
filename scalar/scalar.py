# scalar/scalar.py
from django.http import HttpResponse
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

def scalar_viewer(request):
    openapi_url = "/api/schema/"
    title = "Scalar Api Reference"
    scalar_js_url = "https://cdn.jsdelivr.net/npm/@scalar/api-reference"
    scalar_proxy_url = ""
    scalar_favicon_url = "/static/favicon.ico"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="shortcut icon" href="{scalar_favicon_url}">
        <style>
        body {{
            margin: 0;
            padding: 0;
        }}
        :root {{
            --scalar-font: 'Inter', sans-serif;
            # .light-mode {{
            #     --scalar-color-1: #121212;
            #     --scalar-color-2: rgba(0, 0, 0, 0.6);
            #     --scalar-color-3: rgba(0, 0, 0, 0.4);
            #     --scalar-color-accent: #0a85d1;
            #     --scalar-background-1: #fff;
            #     --scalar-background-2: #f6f5f4;
            #     --scalar-background-3: #f1ede9;
            #     --scalar-background-accent: #5369d20f;
            #     --scalar-border-color: rgba(0, 0, 0, 0.08);
            # }}
            .dark-mode {{
                --scalar-color-1: rgba(255, 255, 255, 1);
                --scalar-color-2: rgba(255, 255, 255, 1);
                --scalar-color-3: rgba(255, 255, 255, 0.282);
                --scalar-color-accent: rgb(251, 140, 0);
                --scalar-background-1: oklch(21% 0.006 285.885);
                --scalar-background-2: oklch(21% 0.006 285.885);
                --scalar-background-3: color-mix(in oklab, white 2%, transparent);
                --scalar-background-accent: #8ab4f81f;
                --scalar-border-color: #302c2d;
                --scalar-button-1: rgb(251, 140, 0);
            }}
            .dark-mode .sidebar{{
                --scalar-sidebar-background-1: color-mix(in oklab, oklch(14.1% 0.005 285.823) 20%, transparent);
                --scalar-sidebar-item-hover-color: rgb(251, 140, 0);
                --scalar-sidebar-color-active: rgb(251, 140, 0);
                --scalar-sidebar-item-hover-background: transparent;
                --scalar-sidebar-item-active-background: color-mix(in oklab, white 6%, transparent);
            }}
        }}
        </style>
    </head>
    <body>
        <noscript>
            Scalar requires Javascript to function. Please enable it to browse the documentation.
        </noscript>
        <script
            id="api-reference"
            data-url="{openapi_url}"
            data-proxy-url="{scalar_proxy_url}"
            >
        </script>
        <script src="{scalar_js_url}"></script>
    </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns_scalar = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", scalar_viewer, name="docs"),
]