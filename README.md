# pi-enigma
A Raspberry Pi Enigma machine for teaching

## Goal
A self-contained machine: keys, lamps, rotors, plugboard. First mostly software, eventually more and more hardware added.

## Status
Version 0.0.0 Initial building of the cipher software

## Planned features

### v1.0.0 (MVP)
- Historically accurate Enigma I cipher: rotors I–V, reflectors B and C,
  ring settings, plugboard, and the double-step of the middle rotor
- 26 mechanical keys with round typewriter-style keycaps
- 26 lamps (one per letter) showing the encrypted letter
- 3 rotor knobs to set starting positions; push + turn to change
  rotor choice, order, and ring settings
- Rotor letter display that steps as you type
- Working 26-jack plugboard with patch cables
- Self-test mode for keys, lamps, and plugboard
- Fully self-contained: starts automatically at power-on,
  no screen, computer, or network needed
- 3D-printed case modelled on the Enigma I

### Future (after v1.0.0)
- Signal path LED panel in the lid: lights the path through plugboard,
  rotors, and reflector
- Built-in screen: animated rotor wiring, tables, and explanations
- Slow mode: the signal moves one stage at a time
- Stepping lights: show when a rotor notch turns the next rotor
- Self-check demo: why a letter never encrypts to itself
- Physical swappable rotors with sensors and motors
- Internal power bank (no power cable)
- Safe on/off switch
- Naval M4 mode (4 rotors)
- Morse code output on a buzzer
- Thermal printer for messages and daily key sheets
- Historical message library
- Letter frequency display
- Bombe and crib demo (how Enigma was broken)
- Teacher mode: hide or lock the settings
- Two-machine classroom exercise
