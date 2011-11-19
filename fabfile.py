set(fab_user='admin',
     fab_hosts=['bristowgroup.com'],
     root='/',
     site='clientsite')

def deploy():
    local('git archive --format=tar HEAD | gzip > $(site).tar.gz')
    run('rm -rf $(root)$(site)')
    put('$(site).tar.gz', '$(root)$(site).tar.gz')
    run('cd $(root)$(site) && tar zxf $(site).tar.gz')
    restart()

def restart():
    run('sh $(root)$(site)/restart.sh')

