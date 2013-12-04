========================
Bellmetric Reports
========================

*December 04, 2013 3:00pm*

System
======
- ubuntu 12.04.3 LTS ($ cat /etc/lsb-release)
- python 2.7.3 ($ python -V)
- django 1.5.5 final ($ echo "import django; print django.VERSION" | python)
- virtualenv 1.10.1 ($ virtualenv --version)

Django project
==============

- coding style: PEP8
- layout: `github.com/morenopc/django-twoscoops-project <https://github.com/morenopc/django-twoscoops-project>`_

adapt from: Two Scoops of Django by Daniel Greenfeld book::

    $ django-admin.py startproject --template=https://github.com/morenopc/django-twoscoops-project/zipball/develop --extension=py,rst,html bellmetric_reports

Getting start
=============

setting local project::

    $ bellmetric-reports-project$ ./scripts/local.sh

runserver::

    $ bellmetric-reports-project$ ./scripts/runserver.sh
