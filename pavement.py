"""paver config file"""

# from testing python book
from paver.easy import sh
from paver.tasks import task, needs


@task
def nosetests():
    """unit testing"""
    sh('nosetests --cover-package=hardDecisions --cover-tests '
       ' --with-doctest --rednose  ./hardDecisions/')

@task
def pylint():
    """pyltin"""
    sh('pylint ./hardDecisions/')

@task
def pypi():
    """Instalation on PyPi"""
    sh('python setup.py sdist')
    sh('twine upload dist/*')


@task
def sphinx():
    """Document creation using Shinx"""
    sh('cd docs; make html; cd ..')

@needs('nosetests', 'pylint', 'sphinx')
@task
def default():
    """default"""
    pass
