VAGRANTFILE_API_VERSION = '2'

ANSIBLE_INVENTORY_PATH  = 'ops/inventory/development-single'

BOX                     = 'saucy64-official'
BOX_URL                 = 'http://cloud-images.ubuntu.com/vagrant/saucy/      current/saucy-server-cloudimg-amd64-vagrant-disk1.box'


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box       = BOX
    config.vm.box_url   = BOX_URL

    

    # Application Server 
    config.vm.define 'app' do |app|
        app.vm.hostname = 'vagrant-app'

        app.vm.synced_folder '.', '/srv/app'
        app.vm.network :private_network, ip: '10.0.0.2'
        app.vm.provision :ansible do |ansible|
            ansible.inventory_path  = ANSIBLE_INVENTORY_PATH
            
            ansible.playbook        = 'ops/single-vm.yml'
            
        end
    end


end

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  #config.vm.box = 'digital_ocean'
  #config.vm.box_url = "https://f0fff3908f081cb6461b407be80daf97f07ac418.googledrive.com/host/0BwtuV7VyVTSkUG1PM3pCeDJ4dVE/centos7.box"
  #config.ssh.private_key_path = '~/.ssh/id_rsa'

  config.vm.hostname = 'wesam3' #droplet name
  config.ssh.username = 'nerdfiles' #default root

  config.vm.provider :digital_ocean do |provider, override|
    override.ssh.private_key_path = '~/.ssh/id_rsa'
    override.ssh.forward_agent = true
    override.vm.box = 'digital_ocean'
    override.vm.box_url = "https://github.com/smdahlen/vagrant-digitalocean/raw/master/box/digital_ocean.box"

    provider.ca_path = '/usr/share/curl/ca-bundle.crt'
    provider.token = 'baf280cb409a88a5f9fca291624e0d1a82afb80b87fd45fdcf4cbb04897d2909' #personal token
    provider.image = 'CentOS 7'
    provider.region = 'nyc2'
    provider.size = '512mb'
  end
end

