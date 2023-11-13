"""EXAMPLE 0 - Single static carrier

This example shows the DDS functionality with 1 carrier
with a fixed frequency and . 
"""

import sys
import spcm
import numpy as np

## Load the card
with spcm.DDS('/dev/spcm0') as card:
    if not card: sys.exit(-1)
    print("Driver version: {major}.{minor}.{build}".format(**card.drv_version()))
    
    ## Setup the card
    card.set(spcm.SPC_CHENABLE, 1) # enable channel 0
    card.out_enable(0, True)
    card.out_amp(0, 1000)
    card.write_to_card()
    
    ## Setup DDS
    card.dds_reset()

    ## Start the test
    amp = 0.4
    freq = 100e6 # in Hz
    act_amp = card.amp(0, amp)
    act_freq = card.freq(0, freq)
    print("actual amplitude: {:.8E}".format(act_amp), end=" | ")
    print("actual frequency: {:.8E}".format(act_freq))
    card.exec_at_trg()
    card.write_to_card()

    ## Start the card
    card.start(spcm.M2CMD_CARD_WAITREADY, spcm.M2CMD_CARD_ENABLETRIGGER)
