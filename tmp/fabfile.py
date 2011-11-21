set(fab_user='nerdfiles',
     fab_hosts=['nerdfiles.net'],
     root='/home/nerdfiles/webapps/django/nerdfiles_net/',
     site='nerdfiles.net')

def deploy():
    local('git archive --format=tar HEAD | gzip > $(site).tar.gz')
    #run('rm -rf $(root)$(site)')
    put('$(site).tar.gz', '$(root)$(site).tar.gz')
    #run('cd $(root)$(site) && tar zxf $(site).tar.gz')
    #restart()

def restart():
    run('sh $(root)$(site)/restart.sh')

