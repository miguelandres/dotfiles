# Miguely's Dotfiles

This repo uses anishathalye/dotbot for configuring my dotfiles and other utilities.

## Getting started

```sh
git clone git@github.com:miguelandres/dotfiles.git .dotfiles/
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
./install-profile mac mac-personal
```

#### Work Mac

```sh
./install-profile mac mac-cloud
```

#### mackup

After Google Drive is configured, you can run the following command to sync application configuration
```sh
./install-standalone mackup
```

### Linux
#### Raspberry pi

```sh
./install-profile linux
```

On my Corp linux:

```sh
./install-profile glinux
```
