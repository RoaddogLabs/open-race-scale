### This is the Roaddog Labs fork of Open Race Scale
**It is not synced with the current version deployed that Project and Issues are tracking**
See upstream source at https://github.com/jenkinsracing/open-race-scale/tree/master/software

Current hardware deployment is Raspbian Jesse built for arm7l

Using default user pi code is deployed to ~pi

This release requires dependencies to be built with python3

Change bool value of sim to False  `sim = False` in main.py to deploy on RPi hardware


The software is currently designed in two parts.  
1. Core - The core code runs on the RPi3 and communicates with HX711 to receive weights from the loadcells. It does limited calculations with those weights to give standard weighing information. This data (will be) published to a Bluetooth RFComm channel for clients to read.
2. App - The app code at this time runs a local GUI which instantiates the core code. Bluetooth is currently not implemented, however in the future this code will be reused in two ways: local mode for a GUI running on the same RPi3 that is connected to the loadcells, and client mode where the app will operate as a Bluetooth client on a smart phone.  
  
  
Core Dependencies: 
pybluez

  
App Dependencies: 

kivy
pygame
cython  
  
  
