import socket
import time
import struct


# Based on mclib by Thomas Schmid (http://github.com/tschmid/mclib)

class SCPI:
    PORT = 5025

    def __init__(self, host, port=PORT):
        self.host = host
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))

    def reset(self):
        # reset and clear device
        self.s.send("*RST\n")
        self.s.send("*CLS\n")
    
    def setVoltage(self, channel, voltage):
        #set output voltage
        self.s.send("VOLTage %.2f,(@%d)\n"%(voltage,channel,))

    def setCurrent(self, channel, voltage):
        #set current
        self.s.send("CURR %.2f,(@%d)\n"%(voltage,channel,))

    def setOutput(self, channel, status):
        if status:
            #enable the output
            self.s.send("OUTPut ON,(@" + str(channel) + ")\n")
        else:
            self.s.send("OUTPut OFF,(@" + str(channel) + ")\n")

    def startCurrentMeasurement(self, channel, samples, res):
        self.s.send("FORM REAL\n")
        self.s.send("FORM:BORD NORM \n")
        self.s.send("SENS:SWE:TINT " + str(1/float(res)) + ",(@" + str(channel) + ")\n")
        self.s.send("SENS:SWE:POIN " + str(samples) + ",(@" + str(channel) + ")\n")
        self.s.send("SENS:CURR:RANG:AUTO ON, (@" + str(channel) + ")\n")
        self.s.send("SENS:CURR:CCOM OFF, (@" + str(channel) + ")\n")
        self.s.send("MEAS:ARR:CURR? (@" + str(channel) + ")\n")
        #self.s.send("FETC:ARR:CURR? (@" + str(channel) + ")\n")
        
    def startPowerMeasurement(self, channel, samples, res):
        self.s.send("SENS:SWE:TINT " + str(1/float(res)) + ",(@" + str(channel) + ")\n")
        self.s.send("SENS:SWE:POIN " + str(samples) + ",(@" + str(channel) + ")\n")
        self.s.send("SENS:CURR:RANG:AUTO ON, (@" + str(channel) + ")\n")
        self.s.send("SENS:CURR:CCOM OFF, (@" + str(channel) + ")\n")
        self.s.send("MEAS:ARR:POW? (@" + str(channel) + ")\n")

    def getCurrentMeasurements(self, channel, samples):
        self.s.settimeout(1)
        buf = []
        n = 1024
        num_digits = int(self.s.recv(2)[1])
        num_samples = int(self.s.recv(num_digits))

        while True:

            try:
                data = self.s.recv(n)
                buf.append(data)
            except socket.timeout:
                break

        records = "".join(buf)
        buf2 = []
        for i in range(0,num_samples,4):
            buf2.append(struct.unpack('>f',records[i:i+4])[0])


        '''
        data = list()
        
        for entry in records:
            try:
                data.append(float(entry.strip(' \r\n')))
            except ValueError:
                print "Error: ", entry
        return data
        '''
        return buf2

    def getCSV(self, filename):
            
        self.s.settimeout(1)
        a = self.s.send("MMEM:EXP:DLOG \"external:\data.csv\"\n")
        buf = []

        #a = self.s.send("DCL\n")
        #print "AAA: ", a
        while True:
            try:
                data = self.s.recv(1024)
                buf.append(data)
            except socket.timeout:
                break
        self.s.settimeout(None)
        return buf

