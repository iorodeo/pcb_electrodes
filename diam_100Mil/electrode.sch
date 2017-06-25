EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:eletrode
LIBS:electrode-cache
EELAYER 27 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date "25 jun 2017"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L CONN_3 K1
U 1 1 595009A1
P 2950 2400
F 0 "K1" V 2900 2400 50  0000 C CNN
F 1 "CONN_3" V 3000 2400 40  0000 C CNN
F 2 "" H 2950 2400 60  0000 C CNN
F 3 "" H 2950 2400 60  0000 C CNN
	1    2950 2400
	-1   0    0    1   
$EndComp
$Comp
L ELETRODE E1
U 1 1 59500EF0
P 4300 2400
F 0 "E1" H 4350 2150 60  0000 C CNN
F 1 "ELETRODE" H 4350 2650 60  0000 C CNN
F 2 "~" H 4300 2350 60  0000 C CNN
F 3 "~" H 4300 2350 60  0000 C CNN
	1    4300 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	3300 2500 3700 2500
Wire Wire Line
	3700 2300 3550 2300
Wire Wire Line
	3550 2300 3550 2400
Wire Wire Line
	3550 2400 3300 2400
Wire Wire Line
	3300 2300 3450 2300
Wire Wire Line
	3450 2300 3450 2450
Wire Wire Line
	3450 2450 3600 2450
Wire Wire Line
	3600 2450 3600 2400
Wire Wire Line
	3600 2400 3700 2400
Text Label 3300 2300 0    60   ~ 0
WRK
Text Label 3300 2400 0    60   ~ 0
REF
Text Label 3300 2500 0    60   ~ 0
CTR
$EndSCHEMATC
