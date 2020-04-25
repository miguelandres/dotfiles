# Miguely's Dotfiles

This repo uses anishathalye/dotbot for configuring my dotfiles and other utilities.

## Getting started


```sh
ssh-keygen -t rsa -b 4096 -C "miguelandres@users.noreply.github.com" || exit 1
eval "$(ssh-agent -s)"
if [ `uname` -eq "Darwin" ] then
  echo << EOF
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_rsa
EOF > ~/.ssh/config
fi
ssh-add -K ~/.ssh/id_rsa || ssh-add ~/.ssh/id_rsa 

echo "Put the following key in your github account."
cat ~/.ssh/id_rsa.pub

read -p "Press enter when done"

git clone --recurse-submodules -j8 git@github.com:miguelandres/dotfiles.git .dotfiles/
```

## Profiles and configs

Since my dotfiles vary slightly between linux and mac, and whether this is personal or a work computer, I use a [more complicated system than the default](https://github.com/anishathalye/dotbot/wiki/Tips-and-Tricks#more-advanced-setup)

There are, so far, the following profiles

* `mac`
  * Sets up zsh
  * Sets up oh-my-zsh
  * adds standard zshrc imports for mac that improve integration with the system (and iTerm)
  * installs homebrew
  * installs a brewfile that includes all the Mac App Store apps, downloaded apps and brews I need for personal and work computers.
* `mac-personal`: Installs office apps, and other apps I cannot install on corp laptop.
* `mac-cloud`: Installs gcloud, kubectl, docker and terraform. May the force be with you.
* `linux`: vanilla linux installation of zsh, oh-my-zsh and standard imports
* `glinux`: specific steps to set up zsh on my machine on glinux, and google specific imports. May move some of this off github.

## How to use

### macOS

#### Personal mac

```sh
./install-profile mac && ./install-profile mac-personal
```

#### Work Mac

```sh
./install-profile prereqs-corp-mac && ./install-profile mac && ./install-profile mac-corp && ./install-profile cloud-mac
```

#### mackup

After Google Drive is configured, you can run the following command to sync application configuration
```sh
refresh-mackup
```

### Linux
#### Raspberry pi

```sh
./install-profile linux && ./install-profile linux-personal
```

On my Corp linux:

```sh
./install-profile prereqs-glinux && ./install-profile linux && ./install-profile glinux
```


## Refresh configuration

At any time after first sucessful installation you can invoke `refresh-dotfiles` to sync everything and `refresh-mackup` to sync mackup only. Both will involve a `git pull` and running the respective commands for the correct platform