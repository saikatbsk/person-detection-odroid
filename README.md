# Person Detection and Counting on Odroid XU4

This is a very lame readme explaining how to run the code that comes with this very lame repo :P

## How to run this code?

#### 1. Identify Zones
You need to identify the zones first. To identify zones,
1. First, run `python3.6 draw_zone.py -n <name_of_zone>` (replace _<name_of_zone>_ with a valid name i.e. _zoneq_).
2. A wild GUI will appears. Left click and start drawing a polygon. Right click when you are finished.
3. Repeat step _1_ for all the zones you want.

#### 2. Run the Sample OSC Server
Run `python3.6 sample_osc_server.py`.

#### 3. Run the Real Time Person Detection
Open another terminal and run `./test.sh`
