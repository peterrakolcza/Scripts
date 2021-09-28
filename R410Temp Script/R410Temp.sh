#!/bin/bash

# ----------------------------------------------------------------------------------
# Script for checking the temperature reported by the sensors,
# and if deemed too high send the raw IPMI command to enable dynamic fan control.
#
# Requires:
# ipmitool – apt-get install ipmitool
# ipmitool – apt-get install ipmitool
# ----------------------------------------------------------------------------------


# IPMI SETTINGS:
# Modify to suit your needs.
# DEFAULT IP: 192.168.0.120
IPMIHOST=192.168.1.***
IPMIUSER=*******
IPMIPW=******

# TEMPERATURE
# Change this to the temperature in celcius you are comfortable with.
# If the temperature goes above the set degrees it will send raw IPMI command to enable dynamic fan control
MAXTEMP=65

# This variable sends a IPMI command to get the temperature, and outputs it as two digits.
# Do not edit unless you know what you do.
TEMP=$(sensors | grep + | cut -d "+" -f2 | cut -d "." -f1)
TEMP2=(${TEMP//\n/ })
max=${TEMP2[0]}
for n in "${TEMP2[@]}" ; do
    ((n > max)) && max=$n
done
echo "The hottest CPU Core is $max C"

if [[ $max > $MAXTEMP ]];
  then
    echo "Warning: Temperature is too high! Activating dynamic fan control! ($max C)"
    ipmitool -I lanplus -H $IPMIHOST -U $IPMIUSER -P $IPMIPW raw 0x30 0x30 0x01 0x01 >/dev/null 2>&1
  else
    ipmitool -I lanplus -H $IPMIHOST -U $IPMIUSER -P $IPMIPW raw 0x30 0x30 0x01 0x00 >/dev/null 2>&1
    ipmitool -I lanplus -H $IPMIHOST -U $IPMIUSER -P $IPMIPW raw 0x30 0x30 0x02 0xff 0x28 >/dev/null 2>&1
    echo "Temperature is OK ($max C) - MANUAL FAN CONTROL IS ACTIVE"
fi
