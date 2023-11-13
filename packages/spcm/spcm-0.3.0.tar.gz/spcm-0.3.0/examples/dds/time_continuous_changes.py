"""EXAMPLE 4 - Continuous changes

Use one carrier to jump between different frequencies that are send through the FIFO
"""

import sys
import spcm
import numpy as np
import time

import psutil
import os

# Set the highest process priority to the Python process, to enable highest possible command streaming
p = psutil.Process(os.getpid())
p.nice(psutil.REALTIME_PRIORITY_CLASS)

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

    ## Start the DDS test
    num_freq      = 100
    start_freq_Hz =  85.0e6 #  85 MHz
    end_freq_Hz   = 115.0e6 # 115 MHz
    
    freq_list = np.linspace(start_freq_Hz, end_freq_Hz, num_freq)

    # STEP 0 - Initialize frequencies
    period_s = 1.0 # seconds
    card.trg_src(spcm.SPCM_DDS_TRG_SRC_TIMER)
    card.trg_timer(period_s)
    card.amp(0, 0.45)
    card.freq(0, freq_list[0])
    card.exec_at_trg()
    card.write_to_card()
    
    # STEP 1a - Pre-fill Buffer
    period_s = 1000e-6 # 1 ms
    card.trg_timer(period_s)
    dds_fill_max = card.get(spcm.SPC_DDS_QUEUE_CMD_MAX)
    fill_number = int(dds_fill_max / 4)
    for column in range(fill_number):
        frequency = freq_list[column % num_freq]
        card.freq(0, frequency)
        card.exec_at_trg()
    card.write_to_card()

    ## Start the card
    card.start(spcm.M2CMD_CARD_ENABLETRIGGER)

    # STEP 1b - Streaming data points
    dds_fill_count = card.get(spcm.SPC_DDS_QUEUE_CMD_COUNT)
    dds_fill_check = dds_fill_max - fill_number
    while True: # infinitely long streaming
        while True:
            dds_fill_count = card.get(spcm.SPC_DDS_QUEUE_CMD_COUNT)
            if dds_fill_count < dds_fill_check: break
        for column in range(fill_number):
            frequency = freq_list[column % num_freq]
            card.freq(0, frequency)
            card.exec_at_trg()
        card.write_to_card()
        dds_status = card.get(spcm.SPC_DDS_STATUS)
        if dds_status & spcm.SPCM_DDS_STAT_QUEUE_UNDERRUN:
            break

    print("ERROR: Buffer underrun")