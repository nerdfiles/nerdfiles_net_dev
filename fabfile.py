from fabric.api import local, cd, run

local_dir = './'


def init ():
    """Init"""

    local("pip install -r requirements.txt")


def launch(version="", port=8001):
    """Launch"""

    local("python%s manage.py runserver %s" % (version, port))


def install(version=""):
    """Install Django and config"""
    local("python%s manage.py syncdb --all" % version)
    local("python%s manage.py schemamigration --initial app" % version)
    # local("python%s manage.py migrate rest_framework.authtoken " % version)
    local("python%s manage.py createsuperuser" % version)


def clean():
    """Remove all the .pyc files"""
    local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)
