Vagrant.configure("2") do |config|
  # Ubuntu VM 1
  config.vm.define "ubuntu-vm1" do |ubuntu|
    ubuntu.vm.box = "ubuntu/focal64"
    ubuntu.vm.hostname = "ubuntu-vm1"
    ubuntu.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)"
    ubuntu.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = 2
    end
    ubuntu.vm.provision "shell", inline: <<-SHELL
      sudo apt update && sudo apt install -y python3 python3-pip
    SHELL
  end

  # Ubuntu VM 2
  config.vm.define "ubuntu-vm2" do |ubuntu|
    ubuntu.vm.box = "ubuntu/focal64"
    ubuntu.vm.hostname = "ubuntu-vm2"
    ubuntu.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)"
    ubuntu.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = 2
    end
    ubuntu.vm.provision "shell", inline: <<-SHELL
      sudo apt update && sudo apt install -y python3 python3-pip
    SHELL
  end

  # Kali VM
  config.vm.define "kali-vm" do |kali|
    kali.vm.box = "kalilinux/rolling"
    kali.vm.hostname = "kali-vm"
    kali.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)"
    kali.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = 2
    end
    kali.vm.provision "shell", inline: <<-SHELL
      sudo apt update && sudo apt install -y metasploit-framework
    SHELL
  end
    # Kali VM
  config.vm.define "kali-vm1" do |kali|
    kali.vm.box = "kalilinux/rolling"
    kali.vm.hostname = "kali-vm1"
    kali.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)"
    kali.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = 2
    end
    kali.vm.provision "shell", inline: <<-SHELL
      sudo apt update && sudo apt install -y metasploit-framework
    SHELL
  end

end


  