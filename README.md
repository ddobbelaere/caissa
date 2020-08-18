# Caissa

[![Build Status](https://travis-ci.org/ddobbelaere/caissa.svg?branch=master)](https://travis-ci.org/ddobbelaere/caissa)
[![Coverage Status](https://coveralls.io/repos/github/ddobbelaere/caissa/badge.svg?branch=master)](https://coveralls.io/github/ddobbelaere/caissa?branch=master)
[![PyPI version](https://badge.fury.io/py/caissa.svg)](https://badge.fury.io/py/caissa)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1959/badge)](https://bestpractices.coreinfrastructure.org/projects/1959)

Caissa is an intelligent voice-controlled personal assistant (still under development).

Currently she is able to play your favorite internet radio. Some of her upcoming skills include

  - play chess
  - monitor live chess games
  - help you study foreign languages

![Component Overview](https://github.com/ddobbelaere/caissa/raw/master/doc/caissa.png)

## Building and running Caissa

### Debian and derivatives

#### Dependencies

```sh
sudo apt update
sudo apt install -y espeak mpg123 libasound2-dev libpulse-dev python3-setuptools
```

Optionally, if you want to talk to Caissa via remote control, install LIRC (by following [this guide](https://github.com/josemotta/IoT.Starter.Api/tree/master/gpio-base#lirc-linux-infrared-remote-control-for-raspberry-pi) for Raspbian Stretch, apply [this workaround](https://github.com/raspberrypi/linux/issues/2993#issuecomment-497420228) for Raspbian Buster) and the following dependencies:

```sh
sudo apt-get install -y cython gcc liblircclient-dev python3-dev
sudo pip3 install pyalsaaudio python-lirc
```

#### Notes for Raspbian Buster
 - The PyPi version of `python-lirc` is still shipped (as of August 18, 2020) with a cython generated C file that is incompatible with Python 3.7.
 - Build/install from the sources instead:
 
    ```
    sudo apt install -y cython3 gcc liblircclient-dev python{,3}-{dev,setuptools}
    git clone https://github.com/tompreston/python-lirc.git
    cd python-lirc/
    make py3 && sudo python3 setup.py install
    sudo pip3 install -U .
    ```

#### Installation
Install the latest stable release:

```sh
sudo pip3 install caissa
```

You can now type `caissa --help` and start. On Raspberry Pi `sudo caissa` is necessary to access various devices.
