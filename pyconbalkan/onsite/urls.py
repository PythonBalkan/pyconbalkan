from django.urls import path
from django.views.generic import TemplateView
from meta.views import Meta


urlpatterns = [
    path('lightning-talks', TemplateView.as_view(template_name="lightningtalks.html", extra_context={
        "meta": Meta(
            title="PyCon Balkan - Lightning Talks",
            description="Not familiar with Lightning Talks ? Don't worry, we will make sure "
                        "that for this year's PyCon we have you prepped and ready, Read more here.",
        )
    }), name='lightning-talks'),
    path('open-spaces', TemplateView.as_view(template_name="openspaces.html", extra_context={
        "meta": Meta(
            title="PyCon Balkan - Open Spaces",
            description="Open Spaces is a PyCon US Concept we will be bringing in to our PyCon from this year, "
                        "read more here to get up to speed on how open-spaces work !"
        )
    }), name='open-spaces'),
]