====================
Django Image Gallery
====================

Multi-gallery image gallery for Django.

Installation from Source
========================

::

 $ git clone git://github.com/jbergantine/django-image-gallery.git
 $ cd django-image-gallery
 $ python setup.py install

You will also have to install `PIL <http://pypi.python.org/pypi/PIL>`_, `sorl-thumbnail <http://pypi.python.org/pypi/sorl-thumbnail/>`_, and `South <http://pypi.python.org/pypi/South/>`_.

Installation via PIP Requirements File
======================================

Include in the PIP requirements file the following lines:

::

 PIL==1.1.6
 sorl-thumbnail==3.2.5
 south==0.7.6
 -e git://github.com/jbergantine/django-image-gallery.git#egg=gallery

And then install as normal (IE:)

::

 $ pip install -r path/to/requirements/file.txt

Setup the Project For the Application
=====================================

Add to the project's settings file tuple of INSTALLED_APPS: 

::

 'gallery',
 'pil',
 'sorl.thumbnail',
 'south'

Sync the database to finish installing sorl-thumbnail.

::

 $ python manage.py syncdb

Migrate the database to finish installing gallery.

::

 $ python manage.py migrate

In the project's urls.py file add: 

::

 url(r'^gallery/', include('gallery.urls')),
    
A list of galleries can now be linked to:

::

 <a href="{% url gallery_list %}">Image Galleries</a>
    
Individual galleries can be linked to by passing their ``slug`` to ``gallery_detail``:

::

 <a href="{% url gallery_detail 'slug' %}">A Gallery</a>

Configure the Templates
=======================

By default the templates contain only the bare necessities. To override the default templates, create a directory called gallery in your templates directory and copy the templates from the project into that directory in order to make adjustments to them. If you're using Virtualenv, ``cd`` to the root of the django project and execute the following command: ::

 cp -r $VIRTUAL_ENV/src/django-image-gallery/gallery/templates/gallery templates/gallery