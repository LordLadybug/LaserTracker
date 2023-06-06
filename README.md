# LaserTracker
Laser tracking program that moves camera to keep laser pointer in focus; crude visual encoder for making measurements along a ruler.

- start with 1D and basic servos(already have)
- option for measurement by ruler(look up/down for markings, or triangulate from whatever part of the FOV the camera focuses on the laser); can work in either inches or mm; can also work with 1- or 2-sided or no ruler
- done in either python or c/c++(probably python)
- add autostartup on boot and an issue tracker upon failure to do so, logs active processes and/or any error messages
- tracker should be able to focus on the laser pointer in: 0.1 SECONDS (validate this with the stated framerate of the camera from camera datasheet)

To run:
Can be run in python3 by running MainTracker.py
