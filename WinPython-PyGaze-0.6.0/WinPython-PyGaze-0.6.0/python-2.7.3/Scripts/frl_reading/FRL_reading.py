import random
import numpy
from constants import *
from pygaze import libtime
from pygaze.libscreen import Display, Screen
from pygaze.eyetracker import EyeTracker
from pygaze.libinput import Keyboard
from pygaze.liblog import Logfile
from pygaze.libgazecon import FRL

# timing and initialization
libtime.expstart()

# visuals
disp = Display()
scr = Screen()

# eye tracking
tracker = EyeTracker(disp)
frl = FRL(pos='center', dist=125, size=200)

# input collection and storage
kb = Keyboard(keylist=['escape','space'], timeout=None)
log = Logfile()
log.write(["gazepos", "trialnr", "trialstart", "trialend", "duration", "image"])

# run trials
tracker.calibrate()

# run experiment
for trialnr in range(0,1):
	#trialType = random.choice(['mask', 'window', 'full'])
	trialType = 'mask'
	maskCount = 0
	windowCount = 0
	fullCount = 0
	if (trialType == 'window' and maskCount < 3):
		# blank display
		disp.fill()
		disp.show()
		libtime.pause(1000)
		# prepare stimulus
		scr.clear()
		scr.draw_image(IMAGES[trialnr])
		disp.fill(screen=scr)
		disp.show()
		libtime.pause(1000)
		# start recording eye movements
		tracker.drift_correction()
		tracker.start_recording()
		tracker.status_msg("trial %d" % trialnr)
		tracker.log("start trial %d" % trialnr)
		# present stimulus
		response = None
		trialstart = libtime.get_time()
		while not response:
			frl = FRL(pos='center', dist=125, size=200)
			gazepos = tracker.sample()
			frl.update(disp, scr, gazepos)
			response, presstime = kb.get_key(timeout=1)
		scr.draw_image(IMAGES[trialnr])
		frl = FRL(pos='center', dist=125, size=200000)
		frl.update(disp, scr, gazepos)
		libtime.pause(1000)
		windowCount = windowCount + 1
		# stop tracking and process input
		tracker.stop_recording()
		tracker.log("stop trial %d" % trialnr)
		log.write([gazepos, trialnr, trialstart, presstime, presstime - trialstart, IMAGES[trialnr]])
	elif (trialType == 'mask' and windowCount < 3):
		# blank display
		disp.fill()
		disp.show()
		libtime.pause(1000)
		# prepare stimulus
		scr.clear()
		scr.draw_image(IMAGES[trialnr])
		disp.fill(screen=scr)
		disp.show()
		libtime.pause(1000)
		# start recording eye movements
		tracker.drift_correction()
		tracker.start_recording()
		tracker.status_msg("trial %d" % trialnr)
		tracker.log("start trial %d" % trialnr)
		# present stimulus
		response = None
		trialstart = libtime.get_time()
		while not response:
			scr.clear()
			scr.draw_image(IMAGES[trialnr])
			gazepos = tracker.sample()
			scr.draw_circle(pos=gazepos, r=100, fill=True, colour=(127, 127, 127))
			disp.fill(screen=scr)
			disp.show()
			response, presstime = kb.get_key(timeout=1)
		libtime.pause(1000)
		maskCount = maskCount + 1
		# stop tracking and process input
		tracker.stop_recording()
		tracker.log("stop trial %d" % trialnr)
		log.write([gazepos, trialnr, trialstart, presstime, presstime-trialstart, IMAGES[trialnr]])
	elif (trialType == 'full'):
		# blank display
		disp.fill()
		disp.show()
		libtime.pause(1000)
		# prepare stimulus
		scr.clear()
		scr.draw_image(IMAGES[trialnr])
		disp.fill(screen=scr)
		disp.show()
		libtime.pause(1000)
		# start recording eye movements
		tracker.drift_correction()
		tracker.start_recording()
		tracker.status_msg("trial %d" % trialnr)
		tracker.log("start trial %d" % trialnr)
		# present stimulus
		response = None
		trialstart = libtime.get_time()
		while not response:
			gazepos = tracker.sample()
			scr.clear()
			scr.draw_image(IMAGES[trialnr])
			disp.fill(screen=scr)
			disp.show()
			response, presstime = kb.get_key(timeout=1)
		libtime.pause(1000)
		fullCount = fullCount + 1
		# stop tracking and process input
		tracker.stop_recording()
		tracker.log("stop trial %d" % trialnr)
		log.write([gazepos, trialnr, trialstart, presstime, presstime - trialstart, IMAGES[trialnr]])

# close experiment
log.close()
tracker.close()
disp.close()
libtime.expend()
