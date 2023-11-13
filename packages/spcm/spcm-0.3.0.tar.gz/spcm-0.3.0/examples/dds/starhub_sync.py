"""EXAMPLE 9 - Output a single carrier on two cards synced through a StarHub

This example shows the DDS functionality with 1 carrier
with a fixed frequency and . 
"""

import sys
import spcm
import numpy as np

## Load the cards
card_identifiers = ["/dev/spcm0", "/dev/spcm1"]
sync_identifier  = "sync0"

# open cards and sync
with spcm.CardStack(card_identifiers=card_identifiers, sync_identifier=sync_identifier, card_class=spcm.DDS) as stack:
    if not stack: sys.exit(-1)

    for card in stack.cards:
        ## Setup the card
        card.set(spcm.SPC_CHENABLE, 1) # enable channel 0
        card.set(spcm.SPC_CLOCKMODE, spcm.SPC_CM_INTPLL)
        card.set(spcm.SPCM_X0_MODE, spcm.SPCM_XMODE_TRIGOUT)

        card.out_enable(0, True)
        card.out_amp(0, 500)
        card.write_setup()
        
        ## Setup DDS
        card.dds_reset()

        ## Start the test
        card.amp(0, 0.7)
        card.freq(0, 100.0e6)
        card.trg_src(spcm.SPCM_DDS_TRG_SRC_NONE)
        card.exec_at_trg()
        card.write_to_card()
    
    # setup star-hub
    nCardCount = len(card_identifiers)
    stack.sync.enable_mask((1 << nCardCount) - 1)

    stack.sync.start(spcm.M2CMD_CARD_ENABLETRIGGER)
    
    stack.cards[0].cmd(spcm.M2CMD_CARD_FORCETRIGGER)

    ## Start the card
    card.start(spcm.M2CMD_CARD_WAITREADY, spcm.M2CMD_CARD_ENABLETRIGGER)
