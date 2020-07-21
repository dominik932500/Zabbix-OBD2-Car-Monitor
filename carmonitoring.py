#!/usr/bin/env python
import obd
from obd import OBDStatus

import serial
import time #sleep funkcija
import string #translate funkcija
import re #regex
import binascii
import os #reikalinga automatiniam scripto restartui
import sys #reikalinga restartavimo komandos antram argumentui

delay =  5 ##pauzes laikas prisijungiant
checkdelay = 10 #pauze cikle duomenu nuskaitymui
baud = 38400
devpath = '/dev/rfcomm0' #OBD sasajos direktorija
scriptpath = '/home/pi/OBD/carmonitoring.py' #sito skripto direktorija
savepath = '/home/pi/OBD/info/'
#connection = obd.OBD(devpath) # prisijungiame prie OBD sasajos
try:
        connection = obd.OBD(devpath) # prisijungiame prie OBD sasajos
except:
        print("error")
        print('restart in progress') #parodome, kad vyksta restartas
        time.sleep(delay) #trumpa pauze pries bandant jungtis vel
        os.execv(scriptpath, sys.argv) #jei diegimas neijungtas, skriptas yra paleidziamas is naujo
else:
        print("viskas veikia")

#tikriname ar sekmingai prisijungeme prie OBD sasajor ir ar automobilio diegimas yra ijungtas
IgnitionCheck = connection.status() == OBDStatus.CAR_CONNECTED # statusas gali buti arba false arba true

f = open(savepath + 'ignition.txt','w+')
f.write(str(IgnitionCheck)) 
f.close()

print ("Ignition status at the moment:", IgnitionCheck) #koks statusas

if IgnitionCheck == False: #patikra ar ijungtas diegimas
        print('restart in progress') #parodome, kad vyksta restartas
        time.sleep(delay) #trumpa pauze pries bandant jungtis vel
        os.execv(scriptpath, sys.argv) #jei diegimas neijungtas, skriptas yra paleidziamas is naujo
else:
        pass #pass reiskia nieko nedaryti

Port = connection.port_name() #naudojamas nuoseklusis prievadas
Protocol = connection.protocol_name() #naudojamo automobilio OBD protokolo pavadinimas 
ProtocolID = connection.protocol_id() #protokolo numeris pagal PID lentele

f = open(savepath + 'protocol.txt','w+') #atidarome faila su irasymo teisemis
f.write(str(Protocol)) #kintamojo konvertacija i string ir irasymas i faila
f.close()
f = open(savepath + 'protocolID.txt','w+')
f.write(str(ProtocolID)) 
f.close()
f = open(savepath + 'port.txt','w+')
f.write(str(Port)) 
f.close()

SupportedPIDs = connection.supported_commands #paziurime kokius PID galima nuskaityti is sio ECU
f = open(savepath + 'supportedpids.txt','w+')
f.write(str(SupportedPIDs)) 
f.close()

#pradedame tikrinti reikalingus parametrus autotransporto priemones stebejimui
while True:
       CarSpeed = connection.query(obd.commands.SPEED) #siunciame uzklausa automobilio ECU ir isaugome kaip kinta$
        CarRPM = connection.query(obd.commands.RPM)
        CarTroubleCodes = connection.query(obd.commands.GET_DTC)
        CarSpeed = connection.query(obd.commands.SPEED)
        CarAmbientAirTemp = connection.query(obd.commands.AMBIANT_AIR_TEMP)
        CarDistanceMIL = connection.query(obd.commands.DISTANCE_W_MIL)
        CarCoolantTemp = connection.query(obd.commands.COOLANT_TEMP)
        CarEngineLoad = connection.query(obd.commands.ENGINE_LOAD)
        CarOilTemp = connection.query(obd.commands.OIL_TEMP)
        CarRunTime = connection.query(obd.commands.RUN_TIME)
        CarFuelRate = connection.query(obd.commands.FUEL_RATE)
        CarFuelPressure = connection.query(obd.commands.FUEL_PRESSURE)
        CarIntakePressure = connection.query(obd.commands.INTAKE_PRESSURE)
        CarIntakeTemp = connection.query(obd.commands.INTAKE_TEMP)
        CarMAF = connection.query(obd.commands.MAF)
        CarThrottlePos = connection.query(obd.commands.THROTTLE_POS)
        CarFuelLevel = connection.query(obd.commands.FUEL_LEVEL)
        CarOBDStandard = connection.query(obd.commands.OBD_COMPLIANCE)
        CarFuelB1 = connection.query(obd.commands.SHORT_FUEL_TRIM_1)
        CarFuelB2 = connection.query(obd.commands.LONG_FUEL_TRIM_1)
        CarFuelB3 = connection.query(obd.commands.SHORT_FUEL_TRIM_2)
        CarFuelB4 = connection.query(obd.commands.LONG_FUEL_TRIM_2)
        CarELMVersion = connection.query(obd.commands.ELM_VERSION)
        CarELMVoltage = connection.query(obd.commands.ELM_VOLTAGE)
        CarTimingAdvance = connection.query(obd.commands.TIMING_ADVANCE)
        CarAirSTATUS = connection.query(obd.commands.AIR_STATUS)
        CarBarometricPressure = connection.query(obd.commands.BAROMETRIC_PRESSURE)

        localtime = time.asctime(time.localtime(time.time()))
        print(localtime)

        print(CarRPM)
        print(CarSpeed)
        print(CarTroubleCodes)
        print(CarELMVersion)
        print(CarELMVoltage)
        print(CarAmbientAirTemp)
        print(CarDistanceMIL)
        print(CarCoolantTemp)
        print(CarEngineLoad)
        print(CarOilTemp)
        print(CarRunTime)
        print(CarFuelRate)
        print(CarFuelPressure)
        print(CarIntakeTemp)
        print(CarMAF)
        print(CarThrottlePos)
        print(CarFuelLevel)
        print(CarOBDStandard)
        print(CarFuelB1)
        print(CarFuelB2)
        print(CarFuelB3)
        print(CarFuelB4)

       #irasome nuskaitytus parametrus i tekstini faila, kad galetu nuskaityti ir issiusti zabbix agentas

        f = open(savepath + 'localtime.txt','w+').write(str(localtime))
        f = open(savepath + 'speed.txt','w+')
        f.write(str(CarSpeed)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'RPM.txt','w+')
        f.write(str(CarRPM)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'ELMver.txt','w+')
        f.write(str(CarELMVersion)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'akumvolts.txt','w+')
        f.write(str(CarELMVoltage)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'AmbientAirTemp.txt','w+')
        f.write(str(CarAmbientAirTemp)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'checkenginekm.txt','w+')
        f.write(str(CarDistanceMIL)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'tempcoolant.txt','w+')
        f.write(str(CarCoolantTemp)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'EngineLoad.txt','w+')
        f.write(str(CarEngineLoad)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'oiltemp.txt','w+')
        f.write(str(CarOilTemp)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'engineruntime.txt','w+')
        f.write(str(CarRunTime)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'fuelconsumption.txt','w+')
        f.write(str(CarFuelRate)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'fuelpressure.txt','w+')
        f.write(str(CarFuelPressure)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'airtemp.txt','w+')
        f.write(str(CarIntakeTemp)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'MAF.txt','w+')
        f.write(str(CarMAF)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'throttle.txt','w+')
        f.write(str(CarThrottlePos)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'fueltanklevel.txt','w+')
        f.write(str(CarFuelLevel)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'OBDstandard.txt','w+')
        f.write(str(CarOBDStandard)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'bank1.txt','w+')
        f.write(str(CarFuelB1)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'bank2.txt','w+')
        f.write(str(CarFuelB2)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'bank3.txt','w+')
        f.write(str(CarFuelB3)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'bank4.txt','w+')
        f.write(str(CarFuelB4)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'timingadvance.txt','w+')
        f.write(str(CarTimingAdvance)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'airstatus.txt','w+')
        f.write(str(CarAirSTATUS)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'barometricpressure.txt','w+')
        f.write(str(CarBarometricPressure)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'code.txt','w+')
        f.write(str(CarTroubleCodes)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()
        f = open(savepath + 'manifoldpressure.txt','w+')
        f.write(str(CarIntakePressure)) #kintamojo konvertacija i string ir irasymas i faila
        f.close()

        time.sleep(checkdelay)
