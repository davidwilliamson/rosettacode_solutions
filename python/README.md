# rosettacode_solutions

Solutions to problems posed at [rosettacode.org](https://rosettacode.org)

[https://rosettacode.org/wiki/Category:Programming_Tasks](https://rosettacode.org/wiki/Category:Programming_Tasks)

## Tools

- run static code checks: `make test-all`
- run all solutions: `./run-all.sh`
- run solutions in a container: `make run-docker`

## Setup

**NOTE** Code written for python 3.7.1 To create a python development environment from scratch, see 
[Create-python-dev-environment](#create-python-dev-environment)


1. clone this repo
2. `cd rosettacode_solutions`
3. create this virtual environment:
```
VERSION='3.7.1'
MY_VIRTUAL_ENV=$(cat .python-version)
pyenv virtualenv $VERSION $MY_VIRTUAL_ENV
pip install -r requirements.txt
```

## Create python dev environment

The following steps are only necessary if you do not currently have a python development environment set up on your machine.

### On a Mac:

```bash
# Install GNU tools.

make --version || xcode-select --install
gcc --version || xcode-select --install


# Install [homebrew](https://brew.sh/).

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


# Install some system utilities that python depends on
# ref the MacOS section of https://github.com/pyenv/pyenv/wiki
brew install openssl readline sqlite3 xz zlib
# Note: openssl may be outdated. If the version (shown by brew) is less than 1.0.2p, consider

brew reinstall openssl

# When running **Mojave** or higher (10.14+) you will also need to install additional SDK headers:

sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /


# Install pyenv and its companion plugin pyenv-virtualenv
# ref: https://github.com/pyenv/pyenv
# ref: https://github.com/pyenv/pyenv-virtualenv

brew install pyenv

brew install pyenv-virtualenv

# configure pyenv and virtualenv-init
# edit .bash_profile or .profile
# NOTE: put this AFTER any other lines that modify PATH
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
fi
```

### On Ubuntu

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

# install utilities
# ref: https://github.com/pyenv/pyenv/wiki
sudo apt-get update
sudo apt-get install -y \
        make \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        xz-utils \
        tk-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev



# install pyenv-virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Restart your shell so the path changes take effect. You can now begin using pyenv.
# **NOTE** may need to pop a new terminal window
exec "$SHELL"
```

