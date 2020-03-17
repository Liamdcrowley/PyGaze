import os.path

# MAIN
DUMMYMODE = False # False for connected eye tracker, True for dummy mode (using mouse or joystick)
LOGFILENAME = input("Participant name: ") # logfilename, without path

# DIRECTORY
DIR = os.path.split(os.path.abspath(__file__))[0]
DATADIR = os.path.join(DIR, 'data')
LOGFILE = os.path.join(DATADIR, LOGFILENAME) # .txt; adding path before logfilename is optional; logs responses (NOT eye movements, these are stored in an EDF file!)
RESDIR = os.path.join(DIR, 'resources')
IMAGES = [os.path.join(RESDIR, 'testImages\m086c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m070c4b.jpg'),
		  	os.path.join(RESDIR, 'testImages\m067c4b.jpg'),
		 	os.path.join(RESDIR, 'testImages\m066c4b.jpg'),
		  	os.path.join(RESDIR, 'testImages\m065c4b.jpg'),
		  	os.path.join(RESDIR, 'testImages\m058c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m043c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m042c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m040c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m039c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m038c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m037c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m030c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m028c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m022c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m021c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m017c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m016c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m008c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m005c4b.jpg'),
]

FOILIMAGES = [os.path.join(RESDIR, 'testImages\m039c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m030c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m038c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m030c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m033c4b.jpg'),
		  	os.path.join(RESDIR, 'testImages\m065c4b.jpg'),
		 	os.path.join(RESDIR, 'testImages\m062c4b.jpg'),
		  	os.path.join(RESDIR, 'testImages\m040c4b.jpg'),
		  	os.path.join(RESDIR, 'testImages\m068c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m067c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m039c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m065c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m042c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m038c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m093c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m070c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m026c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m028c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m068c4b.jpg'),
			os.path.join(RESDIR, 'testImages\m013c4b.jpg'),
]
# DISPLAY
# used in libscreen; the values may be adjusted, but not the constant's names
SCREENNR = 0 # number of the screen used for displaying experiment
DISPTYPE = 'pygame' # either 'psycho' or 'pygame'
DISPSIZE = (1920,1080) # canvas size
SCREENSIZE = (39.9,29.9) # physical screen size
MOUSEVISIBLE = False # mouse visibility
BGC = (127,127,127,255) # backgroundcolour
FGC = (0,0,0,255) # foregroundcolour

# EYETRACKER
# general
TRACKERTYPE = 'eyelink' # either 'smi', 'eyelink' or 'dummy' (NB: if DUMMYMODE is True, trackertype will be set to dummy automatically)
SACCVELTHRESH = 35 # degrees per second, saccade velocity threshold
SACCACCTHRESH = 9500 # degrees per second, saccade acceleration threshold
# SMI only
SMIIP = '127.0.0.1'
SMISENDPORT = 4444
SMIRECEIVEPORT = 5555
