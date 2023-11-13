#
# **************************************************************************
#
# pulse_generator.py                                      (c) Spectrum GmbH
#
# **************************************************************************
#
# Example program for the pulse generator feature on M4i, M4x, M2p and M5i cards.
# Different setups are shown to highlight the capabilities of the pulse
# generator feature.
# This example sets up all pulse generators to create continuous signals
# with various frequencies, high/low characteristics, and offset

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

    lPulseGenEnableMask = 0

    # setup pulse generator 0 (output on X0)
    # generate a continuous signal with the maximum frequency
    card.set(spcm.SPCM_X0_MODE,               spcm.SPCM_XMODE_PULSEGEN) # enable pulse generator output on X0 line

    card.set(spcm.SPC_XIO_PULSEGEN0_MODE,     spcm.SPCM_PULSEGEN_MODE_TRIGGERED)
    card.set(spcm.SPC_XIO_PULSEGEN0_LEN,      2)
    card.set(spcm.SPC_XIO_PULSEGEN0_HIGH,     1) # 50% HIGH, 50% LOW
    card.set(spcm.SPC_XIO_PULSEGEN0_DELAY,    0)
    card.set(spcm.SPC_XIO_PULSEGEN0_LOOPS,    0) # 0: infinite
    card.set(spcm.SPC_XIO_PULSEGEN0_MUX1_SRC, spcm.SPCM_PULSEGEN_MUX1_SRC_UNUSED)
    card.set(spcm.SPC_XIO_PULSEGEN0_MUX2_SRC, spcm.SPCM_PULSEGEN_MUX2_SRC_SOFTWARE) # started by software force command
    lPulseGenEnableMask |= spcm.SPCM_PULSEGEN_ENABLE0 # add pulse generator 0 to enable mask


    # setup pulse generator 1 (output on X1)
    # generate a continuous signal with ~1 MHz, 50% duty cycle
    card.set(spcm.SPCM_X1_MODE,               spcm.SPCM_XMODE_PULSEGEN) # enable pulse generator output on X1 line

    lLenFor1MHz = np.int32 (llPulseGenClock / spcm.MEGA(1))
    card.set(spcm.SPC_XIO_PULSEGEN1_MODE,     spcm.SPCM_PULSEGEN_MODE_TRIGGERED)
    card.set(spcm.SPC_XIO_PULSEGEN1_LEN,      lLenFor1MHz)
    card.set(spcm.SPC_XIO_PULSEGEN1_HIGH,     lLenFor1MHz / 2) # 50% HIGH, 50% LOW
    card.set(spcm.SPC_XIO_PULSEGEN1_DELAY,    0)
    card.set(spcm.SPC_XIO_PULSEGEN1_LOOPS,    0) # 0: infinite
    card.set(spcm.SPC_XIO_PULSEGEN1_MUX1_SRC, spcm.SPCM_PULSEGEN_MUX1_SRC_UNUSED)
    card.set(spcm.SPC_XIO_PULSEGEN1_MUX2_SRC, spcm.SPCM_PULSEGEN_MUX2_SRC_SOFTWARE) # started by software force command
    lPulseGenEnableMask |= spcm.SPCM_PULSEGEN_ENABLE1 # add pulse generator 1 to enable mask


    # setup pulse generator 2 (output on X2)
    # same signal as pulse generator 1, but with a phase shift
    card.set(spcm.SPCM_X2_MODE,               spcm.SPCM_XMODE_PULSEGEN) # enable pulse generator output on X2 line

    card.set(spcm.SPC_XIO_PULSEGEN2_MODE,     spcm.SPCM_PULSEGEN_MODE_TRIGGERED)
    card.set(spcm.SPC_XIO_PULSEGEN2_LEN,      lLenFor1MHz)
    card.set(spcm.SPC_XIO_PULSEGEN2_HIGH,     lLenFor1MHz / 2) # 50% HIGH, 50% LOW
    card.set(spcm.SPC_XIO_PULSEGEN2_DELAY,    lLenFor1MHz / 4) # delay for 1/4 of the period to achieve a "phase shift" by 90°
    card.set(spcm.SPC_XIO_PULSEGEN2_LOOPS,    0) # 0: infinite
    card.set(spcm.SPC_XIO_PULSEGEN2_MUX1_SRC, spcm.SPCM_PULSEGEN_MUX1_SRC_UNUSED)
    card.set(spcm.SPC_XIO_PULSEGEN2_MUX2_SRC, spcm.SPCM_PULSEGEN_MUX2_SRC_SOFTWARE) # started by software force command
    lPulseGenEnableMask |= spcm.SPCM_PULSEGEN_ENABLE2 # add pulse generator 2 to enable mask


    # setup pulse generator 3 (output on X3. Not available on M4i/M4x)
    if (lCardType & spcm.TYP_SERIESMASK) not in [spcm.TYP_M4IEXPSERIES, spcm.TYP_M4XEXPSERIES]:
        card.set(spcm.SPCM_X3_MODE, spcm.SPCM_XMODE_PULSEGEN) # enable pulse generator output on X3 lines

        # generate a continuous signal with ~500 kHz after the first edge on pulse generator 2 occurred, and delay the start for two periods of the 1MHz signal.
        lLenFor500kHz = np.int32(llPulseGenClock / spcm.KILO(500))
        card.set(spcm.SPC_XIO_PULSEGEN3_MODE,     spcm.SPCM_PULSEGEN_MODE_TRIGGERED)
        card.set(spcm.SPC_XIO_PULSEGEN3_LEN,      lLenFor500kHz)
        card.set(spcm.SPC_XIO_PULSEGEN3_HIGH,     9*lLenFor500kHz / 10) # 90% HIGH, 10% LOW
        card.set(spcm.SPC_XIO_PULSEGEN3_DELAY,    2*lLenFor1MHz) # delay for two periods of 1MHz signal
        card.set(spcm.SPC_XIO_PULSEGEN3_LOOPS,    0) # 0: infinite
        card.set(spcm.SPC_XIO_PULSEGEN3_MUX1_SRC, spcm.SPCM_PULSEGEN_MUX1_SRC_UNUSED)
        card.set(spcm.SPC_XIO_PULSEGEN3_MUX2_SRC, spcm.SPCM_PULSEGEN_MUX2_SRC_PULSEGEN2) # started by first edge of pulse generator 2
        lPulseGenEnableMask |= spcm.SPCM_PULSEGEN_ENABLE3 # add pulse generator 3 to enable mask

    # arm the trigger detection for all pulse generators
    card.set(spcm.SPC_XIO_PULSEGEN_ENABLE, lPulseGenEnableMask)

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

