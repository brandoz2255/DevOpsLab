Vagrant.configure("2") do |config|
  # Ubuntu VM 1
  
  config.ssh.insert_key = false
  
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/playbooks/main.yml"
    ansible.inventory_path = "ansible/playbooks/inventory.ini"
  end 

  config.vm.define "ubuntu-vm1" do |ubuntu|
    ubuntu.vm.box = "ubuntu/focal64"
    ubuntu.vm.hostname = "ubuntu-vm1"
    ubuntu.vm.network "private_network", ip: "192.168.56.101"
    ubuntu.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.cpus = 3 
    end
    ubuntu.vm.provision "shell", inline: <<-SHELL
      sudo apt update && sudo apt install -y python3 python3-pip
    SHELL
  end

  # Ubuntu VM 2
  config.vm.define "ubuntu-vm2" do |ubuntu|
    ubuntu.vm.box = "ubuntu/focal64"
    ubuntu.vm.hostname = "ubuntu-vm2"
    ubuntu.vm.network "private_network", ip: "192.168.56.102"
    ubuntu.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.cpus = 3
    end
    ubuntu.vm.provision "shell", inline: <<-SHELL
      sudo apt update && sudo apt install -y python3 python3-pip
    SHELL
  end

  # Kali VM
  config.vm.define "kali-vm" do |kali|
    kali.vm.box = "kalilinux/rolling"
    kali.vm.hostname = "kali-vm"
    kali.vm.network "private_network", ip: "192.168.56.103"
    kali.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.cpus = 3
    end
    kali.vm.provision "shell", inline: <<-SHELL
      sudo apt update && sudo apt install -y metasploit-framework
    SHELL
  end
end
 
