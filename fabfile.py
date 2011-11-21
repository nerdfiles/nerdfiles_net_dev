from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.user = 'nerdfiles'
env.root = '/home/nerdfiles/webapps/django/'
env.site = 'package'
env.hosts = ['nerdfiles.net']

def host_type():
  run('uname -s')

def test():
  with settings(warn_only=True):
    result = local('python manage.py test', capture=True)
  if result.failed and not confirm("Test failed; con't?"):
    abort("Aborting at yr req.")

def pack():
  #local('tar czf nerdfiles_net_package.tgz .')
  local('git archive --format=tar HEAD | gzip > $(site).tar.gz')

def prepare_deploy():
  #test()
  pack()

def trial_deploy():
  local('rm -rf tmp/ && mkdir tmp')
  put('$(root)nerdfiles_net/package.tar.gz', '$(root)nerdfiles_net/tmp/')
  with cd('$(root)nerdfiles_net/tmp/'):
    run('tar xzf package.tar.gz')
  with cd('$(root)'):
    run('touch nerdfiles_net.wsgi')

def prod_deploy():
  local('rm -rf tmp/ && mkdir tmp')
  put('$(site).tar.gz', '$(root)nerdfiles_net/tmp/')
  with cd('$(root)'):
    #run('tar xzf nerdfiles_net/package.tar.gz')
    run('touch nerdfiles_net.wsgi')

"""
set(fab_user='nerdfiles',
     fab_hosts=['nerdfiles.net'],
     root='/home/nerdfiles/webapps/django/nerdfiles_net/')

def deploy():
    local('git archive --format=tar HEAD | gzip > $(site).tar.gz')
    #run('rm -rf $(root)$(site)')
    put('$(site).tar.gz', '$(root)$(site).tar.gz')
    #run('cd $(root)$(site) && tar zxf $(site).tar.gz')
    #restart()

def restart():
    run('sh $(root)$(site)/restart.sh')
"""

