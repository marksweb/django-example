from django.contrib import admin, messages
from django.core.cache import caches, InvalidCacheBackendError
from django.http import HttpResponseRedirect
from django.urls import path, reverse

from django.utils.translation import gettext_lazy as _


class MyAdminSite(admin.AdminSite):
    site_header = "Custom Administration"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("clear-cache/", self.admin_view(self.clear_cache), name="clear_cache")
        ]
        return my_urls + urls

    def clear_cache(self, request):
        """Clear a named cache via the Django cache functionality"""
        for name in caches:
            try:
                cache = caches[name]
                cache.clear()
            except (InvalidCacheBackendError, KeyError):
                messages.error(request, _('Cache named "{}" not found'.format(name)))
            except NotImplementedError:
                messages.error(
                    request,
                    _(
                        (
                            'The cache named "{}" does not support clearing '
                            "(do you have django-debug-toolbar installed?"
                        ).format(name)
                    ),
                )
            else:
                messages.success(request, _('"{}" cache cleared'.format(name)))
        index_path = reverse("admin:index", current_app=self.name)
        return HttpResponseRedirect(request.GET.get("next", index_path))
