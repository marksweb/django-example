django-example
--------------

This is an example django project started with `uv`.

Features
--------

Clear cache view
================

It's possible to clear the cache from the admin using a custom admin view.
This is achieved using a subclass of ``AdminSite``. See ``core.admin.MyAdminSite``
for the view and the URL setup. A basic example is included, but within the view
there is access to the request, so permissions checking can be carried out on
the user if necessary. It also loops over all defined caches and clears each
by default. You could modify this so it only clear certain cache(s).

To use a custom ``AdminSite``, you add it to the installed apps in place of
`django.contrib.admin`. So in `settings.py` you'll see ``"core.apps.MyAdminConfig"`` instead.
