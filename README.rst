=====
MUONIC_DJANGO
=====

Muonic-Django is a consumer to be used with the muonic library for integration with the Django web framework.

Quick start
-----------

1. Install `muonic_django` like this::

    conda install muonic_django -c phyz777

2. Include the muonic_django URLconf in your project urls.py like this::

    url(r'^api/muonic/', include('muonic_django.urls')),

3. Run `python manage.py migrate` (or `muonic_webapp migrate`, when using the `muonic_webapp` package) to create the models.

4. Set os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your.django-project.settings") in your muonic script.

5. Add an instance of muonic_django.consumer.Consumer to your muonic consumers list.

6. Start a measurement

7. Visit http://your-project.url/api/muonic to get your json formatted data (needs rest_framework)
