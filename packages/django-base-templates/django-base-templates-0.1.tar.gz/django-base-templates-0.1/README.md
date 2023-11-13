#Django template including base

This packages provides template element (HTML files) for django projects.
Made by Hizart.soft H._T@2022

##Installation

Install the packages using pip:

    ```bash
    pip install django-base-templates

##Usage

-. **Just follow:**

    #Add 'django_template_elements' to the INSTALLED_APPS in your Django project's settings.py:
    ```bash
    INSTALLED_APPS = [
        # ...
        'django_template_elements',
    ]


    #Update the TEMPLATES configuration in your Django project's settings.py:
    ```bash
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'django_base_templates', 'templates')],
            # ...
        },
    ]

    #Use the provided template elements in your Django project's templates:
    ```bash

    {% extends 'django_base_templates/base/base.html' %}

    {% block content %}
        <section>
            <h2>This is the content of the index page</h2>
                <!-- Add your specific content here -->
        </section>
    {% endblock %}


