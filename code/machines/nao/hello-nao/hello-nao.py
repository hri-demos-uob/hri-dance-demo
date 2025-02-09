#
#
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
# NAO VERSION: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
#
# Miguel Xochicale [http://mxochicale.github.io]
#
# Reference: https://github.com/mikemcfarlane/TickleMeNAO/blob/master/Markov_tickles_motion_data.py

__author__ = "Miguel P Xochicale"
__version__ = "Revision: 0.01"
__date__ = "Date: 10-11-18"
__license__ = "TBC"



##############################################################
# LEFT ARM MOTION DATA
##############################################################


##############################################################
# Shake left arm in front, then open close hand.
leftArmMovementList2 = [

						["LElbowRoll",
						[0.48, 0.92, 1.28, 1.64, 2.2, 2.68, 3.12, 3.32],
						[-0.0613179, -0.076658, -0.0429101, -0.08126, -0.08126, -0.079726, -0.08126, -0.0429101]],

						["LElbowYaw",
						[0.48, 0.92, 1.28, 1.64, 2.2, 2.68, 3.12, 3.32],
						[-1.07998, -1.26713, -1.23338, -1.28707, -1.28707, -1.28707, -1.28707, -1.25025]],

						["LHand",
						[0.48, 0.92, 1.28, 1.64, 1.96, 2.2, 2.44, 2.68, 2.92, 3.12, 3.32],
						[0.2948, 0.2948, 0.2944, 0.2948, 0, 0.00559998, 1, 0.9648, 0.29, 0.2904, 0.2904]],

						["LShoulderPitch",
						[0.48, 0.92, 1.28, 1.64, 2.2, 2.68, 3.12, 3.32],
						[1.21028, 1.20415, 1.21028, 1.1704, 1.1704, 1.17193, 1.17193, 1.20722]],

						["LShoulderRoll",
						[0.48, 0.92, 1.28, 1.64, 2.2, 2.68, 3.12, 3.32],
						[0.0229681, 0.00149202, -0.0107799, 0.0214341, 0.0214341, 0.0214341, 0.0214341, 0.029104]],

						["LWristYaw",
						[0.48, 0.92, 1.28, 1.64, 2.2, 2.68, 3.12, 3.32],
						[1.82387, -1.82387, 1.82387, -1.82387, -1.82387, -1.82387, -1.82387, -0.04146]]

						]

upArms = [
		["HeadPitch",
		[1, 2, 3],
		[[-0.199462, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.199462, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.199461, [3, -0.333333, 0], [3, 0, 0]]] ],

		["HeadYaw",
		[1, 2, 3],
		[[0, [3, -0.333333, 0], [3, 0.333333, 0]], [0, [3, -0.333333, 0], [3, 0.333333, 0]], [0, [3, -0.333333, 0], [3, 0, 0]]] ],

		["LElbowRoll",
		[1, 2, 3],
		[[-0.757754, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.803774, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.757754, [3, -0.333333, 0], [3, 0, 0]]] ],

		["LElbowYaw",
		[1, 2, 3],
		[[-1.27173, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.22878, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.27173, [3, -0.333333, 0], [3, 0, 0]]] ],

		["LHand",
		[1, 2, 3],
		[[0.3112, [3, -0.333333, 0], [3, 0.333333, 0]], [0.3572, [3, -0.333333, 0], [3, 0.333333, 0]], [0.3112, [3, -0.333333, 0], [3, 0, 0]]]  ],

		["LShoulderPitch",
		[1, 2, 3],
		[[0.961776, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.843742, [3, -0.333333, 0], [3, 0.333333, 0]], [0.961776, [3, -0.333333, 0], [3, 0, 0]]]  ],

		["LShoulderRoll",
		[1, 2, 3],
		[[0.161028, [3, -0.333333, 0], [3, 0.333333, 0]], [0.193242, [3, -0.333333, 0], [3, 0.333333, 0]], [0.161028, [3, -0.333333, 0], [3, 0, 0]]]  ],

		["LWristYaw",
		[1, 2, 3],
		[[0.0858622, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0138481, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0858622, [3, -0.333333, 0], [3, 0, 0]]]  ],

		["RElbowRoll",
		[1, 2, 3],
		[[0.73943, [3, -0.333333, 0], [3, 0.333333, 0]], [0.786984, [3, -0.333333, 0], [3, 0.333333, 0]], [0.73943, [3, -0.333333, 0], [3, 0, 0]]]  ],

		["RElbowYaw",
		[1, 2, 3],
		[[1.27164, [3, -0.333333, 0], [3, 0.333333, 0]], [1.28698, [3, -0.333333, 0], [3, 0.333333, 0]], [1.27164, [3, -0.333333, 0], [3, 0, 0]]]   ],

		["RHand",
		[1, 2, 3],
		[[0.304, [3, -0.333333, 0], [3, 0.333333, 0]], [0.304, [3, -0.333333, 0], [3, 0.333333, 0]], [0.304, [3, -0.333333, 0], [3, 0, 0]]]   ],

		["RShoulderPitch",
		[1, 2, 3],
		[[0.983336, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.814512, [3, -0.333333, 0], [3, 0.333333, 0]], [0.983336, [3, -0.333333, 0], [3, 0, 0]]]   ],

		["RShoulderRoll",
		[1, 2, 3],
		[[-0.176452, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.27923, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.176453, [3, -0.333333, 0], [3, 0, 0]]]  ],

		["RWristYaw",
		[1, 2, 3],
		[[0.12728, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0367742, [3, -0.333333, 0], [3, 0.333333, 0]], [0.12728, [3, -0.333333, 0], [3, 0, 0]] ]    ]

		]





##############################################################
# MOTION DATA LISTS
##############################################################


#ArmMovementList = [leftArmMovementList2, upArms]
#ArmMovementList = [upArms]
ArmMovementList = [leftArmMovementList2]

##############################################################


import argparse
from naoqi import ALProxy
from pprint import pprint

def main(robotIP, PORT):
    """ Simple code to test above motion data. """
    # Choregraphe simplified export in Python.
    motion  = ALProxy("ALMotion", robotIP, PORT)
    posture = ALProxy("ALRobotPosture", robotIP, PORT)

    # For text to speech
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)

    tts.setVolume(1.0)  ##Volume set to 100%
    tts.setParameter("pitchShift", 1.2) #Applies a pitch shifting to the voice
    tts.setParameter("doubleVoice", 0.0) #Deactivates double voice
    #tts.say("Hiya. My name is NAO and this is a simple testing where I am moving my left arm and hand.") 
    tts.say("Hello, I am NAO") 



    testList = ArmMovementList

    bezier = True

    motion.wakeUp()

    for i in range(len(testList)):
        names = list()
        times = list()
        keys = list()

        for n, t, k in testList[i]:
            names.append(n)
            times.append(t)
            keys.append(k)

        if bezier:
            motion.angleInterpolationBezier(names, times, keys)
        else:
            motion.angleInterpolation(names, keys, times, True)

  
    motion.rest() # Go to rest position 


    tts.say("bye bye")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)

