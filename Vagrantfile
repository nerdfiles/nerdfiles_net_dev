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
