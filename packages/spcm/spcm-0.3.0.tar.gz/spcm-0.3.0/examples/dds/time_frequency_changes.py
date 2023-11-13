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
    card.trg_src(spcm.SPCM_DDS_TRG_SRC_TIMER)
    card.trg_timer(3.0)
    card.amp(0, 0.7)
    card.freq(0, 100e6) # 100 MHz
    card.exec_at_trg()
    #-----------------------------------------------------------------
    card.freq(0, 200e6) # 200 MHz
    card.exec_at_trg()
    #-----------------------------------------------------------------
    card.freq(0, 300e6) # 300 MHz
    card.exec_at_trg()
    #-----------------------------------------------------------------
    card.write_to_card()

    ## Start the card
    card.start(spcm.M2CMD_CARD_WAITREADY, spcm.M2CMD_CARD_ENABLETRIGGER)
