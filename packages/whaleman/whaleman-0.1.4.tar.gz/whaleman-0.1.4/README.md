## Intro
whaleman It is a simple tool to build , push and tag docker images.

using config .ini file to configure the tool. its annoying sometimes we tagging the image over and over again.

with this we can simply use config for tagging and versioning for each project/dockerfile


## Installation

```bash
pip install whaleman
```

## Usage
by default name of the config file is docker.ini

the content of the config file is

```ini
[registry]
name = index.docker.io # name of the registry URL , default is index.docker.io
login = True # if you want to login to the registry , default is False
# username for the registry 
# default is None or grab from env var with name DOCKER_USERNAME
docker_username = myusername 
# password for the registry , use quotes if you have symbol in the password.
# default is None or grab from env var with name DOCKER_PASSWORD
docker_password = "mypassword"  

[image]
name = soberdev/homepage # this is name of the image, required
tag = 0.1.8 # this is the version of the image or initial version, required
```

or if you want to create a config file simply run:

```bash
whaleman createconfig
```

the createconfig takes arguments, by default it will create a config file with name docker.ini

but you can create a config file with any name you want with the argument -n

```bash
whaleman createconfig -n myconfig.ini
```

### Run the tool

patch choices are **micro, minor and major**

```bash
whaleman build <patch>
```

build the image and patch the version, after done will auto increment the version in the config file

you can build and push the image to the registry with the positional argument **push**

```bash
whaleman build <patch> push
```

or you can use any config file and custom dockerfilename

```bash
whaleman build <patch> push -f myconfig.ini -df mydockerfile.Dockerfile
```

## For more information
```bash
whaleman -h
```

```bash
whaleman build -h
```

```bash
whaleman createconfig -h
```

## Logging Level

default is INFO, but you can change it with the argument -l

```bash
whaleman -l DEBUG build <patch>
```