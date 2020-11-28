from asciimatics.effects import Print

from asciimatics.renderers import BarChart, FigletText, SpeechBubble, Box

from asciimatics.scene import Scene

from asciimatics.screen import Screen

from asciimatics.exceptions import ResizeScreenError

import os

import sys

import math

import time

accel_x = open('/sys/bus/iio/devices/iio:device2/in_accel_x_raw', 'r')

accel_y = open('/sys/bus/iio/devices/iio:device2/in_accel_y_raw', 'r')

accel_z = open('/sys/bus/iio/devices/iio:device2/in_accel_z_raw', 'r')

gyro_x = open('/sys/bus/iio/devices/iio:device2/in_anglvel_x_raw', 'r')

gyro_y = open('/sys/bus/iio/devices/iio:device2/in_anglvel_y_raw', 'r')

gyro_z = open('/sys/bus/iio/devices/iio:device2/in_anglvel_z_raw', 'r')

mag_x = open('/sys/bus/iio/devices/iio:device3/in_magn_x_raw', 'r')

mag_y = open('/sys/bus/iio/devices/iio:device3/in_magn_y_raw', 'r')

mag_z = open('/sys/bus/iio/devices/iio:device3/in_magn_z_raw', 'r')

def _speak(screen, text, pos, start):

  return Print(

    screen,

    SpeechBubble(text, None, uni=screen.unicode_aware),

    x=pos[0] + 4, y=pos[1] - 4,

    colour=Screen.COLOUR_WHITE,

    clear=True,

    start_frame=start,

    stop_frame=start+50)

def accelx():

  accel_x.seek(0)

  accel = int(accel_x.readline())

  accel = accel/16000 + 1

  return accel if accel < 2 else 2

def accely():

  accel_y.seek(0)

  accel = int(accel_y.readline())

  accel = accel/16000 + 1

  return accel if accel < 2 else 2

def accelz():

  accel_z.seek(0)

  accel = int(accel_z.readline())

  accel = accel/16000 + 1

  return accel if accel < 2 else 2

def gyrox():

  gyro_x.seek(0)

  gyro = int(gyro_x.readline())

  gyro = gyro/300 + 1

  return gyro if gyro < 2 else 2

def gyroy():

  gyro_y.seek(0)

  gyro = int(gyro_y.readline())

  gyro = gyro/300 + 1

  return gyro if gyro < 2 else 2

def gyroz():

  gyro_z.seek(0)

  gyro = int(gyro_z.readline())

  gyro = gyro/300 + 1

  return gyro if gyro < 2 else 2

def magx():

  mag_x.seek(0)

  mag = int(mag_x.readline())

  mag = mag/100 + 1

  return mag if mag < 2 else 2

def magy():

  mag_y.seek(0)

  mag = int(mag_y.readline())

  mag = mag/100 + 1

  return mag if mag < 2 else 2

def magz():

  mag_z.seek(0)

  mag = int(mag_z.readline())

  mag = mag/100 + 1

  return mag if mag < 2 else 2

def demo(screen):

    scenes = []

    effects = [

        Print(screen,

              BarChart(

                  10, 40,

                  [accelx, accely, accelz],

                  colour=[c for c in range(1, 4)],

                  bg=[c for c in range(1, 4)],

                  scale=2.0,

                  axes=BarChart.X_AXIS,

                  intervals=0.5,

                  labels=True,

                  border=False),

              x=0, y=0, transparent=False, speed=2),

          _speak(screen, "Accelerometer", (0, 14), 0),

          Print(screen,

              BarChart(

                  10, 40,

                  [gyrox, gyroy, gyroz],

                  colour=[c for c in range(7, 10)],

                  bg=[c for c in range(7, 10)],

                  scale=2.0,

                  axes=BarChart.X_AXIS,

                  intervals=0.5,

                  labels=True,

                  border=False),

              x=0, y=15, transparent=False, speed=2),

          _speak(screen, "Gyroscope", (0, 29), 0),

          Print(screen,

              BarChart(

                  10, 40,

                  [magx, magy, magz],

                  colour=[c for c in range(4, 8)],

                  bg=[c for c in range(4, 8)],

                  scale=2.0,

                  axes=BarChart.X_AXIS,

                  intervals=0.5,

                  labels=True,

                  border=False),

              x=44, y=0, transparent=False, speed=2),

          _speak(screen, "Magnetometer", (50, 14), 0),

    ]

    scenes.append(Scene(effects, -1))

    screen.play(scenes, stop_on_resize=True)



while True:

    try:

        Screen.wrapper(demo)

        sys.exit(0)

    except ResizeScreenError:

        pass
