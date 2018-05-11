# Spy Speak
## Games day room atmosphere.
---

## Alarm System
The pysical comand centre has a 12V flashing red light mounted on it. This repo runs a server that allows the alarm to be raised and lowered with HTTP Post requests. The server uses the Raspberry Pis general purpouse input/output interface to drive a simple 12V relay. The relay is wired that drawing the pin low will power the light, and high will turn it off.

The purpouse of this is so that the game can hit the Pi server when the guards are allerted and cause the in-room alarm to go off, added to the immersion that the game is real.

## Timer
The Pi server also hosts an endpoint that displays a countdown time for the game on a webpage. The server uses socket.io to emit updates the time displayed when an endpoint is called. Javascript is used to countdown the timer from the starting value. For example when the game starts the total game time is displayed, and if for example the game finishes early (spy caught, etc) then the timer can be updated accordingly.

## Game speaking to user
Unfortunately the version of UWS that the game uses doesnot support https communications, which means that it could not directly interface with Google cloud platofrm. As a workaround the RPi has an endpoint that simply bounces to Google at the same URI and content. This functionality allows the game to initaiate speaking to the user rather than the voice server needing to poll the game to ask if it wanted to say anything.
