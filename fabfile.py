#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fabric.api import env, sudo

# modify hosts and user
env.hosts = [""]
env.user = ""

def add_user(user, group=""):
    '''
    usage: fab add_user:user=cara,group=sudo
    '''
    home_dir = "/home/{}".format(user)
    sudo("useradd -d {} -m {}".format(home_dir, user))
    sudo("passwd {}".format(user))
    sudo("usermod -s /bin/bash {}".format(user))
    if group and group != "":
        sudo("usermod -G {} {}".format(group, user))

def del_user(user):
    sudo("userdel -r {}".format(user))

def grant_group(user, group="sudo"):
    sudo("usermod -G {} {}".format(group, user))

def ungrant_group(user, group="sudo"):
    sudo("gpasswd -d {} {}".format(user, group))
