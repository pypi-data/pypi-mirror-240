"""EXAMPLE 1 - Multiple static carriers

This example shows the DDS functionality with 20 carriers
with individual but fixed frequencies on one channel. 
"""

import sys
import spcm
import numpy as np

## Load the card
with spcm.DDS('/dev/spcm0') as card:
    if not card: sys.exit(-1)
    print("Driver version: {major}.{minor}.{build}".format(**card.drv_version()))
    
    ## Setup the card
    num_channels = 2
    card.set(spcm.SPC_CHENABLE, (0x1 << num_channels) - 1) # enable channels
    for channel_index in range(num_channels):
        card.out_enable(channel_index, True)
        card.out_amp(channel_index, 1000)
    card.write_to_card()
    
    ## Setup DDS
    card.dds_reset()

    ## Start the test
    num_freq      =  20
    start_freq_Hz =  99e6 #  99 MHz
    end_freq_Hz   = 101e6 # 101 MHz
    freq_list = np.linspace(start_freq_Hz, end_freq_Hz, num_freq)
    for i, freq in enumerate(freq_list):
        amp = 0.4/num_freq
        act_amp = card.amp(i, amp)
        act_freq = card.freq(i, freq)
        print("channel {}:".format(i), end=" | ")
        print("amp diff: {:.8E}".format(act_amp - amp), end=" | ")
        print("freq diff: {:.8E}".format(act_freq - freq))
    card.exec_at_trg()
    card.write_to_card()

    ## Start the card
    card.start(spcm.M2CMD_CARD_WAITREADY, spcm.M2CMD_CARD_ENABLETRIGGER)
