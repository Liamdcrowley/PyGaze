import random
import numpy
from constants import *
from pygaze import libtime, settings
from pygaze.libscreen import Display, Screen
from pygaze.eyetracker import EyeTracker
from pygaze.libinput import Keyboard
from pygaze.liblog import Logfile
from pygaze.libgazecon import FRL, MRL
import pygaze

# timing and initialization
libtime.expstart()

# visuals
disp = Display()
imageScr = Screen()
stimScr = Screen()
scr = Screen()
maskScr = Screen()

# eye tracking
tracker = EyeTracker(disp)
frl = FRL(pos='center', dist=125, size=200)
mrl = MRL(pos='center', dist=125, size=200)

# input collection and storage
kb = Keyboard(timeout=None)
log = Logfile()
log.write(["trialnr", "Trialype", "correct", "trialstart", "trialend", "duration", "image"])

# run trials
tracker.calibrate()

maskCount = 0
windowCount = 0
fullCount = 0
# run experiment
for trialnr in range(0,len(IMAGES)):
	# decide on trial type
	if (maskCount < 3 and fullCount < 3 and windowCount < 3):
		trialType = random.choice(['mask', 'window', 'full'])
	elif (maskCount < 3 and fullCount < 3 and windowCount >= 3):
		trialType = random.choice(['mask', 'full'])
	elif (maskCount < 3 and fullCount >= 3 and windowCount >= 3):
		trialType = 'mask'
	elif (maskCount >= 3 and fullCount < 3 and windowCount < 3):
		trialType = random.choice(['window', 'full'])
	elif (maskCount >=3 and fullCount >=3 and windowCount < 3):
		trialType = 'window'
	elif (maskCount < 3 and fullCount >= 3 and windowCount < 3):
		trialType = random.choice(['window', 'mask'])
	elif (maskCount >=3 and fullCount < 3 and windowCount >=3):
		trialType = 'full'
	else:
		break
	trialMatch = random.choice(['same', 'different'])
	if (trialType == 'mask'):
		# blank display
		disp.fill()
		disp.show()
		libtime.pause(1000)
		# start recording eye movements
		tracker.drift_correction()
		tracker.start_recording()
		tracker.status_msg("trial %d" % trialnr)
		tracker.log("start trial %d" % trialnr)
		# prepare stimulus
		scr.clear()
		scr.draw_image(IMAGES[trialnr])
		disp.fill(screen=scr)
		disp.show()
		libtime.pause(1000)
		# blank display
		disp.fill()
		disp.show()
		libtime.pause(1000)
		# present stimulus
		response = None
		scr.clear(colour=(127,127,127))
		if trialMatch == 'same':
			imageScr.draw_image(IMAGES[trialnr])
		elif trialMatch == 'different':
			imageScr.draw_image(FOILIMAGES[trialnr])
		else:
			break
		trialstart = libtime.get_time()
		while not response:
			key, presstime = kb.get_key(timeout=1)
			if key:
				if key == 'escape':
					break
				if (key == 'y' and trialMatch == 'same'):
					scr.clear()
					scr.draw_text(text='YOU ARE RIGHT THEY ARE SAME')
					disp.fill(screen=scr)
					disp.show()
					correct = True
					libtime.pause(1000)
					break
				if (key == 'y' and trialMatch == 'different'):
					scr.clear()
					scr.draw_text(text='YOU ARE WRONG THEY ARE DIFFERENT')
					disp.fill(screen=scr)
					disp.show()
					correct = False
					libtime.pause(1000)
					break
				if (key == 'n' and trialMatch == 'same'):
					scr.clear()
					scr.draw_text(text='YOU ARE WRONG THEY ARE SAME')
					disp.fill(screen=scr)
					disp.show()
					correct = False
					libtime.pause(1000)
					break
				if (key == 'n' and trialMatch == 'different'):
					scr.clear()
					scr.draw_text(text='YOU ARE RIGHT THEY ARE DIFFERENT')
					disp.fill(screen=scr)
					disp.show()
					correct = True
					libtime.pause(1000)
					break
			else:
				pass
			mrl = MRL(pos='center', dist=125, size=200)
			gazepos = tracker.sample()
			mrl.mrlupdate(disp, scr, gazepos, imageScr)
		libtime.pause(1000)
		maskCount = maskCount + 1
		# stop tracking and process input
		tracker.stop_recording()
		tracker.log("stop trial %d" % trialnr)
		log.write([trialnr, trialType, correct, trialstart, presstime, presstime - trialstart, IMAGES[trialnr]])
	elif (trialType == 'window'):
		# blank display
		disp.fill()
		disp.show()
		libtime.pause(1000)
		# start recording eye movements
		tracker.drift_correction()
		tracker.start_recording()
		tracker.status_msg("trial %d" % trialnr)
		tracker.log("start trial %d" % trialnr)
		# prepare stimulus
		scr.clear()
		scr.draw_image(IMAGES[trialnr])
		disp.fill(screen=scr)
		disp.show()
		libtime.pause(1000)
		# blank display
		disp.fill()
		disp.show()
		libtime.pause(1000)
		# present stimulus
		scr.clear()
		if trialMatch == 'same':
			scr.draw_image(IMAGES[trialnr])
		else:
			scr.draw_image(FOILIMAGES[trialnr])
		response = None
		trialstart = libtime.get_time()
		while not response:
			key, presstime = kb.get_key(timeout=1)
			if key:
				if key == 'escape':
					break
				if (key == 'y' and trialMatch == 'same'):
					scr.clear()
					scr.draw_text(text='YOU ARE RIGHT THEY ARE SAME')
					disp.fill(screen=scr)
					disp.show()
					correct = True
					libtime.pause(1000)
					break
				if (key == 'y' and trialMatch == 'different'):
					scr.clear()
					scr.draw_text(text='YOU ARE WRONG THEY ARE DIFFERENT')
					disp.fill(screen=scr)
					disp.show()
					correct = False
					libtime.pause(1000)
					break
				if (key == 'n' and trialMatch == 'same'):
					scr.clear()
					scr.draw_text(text='YOU ARE WRONG THEY ARE SAME')
					disp.fill(screen=scr)
					disp.show()
					correct = False
					libtime.pause(1000)
					break
				if (key == 'n' and trialMatch == 'different'):
					scr.clear()
					scr.draw_text(text='YOU ARE RIGHT THEY ARE DIFFERENT')
					disp.fill(screen=scr)
					disp.show()
					correct = True
					libtime.pause(1000)
					break
				else:
					pass
			gazepos = tracker.sample()
			frl.update(disp, scr, gazepos)
		libtime.pause(1000)
		windowCount = windowCount + 1
		# stop tracking and process input
		tracker.stop_recording()
		tracker.log("stop trial %d" % trialnr)
		log.write([trialnr, trialType, correct, trialstart, presstime, presstime-trialstart, IMAGES[trialnr]])
	elif (trialType == 'full'):
		# blank display
		disp.fill()
		disp.show()
		libtime.pause(1000)
		# start recording eye movements
		tracker.drift_correction()
		tracker.start_recording()
		tracker.status_msg("trial %d" % trialnr)
		tracker.log("start trial %d" % trialnr)
		# prepare stimulus
		scr.clear()
		scr.draw_image(IMAGES[trialnr])
		disp.fill(screen=scr)
		disp.show()
		libtime.pause(1000)
		# blank display
		disp.fill()
		disp.show()
		libtime.pause(1000)
		# present stimulus
		scr.clear()
		if trialMatch == 'same':
			scr.draw_image(IMAGES[trialnr])
		else:
			scr.draw_image(FOILIMAGES[trialnr])
		response = None
		disp.fill(screen=scr)
		disp.show()
		trialstart = libtime.get_time()
		while not response:
			key, presstime = kb.get_key(timeout=1)
			if key:
				if key == 'escape':
					break
				if (key == 'y' and trialMatch == 'same'):
					scr.clear()
					scr.draw_text(text='YOU ARE RIGHT THEY ARE SAME')
					disp.fill(screen=scr)
					disp.show()
					correct = True
					libtime.pause(1000)
					break
				if (key == 'y' and trialMatch == 'different'):
					scr.clear()
					scr.draw_text(text='YOU ARE WRONG THEY ARE DIFFERENT')
					disp.fill(screen=scr)
					disp.show()
					correct = False
					libtime.pause(1000)
					break
				if (key == 'n' and trialMatch == 'same'):
					scr.clear()
					scr.draw_text(text='YOU ARE WRONG THEY ARE SAME')
					disp.fill(screen=scr)
					disp.show()
					correct = False
					libtime.pause(1000)
					break
				if (key == 'n' and trialMatch == 'different'):
					scr.clear()
					scr.draw_text(text='YOU ARE RIGHT THEY ARE DIFFERENT')
					disp.fill(screen=scr)
					disp.show()
					correct = True
					libtime.pause(1000)
					break
		libtime.pause(1000)
		fullCount = fullCount + 1
		# stop tracking and process input
		tracker.stop_recording()
		tracker.log("stop trial %d" % trialnr)
		log.write([trialnr, trialType, correct, trialstart, presstime, presstime - trialstart, IMAGES[trialnr]])



# close experiment
log.close()
tracker.close()
disp.close()
libtime.expend()
