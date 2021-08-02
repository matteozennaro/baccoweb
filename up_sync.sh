#!/bin/bash

rsync -avt --exclude '*gpy*' --exclude '*SFR*' --exclude '.git/' ./ bacco@82.223.84.172:/var/www/vhosts/bacco.dipc.org/httpdocs/
