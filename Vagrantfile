# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "debian/buster64"

  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.ssh.forward_agent = true
  config.vm.hostname = "streamvm"
  config.vm.define "streamvm-vagrant" do |v|
  end

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
    vb.name = "streamvm-vagrant"
    vb.memory = 2048 # the default of 512 gives us a OOM during setup.
  end
  config.vm.network :private_network, ip: '192.168.50.50'

  config.vm.synced_folder ".", "/home/vagrant/stream"

  config.vm.provision "shell", path: "config/vagrant/provision_vagrant.sh"
  config.ssh.username = "vagrant"

end