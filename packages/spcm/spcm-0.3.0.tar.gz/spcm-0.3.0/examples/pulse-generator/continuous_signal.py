#
# **************************************************************************
#
# 1_continuous_signal.py                                   (c) Spectrum GmbH
#
# **************************************************************************
#
# Example program for the pulse generator feature on M4i, M4x, M2p and M5i cards.
# Different setups are shown to highlight the capabilities of the pulse
# generator feature.
# This example sets up the pulse generator for X0 to create a continuous signal
# The setup of the card for acquisition/replay is shown in the other examples.

# Documentation for the API as well as a detailed description of the hardware
# can be found in the manual for each device which can be found on our website:
# https:#www.spectrum-instrumentation.com/en/downloads

# Further information can be found online in the Knowledge Base:
# https:#www.spectrum-instrumentation.com/en/knowledge-base-overview
#
# **************************************************************************
#

import spcm
import sys
import numpy as np


# open card
# uncomment the first line and replace the IP address to use remote
# cards like in a NETBOX
# with spcm.Card('TCPIP::192.168.1.10::inst0::INSTR') as card:
with spcm.Card('/dev/spcm0') as card:
    if not card: sys.exit(-1)
    print("Driver version: {major}.{minor}.{build}".format(**card.drv_version()))

    # read type, function and sn and check for A/D card
    lCardType = card.get(spcm.SPC_PCITYP)
    lSerialNumber = card.sn()
    lFncType = card.get(spcm.SPC_FNCTYPE)
    sCardName = card.product_name()
    
    # pulse generators are not available on M2i and M3i cards
    print("Found: {0} sn {1:05d}\n".format(sCardName, lSerialNumber))
    if lCardType & spcm.TYP_SERIESMASK in [spcm.TYP_M2ISERIES, spcm.TYP_M2IEXPSERIES, spcm.TYP_M3ISERIES, spcm.TYP_M3IEXPSERIES]:
        print("ERROR: pulse generators not available on this card\n")
        sys.exit(-1)

    # on newer cards the availability depends on a (paid) feature
    # so we check if this card has the pulse generator feature installed
    lFeatures = card.get(spcm.SPC_PCIEXTFEATURES)
    if not (lFeatures & spcm.SPCM_FEAT_EXTFW_PULSEGEN):
        print("ERROR: pulse generators not supported by this card\n")
        sys.exit(-1)

    # first we set up the channel selection and the clock
    # for this example we enable only one channel to be able to use max sampling rate on all card types
    # ! changing the card settings while pulse generators are active causes a stop and restart of the pulse generators
    card.set(spcm.SPC_CHENABLE, spcm.CHANNEL0)
    llMaxSR = card.get(spcm.SPC_PCISAMPLERATE)
    card.set(spcm.SPC_SAMPLERATE, llMaxSR)

    # start the pulse generator
    # uncomment one of the following function calls. Each will set up the pulse generators differently.
    llPulseGenClock = card.get(spcm.SPC_XIO_PULSEGEN_CLOCK)

    # enable pulse generator output on XIO lines
    card.set(spcm.SPCM_X0_MODE, spcm.SPCM_XMODE_PULSEGEN)

    # setup pulse generator 0 (output on X0)
    # generate a continuous signal with 1 MHz
    lLenFor1MHz = np.int32(llPulseGenClock / spcm.MEGA(1))
    card.set(spcm.SPC_XIO_PULSEGEN0_MODE,     spcm.SPCM_PULSEGEN_MODE_TRIGGERED)
    card.set(spcm.SPC_XIO_PULSEGEN0_LEN,      lLenFor1MHz)
    card.set(spcm.SPC_XIO_PULSEGEN0_HIGH,     lLenFor1MHz / 2) # 50% HIGH, 50% LOW
    card.set(spcm.SPC_XIO_PULSEGEN0_DELAY,    0)
    card.set(spcm.SPC_XIO_PULSEGEN0_LOOPS,    0) # 0: infinite
    card.set(spcm.SPC_XIO_PULSEGEN0_MUX1_SRC, spcm.SPCM_PULSEGEN_MUX1_SRC_UNUSED)
    card.set(spcm.SPC_XIO_PULSEGEN0_MUX2_SRC, spcm.SPCM_PULSEGEN_MUX2_SRC_SOFTWARE) # started by software force command

    # arm the trigger detection for all pulse generators
    card.set(spcm.SPC_XIO_PULSEGEN_ENABLE, spcm.SPCM_PULSEGEN_ENABLE0)

    # write the settings to the card
    # update the clock section to generate the programmed frequencies (SPC_SAMPLERATE)
    # and write the pulse generator settings
    card.write_setup()

    # start all pulse generators that wait for a software command
    card.set(spcm.SPC_XIO_PULSEGEN_COMMAND, spcm.SPCM_PULSEGEN_CMD_FORCE)

    # wait until user presses a key
    input("Press a key to stop the pulse generator(s) ")

    # stop the pulse generators
    card.set(spcm.SPC_XIO_PULSEGEN_ENABLE, 0)
    card.cmd(spcm.M2CMD_CARD_WRITESETUP)

