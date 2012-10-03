## Installation

    $ pip install -r requirements.txt

## Usage

Add ``'image-gallery',`` to the ``INSTALLED_APPS`` tuple in ``settings.py``.

Sync the database to finish installing the application.

Add the following to the ``patterns()`` method in the project's primary ``urls.py`` file:

    url(r'^gallery/', include('image-gallery.urls')),
    
A list of galleries can now be linked to:

    <a href="{% url image-gallery %}">Image Galleries</a>

Edit the templates as necessary.