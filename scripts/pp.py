#! /usr/bin/python2.7

import SCPI
import time
import sys
from eng import EngNumber

class PA_control():

    def help(self):
        print "usage:"
        print "pp\t\tusage"
        print "pp 2\t\tpower cycle ch 2"
        print "pp 1off\t\tch 1 off"
        print "pp 1on\t\tch 1 on"
        print "pp 1v3.3\tch 1 voltage to 3.3V"
        print "pp 1c\t\taverage current ch 1"
        print "pp 1cc\t\tcontinuous average current ch 1"

    def connect(self):
        self.s = SCPI.SCPI('pa05')
    def turn_on(self):
        self.s.setOutput(int(self.ch),1)
    def turn_off(self):
        self.s.setOutput(int(self.ch),0)
    def set_voltage(self, voltage):
        self.s.setVoltage(int(self.ch),float(voltage))

    def main(self, argv):
        if len(argv) <= 1:
            self.connect()
            self.ch = 3
            self.help()
            self.turn_off()
            time.sleep(0.5)
            self.turn_on()
            return -1

        self.connect()
        cmd = argv[1][1:]
        try:
            self.ch = int(argv[1][0])
        except:
            self.help()
            return -1

        if cmd == '':
            self.turn_off()
            time.sleep(0.5)
            self.turn_on()
        elif cmd == 'on':
            self.turn_on()
        elif cmd == 'off':
            self.turn_off()
        elif cmd[0] == 'v':
            if float(cmd[1:]) > 3.6:
                print "voltage too high"
                return -1
            self.set_voltage(cmd[1:])
        elif cmd[0] == 'c':
            try:
                if cmd[1] == 'c':
                    while(True):
                        ret = self.s.getAvgCurrent(self.ch,195312*2,195312)
                        print str(EngNumber(ret)) + "A"
            except:
                ret = self.s.getAvgCurrent(self.ch,195312*2,195312)
                print str(EngNumber(ret)) + "A"

if __name__ == '__main__':
    pa = PA_control()
    pa.main(sys.argv)


