"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

from get_polygons import get_polygons

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port", type=int, default=5005, help="The port to listen on")
  parser.add_argument("--zone_files_dir", default="zone_files", help="zone files directory")
  args = parser.parse_args()

  zones = [key for key in get_polygons(args.zone_files_dir)]

  dispatcher = dispatcher.Dispatcher()
  for zone in zones:
      dispatcher.map("/trigger/"+zone, print)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
