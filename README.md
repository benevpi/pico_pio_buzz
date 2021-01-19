# pico_pio_buzz

A simple PIO program that outputs a tone based on a number going into it. I've not yet done the maths to work out what number means what note, but it seems to give a nice range over audible tones. A bit buzzy at lower frequencies, but sounds nicer higher up.

![Pico_pio_buzz in action](https://github.com/benevpi/pico_pio_buzz/blob/main/IMG_20210119_132557768.jpg)


Connect headphones between 0 and ground to hear the sound (might be a bit loud, so don't put them on headphones on until you've run it to check). A good idea to add a circa 220 ohm resistor in series. You may be able to get away without this, but don't blame me if you blow up your headphones and/or Pico!

## files
There are three files here.
* pio_buzz is an all-in-one file that you can upload to your Pico and it will run.
* PIOBeep is a library that you can use to build your own beepy programs. The simplest way to use this is with:
```
>>> import PIOBeep
>>> beeper = PIOBeep.PIOBeep(0,0)
>>> beeper.play_pitch(10,1,400)
```
* PIOBuzz birthday is happy birthday played using the library.

## values vs. Pitchs
The PIO program plays a 'value' which is a number between 0 and 5000 (adjustable if you want to). You can either precalculate these using the calc_value(hertz) method, and then play them using play_value, or you can calculate them on the fly using play_pitch which takes an argument in Hz. The latter adds a little more on-the-hoof overhead, but it shouldn't be too significant unless you're trying to get super-fine timings.

**play_value(note_len, pause_len, value)** plays the value for note_len seconds followed by a pause of pause_len
**play_pitch(note_len, pause_len, hertz)** plays the pitch hertz for note_len followed by a pause of pause_len

## Extension
* Could build a very simple resistor DAC and output a 2 (or more) bit sound with multiple loops and side(0) side(1) side(2) side(3) side(2) side(1)
* Can also have up to 8 of these running to make a polyphonic sound. Possibly based on button input
