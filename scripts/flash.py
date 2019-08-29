#!/usr/bin/python

import sys, getopt
import subprocess
import glob
import re

def main(argv):
    hex_file = ''
    #flash = "\ndevice nrf52\nS\nSWD\n4000\n"#sleep 1000\n"
    flash = "\nconnect\nnrf52\nS\n4000\nr\n"#sleep 1000\n"
    #ip = "\nip 192.168.200.204\n"
    ip = "\nip 192.168.15.61\n"
    tun = "\nip tunnel:683545400\n"
    erase = False
    flash_sd = False
    addr_set = False
    opts, args = getopt.getopt(argv,"hea:s:",["erase", "ram", "remote","tunnel","address="])

    remote = False
    tunnel = False
    for opt,arg in opts:
        if opt in ("--remote"):
            remote = True
        if opt in ("--tunnel"):
            tunnel = True
    sn = None
    if not remote and not tunnel:
        cmd = "echo -e '\nShowEmuList\nexit\n' | JLinkExe"
        print cmd
        p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell='/bin/sh')
        p1.wait()
        p1_out = p1.communicate()
        m_line = []
        for line in p1_out[0].splitlines():
            m = re.search("J-Link\[.\](.*)", line)
            if m:
                m_line.append(m.group(0))
        if len(m_line) == 0:
            print "No J-Link found"
            sys.exit(2)
        elif len(m_line) > 1:
            print "Please select J-Link"
            for l in  m_line:
                print l
            sel = input("> ")
            sn = re.search("Serial number: (.........)", m_line[sel])
            sn = " -SelectEmuBySN " + sn.group(1)

    try:
        hex_file = args[0]
    except:
        hex_file = None
    for opt,arg in opts:
        
        if opt == '-h':
            print 'usage: jlink_flash.py [-e (--erase) -a (--address) 0 filename.hex]'
            sys.exit(2)
        elif opt in ("--remote"):
            flash = ip + flash
        elif opt in ("--tunnel"):
            flash = tun + flash
        elif opt in ("-e", "--erase"):
            flash = flash + "r\ng\nw4 4001e504 2\nw4 4001e50c 1\nr\ng\n"
            erase = True
        elif opt in ("--ram",):
            flash = flash + "r\ng\nmem32 40000900 24\nr\n"
        elif opt in ("-a", "--address"):
            try:
                addr = arg
                addr_set = True
            except:
                addr = None
                addr_set = False
        elif opt in ("-s", "--softdevice"):
            
            s2 = s3 = s4 = '*'
            s1 = arg[:4]
            if len(arg) > 4:
                s2 = arg[4]
            if len(arg) > 5:
                s3 = arg[5]
            if len(arg) > 6:
                s4 = arg[6]
            string = "/home/devzone/softdevice/" + s1 + "*nrf51*" + s2 + "*" + s3 + "*" + s4 + "*.hex"
            files = glob.glob(string)
            if len(files) == 0:
                print "No softdevices maching the argument"
                sys.exit(2)
            elif len(files) > 1:
                print "Several softdevices maching the argument"
                for i in files:
                    print i
                sys.exit(2)
            else:
                flash = flash + "loadbin " + files[0] + " 0\nsleep 100\nr\n"
                flash_sd = True
            
    if hex_file == None:
        files = glob.glob("*.hex")
        if len(files) == 0:
            if not erase and not flash_sd:
                print "No hex-files in current folder"
                print 'usage: jlink_flash.py [-e (--erase) -a (--address) 0 filename.hex]'
                sys.exit(2)
        elif len(files) > 1:
            if not erase and not flash_sd:
                print "More than one hex-file in current folder"
                print 'usage: jlink_flash.py [-e (--erase) -a (--address) 0 filename.hex]'
                sys.exit(2)
        else:
            hex_file = files[0]

    if hex_file != None:
        if addr_set:
            flash = flash + "loadbin " + hex_file + " 0x" + addr +"\nsleep 100\nr\n"
        else:
            flash = flash + "loadbin " + hex_file + " 0\nsleep 100\nr\n"
    flash = flash + "r\ng\nexit\n"

    cmd = "echo -e '" + flash + "' | JLinkExe" + (sn if sn else '')
    print cmd
    pcmd = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell='/bin/sh')
    pcmd.wait()
    pout = pcmd.communicate()
    print pout[0]


if __name__ == "__main__":
    main(sys.argv[1:])

