import math
import matplotlib as mp
import random

#create a empty dataframe
#data will hold the force value at each frame

data = {}
unweighting_data={}

#how long from beginning of jump to end of jump
#we will add to this throughout
total_time = 0

#velocity will change throughout
velocity=0

#acceleration will change throughout
acceleration=0

#total frames
total_frames = 0


#mass on person
#in kg
mass = 80

#gravity
gravity = -9.81

####################################
#quiet phase

#simulate random time between 1.5 and 2 for the quiet interval
quiet_interval = round(random.uniform(1.3,1.6), 2)
total_time += quiet_interval

#Resting (Quiet Phase) force
#F=ma
force_quiet = int(round(mass*(-1)*gravity))

#calculate amount of frames captures
quiet_frames = int(round(quiet_interval*60))
total_frames += quiet_frames

#get data for each fram in the quiet interval
for frame in range(quiet_frames):
    velocity = 0
    acceleration = 0

    data[frame]=[velocity],[acceleration],[force_quiet]






####################################
#unweighting phase

#simulate random time between .3 and .5 for the unweighting phase
unweighting_interval = round(random.uniform(.2,.3), 2)
total_time += unweighting_interval

#calculate amount of frames captures
unweighting_frames = int(round(unweighting_interval*60))
total_frames += unweighting_frames

#calculate unweighting peak force (must be lower than quiet phase)
force_unweighting = (-1)*(round(random.randint(100, force_quiet)))

for frame in range(unweighting_frames):
    force = round(force_unweighting*math.cos((((2*(math.pi))/((unweighting_frames)*2))*(frame))-((math.pi)/(2)))+force_quiet, 2)
    unweighting_data[frame]=[force]


###################################






#simualte random time between 1.25 and 1.75 for the propulsion phase
propulsion_interval = round(random.uniform(1.25, 1.75), 1)
total_time += propulsion_interval

#simulate random time in air time between .5 and .7 for the air time
time_in_air_interval = round(random.uniform(.5, .7), 1)
total_time += time_in_air_interval

#simulate random time in air time between .75 and 1.25 for the landing time
landing_interval = round(random.uniform(.75, 1.25), 1)
total_time += landing_interval










data[1] = 500

print(unweighting_data)
print (unweighting_frames)
print (total_time)
#for loop capturing data for each frame
#for frame in range(frames):
    
   


