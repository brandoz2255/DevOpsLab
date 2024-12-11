Vagrant.configure("2") do |config|
    # Ubuntu VM for AI Web App
    config.vm.define "ubuntu-vm" do |ubuntu|
      ubuntu.vm.box = "ubuntu/focal64"
      ubuntu.vm.network "private_network", type: "dhcp"
      ubuntu.vm.provision "shell", inline: <<-SHELL
        sudo apt update && sudo apt install -y python3 python3-pip
      SHELL
    end
  
    # Kali VM for Security Testing
    #config.vm.define "kali-vm" do |kali|
      #kali.vm.box = "kalilinux/rolling"
      #kali.vm.network "private_network", type: "dhcp"
      #kali.vm.provision "shell", inline: <<-SHELL
        #sudo apt update && sudo apt install -y metasploit-framework
      SHELL
    end
  end
  