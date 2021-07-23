#!/bin/bash

rsync -avt --exclude '*gpy*' --exclude '*SFR*' bacco@82.223.84.172:/var/www/vhosts/bacco.dipc.org/httpdocs/ .
