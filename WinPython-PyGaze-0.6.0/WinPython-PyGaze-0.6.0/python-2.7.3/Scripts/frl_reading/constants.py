import os.path

# MAIN
DUMMYMODE = True # False for connected eye tracker, True for dummy mode (using mouse or joystick)
LOGFILENAME = input("Participant name: ") # logfilename, without path

# DIRECTORY
DIR = os.path.split(os.path.abspath(__file__))[0]
DATADIR = os.path.join(DIR, 'data')
LOGFILE = os.path.join(DATADIR, LOGFILENAME) # .txt; adding path before logfilename is optional; logs responses (NOT eye movements, these are stored in an EDF file!)
RESDIR = os.path.join(DIR, 'resources')
IMAGES = [os.path.join(RESDIR, 'testImages\screenshot1.jpg'),
			os.path.join(RESDIR, 'testImages\screenshot2.jpg'),
			os.path.join(RESDIR, 'testImages\screenshot3.jpg'),
		  	os.path.join(RESDIR, 'testImages\screenshot4.jpg'),
		 	os.path.join(RESDIR, 'testImages\screenshot5.jpg'),
		  	os.path.join(RESDIR, 'testImages\screenshot6.jpg'),
		  	os.path.join(RESDIR, 'testImages\screenshot7.jpg'),
			os.path.join(RESDIR, 'testImages\screenshot8.jpg')]
FOILIMAGES = [os.path.join(RESDIR, 'foilImages\screenshot1.jpg'),
				os.path.join(RESDIR, 'foilImages\screenshot2.jpg'),
				os.path.join(RESDIR, 'foilImages\screenshot3.jpg'),
		 	 	os.path.join(RESDIR, 'foilImages\screenshot4.jpg'),
		 		os.path.join(RESDIR, 'foilImages\screenshot5.jpg'),
		 	 	os.path.join(RESDIR, 'foilImages\screenshot6.jpg'),
		 	 	os.path.join(RESDIR, 'foilImages\screenshot7.jpg'),
				os.path.join(RESDIR, 'foilImages\screenshot8.jpg')]

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
