# open-race-scale
# 
This is the Roaddog Labs fork of Open Race Scale, the open hardware
race car scale from Andrew Jenkins at
https://github.com/jenkinsracing/open-race-scale used under OSHWA and
LGPL 3.0 license.  [Original README.md] (./orig_README.md)

This fork deals with hardware implementation, hardware packaging and
PCB/PCBA design and fabrication.  This fork uses the software/firmware
from the upstream fork.  Please issue software/firmware pull requests to
the upstream repo.  Pull requests for hardware implementation in this
fork are more than welcome.

The `electrical` dir contains circuit designs and PCB/PCBA info.  It
includes the reference design from the upstream master that uses Chengbo HX711 carriers, a Pi Zero W
based control board with integrated HX711 load cell amps (no carriers) and Pi Hat design using Sparkfun HX711 formfactor carriers.

The `mechanical` dir contains a reference scale pad design and enclosure designs for the various controller boards.


Original designs from Roaddog Labs Ltd are released per the Open Source
Hardware Association guidelines for open source hardware at
http://www.oshwa.org/definition/.

Material specific to the components and documentation that is not
derived from other sources are released under the Creative Commons
Attribution 4.0 International license.