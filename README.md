# Miguely's Dotfiles

This repo uses [@anishathalye/dotbot](http://github.com/anishathalye/dotbot) for configuring my dotfiles and other utilities.

## Getting started (basic)


```sh
git clone --recurse-submodules -j8 git@github.com:miguelandres/dotfiles.git ~/.dotfiles/
cd ~/.dotfiles/
```

## Getting started (With SSH auth)


```sh
[ -f ~/.ssh/id_rsa ] || ssh-keygen -t rsa -b 4096 -C "miguelandres@users.noreply.github.com"
eval "$(ssh-agent -s)"
if [ `uname` = "Darwin" ]; then;
  tee ~/.ssh/config << EOF
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_rsa
EOF
fi
ssh-add -K ~/.ssh/id_rsa 2>/dev/null || ssh-add ~/.ssh/id_rsa

echo "Put the following key in your github account."
cat ~/.ssh/id_rsa.pub

git clone --recurse-submodules -j8 git@github.com:miguelandres/dotfiles.git ~/.dotfiles/
cd ~/.dotfiles/
```


## Profiles and configs

Since my dotfiles vary slightly between linux and mac, and whether this is personal or a work computer, I use a [more complicated system than the default](https://github.com/anishathalye/dotbot/wiki/Tips-and-Tricks#more-advanced-setup)

My modifications are as follows:

* `meta/`: Contains base configs, lightweight configs that can be run before installing profiles. These are used mostly for weird exceptions in glinux and gmac that need to be run BEFORE anything that would be common to the OS.
* `meta/configs`: contains all regular configs. These configs can be referred to by a profile, and reused in multiple profiles.
* `meta/profiles`: Contains profiles. Each profile is a list of `meta/configs` identifiers separated by `\n` and these are run in order.

### Base Configs:
* `base`
  * cleans up old symlinks
  * creates `~/.zshrc-imports` in preparation for all of the files that will be put there
* `base-glinux`
  * sets up zsh in ganpati2, otherwise it doesn't stick as the default
  * adds a git wrapper for performance in CitC.
* `base-gmac`
  * Changes permissions to the directiories `brew` uses. This is only necessary in gmac.

### Profiles
* `mac`: Base configuration, sets up oh-my-zsh, installs homebrew and all the apps I normally use.
  * `mac-personal`: Installs apps that are not allowed in corp (like MS Office) and things Santa complains about
  * `mac-cloud`: Installs  `docker`, `kubernetes` and `gcloud` using `brew`.
* `linux`: vanilla linux installation of zsh, oh-my-zsh and standard imports, etc.
  * `raspbian-docker`: Installs docker ON the raspberry pi exclusively.
  * `glinux`: google specific imports. May move some of this off github.

### Configurations
Each configuration is a list of base configs and a list of profiles to run. These are run in the order in which they were declared in the invocation.

## macOS

### Personal mac

```sh
./install-profile --pull --save-config mac mac-personal
```

### Mati's mac

```sh
./install-profile --pull --save-config mac mac-mati
```

### Work Mac

```sh
./install-profile --pull --save-config --base-configs=base,base-gmac mac mac-corp
```


## Linux
### Raspberry pi

```sh
./install-profile --pull --save-config linux linux-personal raspbian-docker docker-home-server
```

### Personal Linux Laptop

```sh
./install-profile --pull --save-config linux linux-personal linux-gui
```

### On my Corp linux:

```sh
./install-profile --pull --save-config --base-configs=base,base-glinux linux glinux
```

## [mackup](https://github.com/lra/mackup)

After Google Drive is configured, you can run the following command to sync application configuration
```sh
mackup restore && mackup backup
```

Look at mackup/mackup.cfg to see what will not be synced (or maybe customize it and just choose apps manually)


## Refresh configuration

At any time after first sucessful installation you can invoke `refresh`, which will in practice re-invoke the last command to which you passed `--save-config`.
