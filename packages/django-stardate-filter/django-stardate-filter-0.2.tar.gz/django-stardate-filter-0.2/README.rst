======================
Django-stardate-filter
======================

Django-stardate-filter is a small Django app implementing a filter to display a date as a Star-Trek stardate in a template.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "stardate" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'stardate',
    ]

2. Use the filter with a date as follows for example:

    {% now 'Y-m-d H:i' as today %}
    {% load stardate %}
    <div>Stardate: {{ today|stardate }}</div>

And it display the date provided as a stardate

Please use this app and the code freely
Special thanks to Nicolas FLANDROIS for the conversion formula
Live long and Prosper