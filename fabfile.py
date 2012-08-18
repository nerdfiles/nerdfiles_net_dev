from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
import sys, os, datetime
import settings

DEBUG = settings.DEBUG

# env

env.user = 'nerdfiles'
env.root = '/home/nerdfiles/webapps/django/'
env.site = 'package'
env.hosts = ['nerdfiles.net']

def host_type():
  run('uname -s')

def test():
  print('Testing instance...')
  with settings(warn_only=True):
    result = local('python manage.py test', capture=True)
  if result.failed and not confirm("Test failed; con't?"):
    abort("Aborting at yr req.")

def pack():
  #local('tar czf nerdfiles_net_package.tgz .')
  print('Packaging instance...')
  local('rm -rf deploy/')
  local('mkdir deploy && cd deploy && touch .delete-me && cd ..')
  local('git archive --format=tar HEAD | gzip > deploy/%s.tar.gz' % env.site)
  print('Package created: ./deploy/%s.tar.gz at %s' % (env.site, datetime.datetime.now()))

def prepare_deploy():
  test()
  pack()
  print('Instance prepared!')

def trial_deploy():
  print('Trial deploy is to test the server against itself...')
  local('rm -rf tmp/ && mkdir tmp')
  print('---')
  print('Grabbing .deploy/%s' % env.site)
  print('---')
  put('%snerdfiles_net/deploy/%s.tar.gz' % (env.root, env.site), '%snerdfiles_net/tmp/' % env.root)
  with cd('%snerdfiles_net/tmp/' % env.root):
    run('tar xzf package.tar.gz')
  with cd('%s' % env.root):
    run('touch nerdfiles_net.wsgi')
  print('---')
  print('Trial complete!')

def prod_deploy():
  print('Wherever you are, deploy!')
  local('rm -rf tmp/ && mkdir tmp')
  print('---')
  print('Grabbing .deploy/%s' % env.site)
  print('---')
  if DEBUG == False:
    #put('%s.tar.gz' % env.site, '%snerdfiles_net/' % env.root)
    print('Placing...')
    with cd('deploy/%s' % env.root):
      #run('tar xzf package.tar.gz')
      print('...that ball!')
  else:
    print('Not doing that just yet. Set DEBUG to False. Still restarting...')
  with cd('%s' % env.root):
    run('touch nerdfiles_net.wsgi')
  print('---')
  print('Deployed!')
  print('Run a git status to confirm.')
  print('')
  print(': "This is end-to-end."')
  print(': "... I know."')
  print('---')

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

