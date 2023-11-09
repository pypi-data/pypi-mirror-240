#!/bin/bash

mkdir /tmp/chpalcon
git clone https://github.com/phalcon/cphalcon.git -b $1 /tmp/cphalcon
cd /tmp/cphalcon/build
./install
cd -
rm -rf /tmp/cphalcon
