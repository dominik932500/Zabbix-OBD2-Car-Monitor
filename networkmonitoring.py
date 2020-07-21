#!/usr/bin/python3
import time
import vodem.simple
import string
import os
import sys
import ntplib #naudojamas laiko sinchronizacijai kai atsiranda interneto rysys
path = '/home/pi/monitoring/network/'
scriptpath = '/home/pi/modem/networkmon.py'
checkdelay = 300
delay = 5

#client = ntplib.NTPClient()
#response = client.request('pool.ntp.org')
#os.system('date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))

host = 'm.home'
pinging = os.system("ping -c 1 " + host)
if pinging == 0: #0 yra gerai
        Connected = True
#       client = ntplib.NTPClient()
#       response = client.request('pool.ntp.org')
#       print(response)
else:
        print("Waiting for modem to connect")
        time.sleep(delay)
        os.execv(scriptpath, sys.argv)


f = open(path + 'ModemConnectionStatus.txt', 'w+')
f.write(str(Connected))
f.close()
#vodem.simple.sms_send("+37066323260", "Message String")

while True:
        CellID = vodem.api.cell_id(overrides=None) #stoties ID prie kurios esame prisijunge
        HWver = vodem.api.hardware_version(overrides=None) #modemo irangos versija
        IMEI = vodem.api.imei(overrides=None)   #modemo IMEI numeris
        ModemMSN = vodem.api.modem_msn(overrides=None) #modemo MSN numeris
        Provider = vodem.api.network_provider_fullname(overrides=None) #operatorius prie kurio prisijungeme
        NetworkType = vodem.api.network_type(overrides=None) #rysio technologija
        PIN_status = vodem.api.pin_status(overrides=None) #ar yra uzdetas PIN
        RealTime = vodem.api.realtime_time(overrides=None) #kiek laiko esame prisijunge prie tinklo
        RMCC = vodem.api.rmcc(overrides=None) #RMCC numeris
        RMNC = vodem.api.rmnc(overrides=None) #RMNC numeris
        SignalBars = vodem.api.signalbar(overrides=None) #signalo lygis
        ICCID = vodem.api.sim_iccid(overrides=None) #ICCID numeris
        IMSI = vodem.api.sim_imsi(overrides=None) #IMSI numeris
        SIM_cardRoam = vodem.api.simcard_roam(overrides=None) #patikra ar SIM kortele uzsienyje
        SMS_capacity = vodem.api.sms_capacity_info(overrides=None) #SMS dezutes parodymai
        UnreadSMS = vodem.api.sms_unread_num(overrides=None) #neperskaityti SMS
        Uptime = vodem.api.system_uptime(overrides=None) #laikas kiek veikia modemas
        rxTotal = vodem.api.total_rx_bytes(overrides=None) #gautu duomenu kiekis
        TotalTime = vodem.api.total_time(overrides=None) #modemo veikimo laikas sumuojant laika nuo paskutinio res$
        txTotal = vodem.api.total_tx_bytes(overrides=None) #issiustu duomenu kiekis
        WAN_APN = vodem.api.wan_apn(overrides=None) #APN pavadinimas prie kurio esame prisijunge
        IP = vodem.api.wan_ipaddr(overrides=None) #viesasis IP adresas
        InboxCount = vodem.simple.sms_inbox_count() #SMS kiekis dezuteje
        InboxPage = vodem.simple.sms_inbox_page(page=1, count=10, safe=False) #Pirmas puslapis SMS duzetes

#       print(CellID)
#       print(HWver)
#       print(IMEI)
#       print(ModemMSN)
#       print(Provider)
#       print(NetworkType)
#       print(PIN_status)
#       print(RealTime)
#       print(RMCC)
#       print(RMNC)
#       print(SignalBars)
#       print(ICCID)
#       print(IMSI)
#       print(SIM_cardRoam)
#       print(SMS_capacity)
#       print(UnreadSMS)
#       print(Uptime)
#       print(rxTotal)
#       print(txTotal)
#       print(TotalTime)
#       print(WAN_APN)
#       print(IP)
#       print(InboxCount)
#       print(InboxPage)

       f = open(path + 'CellID.txt', 'w+')
        f.write(str(CellID))
        f.close()
        f = open(path + 'HWver.txt', 'w+')
        f.write(str(HWver))
        f.close()
        f = open(path + 'IMEI.txt', 'w+')
        f.write(str(IMEI))
        f.close()
        f = open(path + 'ModemMSN.txt', 'w+')
        f.write(str(ModemMSN))
        f.close()
        f = open(path + 'Provider.txt', 'w+')
        f.write(str(Provider))
        f.close()
        f = open(path + 'NetworkType.txt', 'w+')
        f.write(str(NetworkType))
        f.close()
        f = open(path + 'PIN_status.txt', 'w+')
        f.write(str(PIN_status))
        f.close()
        f = open(path + 'RealTime.txt', 'w+')
        f.write(str(RealTime))
        f.close()
        f = open(path + 'RMCC.txt', 'w+')
        f.write(str(RMCC))
        f.close()
        f = open(path + 'RMNC.txt', 'w+')
        f.write(str(RMNC))
        f.close()
       f = open(path + 'SignalBars.txt', 'w+')
        f.write(str(SignalBars))
        f.close()
        f = open(path + 'ICCID.txt', 'w+')
        f.write(str(ICCID))
        f.close()
        f = open(path + 'IMSI.txt', 'w+')
        f.write(str(IMSI))
        f.close()
        f = open(path + 'SIM_cardRoam.txt', 'w+')
        f.write(str(SIM_cardRoam))
        f.close()
        f = open(path + 'SMS_capacity.txt', 'w+')
        f.write(str(SMS_capacity))
        f.close()
        f = open(path + 'UnreadSMS.txt', 'w+')
        f.write(str(UnreadSMS))
        f.close()
        f = open(path + 'Uptime.txt', 'w+')
        f.write(str(Uptime))
        f.close()
        f = open(path + 'rxTotal.txt', 'w+')
        f.write(str(rxTotal))
        f.close()
        f = open(path + 'txTotal.txt', 'w+')
        f.write(str(txTotal))
        f.close()
        f = open(path + 'TotalTime.txt', 'w+')
        f.write(str(TotalTime))
        f.close()
        f = open(path + 'WAN_APN.txt', 'w+')
        f.write(str(WAN_APN))
        f.close()
        f = open(path + 'IP.txt', 'w+')
        f.write(str(IP))
        f.close()
        f = open(path + 'InboxCount.txt', 'w+')
        f.write(str(InboxCount))
        f.close()
        f = open(path + 'InboxPage.txt', 'w+')
        f.write(str(InboxPage))
        f.close()

        time.sleep(checkdelay)