#!/bin/bash
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
modprobe bluetooth-6lowpan
echo 1 > /proc/sys/net/ipv6/conf/all/forwarding
echo 1 > /sys/kernel/debug/bluetooth/6lowpan_enable
echo "connect "$1" 1" > /sys/kernel/debug/bluetooth/6lowpan_control &&
CONNECTED=false
for i in `seq 1 8` ; do
    FOUND=`grep bt0 /proc/net/dev`
    if [ -n "$FOUND" ] ; then
        ifconfig bt0 add 2001:db8::1/64
        /etc/init.d/radvd restart
        CONNECTED=true
    fi 
    if [ "$CONNECTED" = true ] ; then
        break
    else
        printf "."
    fi
    /bin/sleep 0.5
done
if [ "$CONNECTED" = true ] ; then
    echo "Connected"
    echo `hcitool con`
else
    echo "Could not connect"
fi

