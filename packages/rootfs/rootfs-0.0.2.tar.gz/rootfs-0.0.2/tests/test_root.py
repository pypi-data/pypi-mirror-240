#!/usr/bin/env python3

import rootfs
import pathlib

def test_file():
    file = rootfs.file('/usr/share/cats.jpg')
    assert isinstance(file, pathlib.Path)

def test_cat():
    file = rootfs.cat('/usr/share/cats.jpg')
    assert type(file) == bytes
    colors = rootfs.cat('/etc/colors').decode().splitlines()
    assert 'red' in colors

def test_ls():
    assert 'colors' in rootfs.list('/etc')
    assert 'share' in rootfs.list('/usr')

def test_find():
    cats = [p for p in rootfs.find('/usr') if p.name == 'cats.jpg']
    assert cats
