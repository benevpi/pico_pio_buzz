# pico_pio_buzz

A simple PIO program that outputs a tone based on a number going into it. I've not yet done the maths to work out what number means what note, but it seems to give a nice range over audible tones. A bit buzzy at lower frequencies, but sounds nicer higher up.

Connect headphones between 0 and ground to hear the sound (might be a bit loud, so don't put them on headphones on until you've run it to check). A good idea to add a circa 220 ohm resistor in series. You may be able to get away without this, but don't blame me if you blow up your headphones and/or Pico!

## Extension
* Could build a very simple resistor DAC and output a 2 (or more) bit sound with multiple loops and side(0) side(1) side(2) side(3) side(2) side(1)
* Can also have up to 8 of these running to make a polyphonic sound. Possibly based on button input
