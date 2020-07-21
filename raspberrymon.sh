#!/bin/bash

while true
do
	temp=$(vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*')  #isvesti tik skaicius
	echo $temp > /home/pi/monitoring/temperatura.txt #mikrovaldiklio temperatura

	throttle=$(vcgencmd get_throttled  | cut -d= -f2-) #isvesti viska po = simbolio
	echo $throttle > /home/pi/monitoring/throttle.txt #mikrovaldiklio  veikimo parametras

	measure_clock_arm=$(vcgencmd measure_clock arm | cut -d= -f2-)  #isvesti viska po = simbolio
	let "measure_clock_arm = $measure_clock_arm / 1000000" # hz pakeiciame i mhz
        echo $measure_clock_arm > /home/pi/monitoring/measure_clock_arm.txt #procesoriaus greitis

	volts_core=$(vcgencmd measure_volts core | cut -d= -f2- | tr -d '[:alpha:]')  #isvesti viska po = ir istrinti vissas raides
        echo $volts_core > /home/pi/monitoring/volts_core.txt #mikrovaldiklio procesoriaus itampa
	volts_sdram_c=$(vcgencmd measure_volts sdram_c | cut -d= -f2- | tr -d '[:alpha:]')  #isvesti viska po = ir istrinti vissas raides
        echo $volts_sdram_c > /home/pi/monitoring/volts_sdram_c.txt #mikrovaldiklio sdram_c itampa
	volts_sdram_i=$(vcgencmd measure_volts sdram_i | cut -d= -f2- | tr -d '[:alpha:]')  #isvesti viska po = ir istrinti vissas raides
        echo $volts_sdram_i > /home/pi/monitoring/volts_sdram_i.txt #mikrovaldiklio sdram_i itampa
	volts_sdram_p=$(vcgencmd measure_volts sdram_p | cut -d= -f2- | tr -d '[:alpha:]')  #isvesti viska po = ir istrinti vissas raides
        echo $volts_sdram_p > /home/pi/monitoring/volts_sdram_p.txt #mikrovaldiklio sdram_p itampa

        get_mem_gpu=$(vcgencmd get_mem gpu | cut -d= -f2- | tr -d '[:alpha:]' | cut -d= -f2- | tr -d '[:alpha:]')  #isvesti viska po = ir istrinti vissas raides
        echo $get_mem_gpu > /home/pi/monitoring/get_mem_gpu.txt #mikrovaldiklio GPU atminties naudojimas 
        get_mem_arm=$(vcgencmd get_mem arm | cut -d= -f2- | tr -d '[:alpha:]' | cut -d= -f2- | tr -d '[:alpha:]')  #isvesti viska po = ir istrinti vissas raides
        echo $get_mem_arm > /home/pi/monitoring/get_mem_arm.txt #mikrovaldiklio CPU atminties naudojimas

        firmware=$(vcgencmd version) #isvesti firmware
        echo $firmware > /home/pi/monitoring/firmware.txt

	config=$(vcgencmd get_config int)  #isvesti konfiguracija
        echo $config > /home/pi/monitoring/config.txt 
sleep 300
done
