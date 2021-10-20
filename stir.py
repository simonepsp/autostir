# -*- coding: utf-8 -*-
#!/usr/bin/python

# Project name: AutoStir for FormLabs 1+ (OpenFL FW)
# Written by Simonepsp (2018)

from OpenFL import Printer, FLP
import sys
import time
import os

# CONFIG
INIT = True  # Will init printer and then move to home pos
TOP_BOTTOM_STEPS = -73500
SPEED = 7000

# STIR
STIR_STEPS = 1850
STIR_SPEED = 1200  # Steps / Second
STIR_N = 10  # How many stirs movement will be done

# init printer
p = Printer.Printer()

# Clear screen
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('\nAUTOSTIR -- V1\n')

if p.get_machine_information():
    print('Printer ONLINE')
else:
    sys.exit('Printer OFFLINE :|')

if INIT:
    # Move to home pos
    print('Initializing...')
    p.initialize()

    print('Moving to bottom...')
    # Move to bottom pos
    p.move_z(TOP_BOTTOM_STEPS, SPEED)
else:
    print('-- Will not init printer --')

print('Stirring resin')

# Stir
for i in range(0, STIR_N):
    print ('... (%d)' % (i + 1))
    p.move_z(STIR_STEPS, STIR_SPEED)
    p.move_z(-STIR_STEPS, STIR_SPEED)

    # Sleep between movements
    time.sleep(0.25)

if INIT:
    print ('DONE. Moving back to HOME pos\n')
    # p.move_z(-TOP_BOTTOM_STEPS, SPEED)
    p.initialize()
