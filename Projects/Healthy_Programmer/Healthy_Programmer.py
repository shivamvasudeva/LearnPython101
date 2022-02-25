"""
Objective:
Drink 3.5 lit -water.mp3 -- input to be there drank -- log text file

every 30 min eyes exercies -eyes.mp3 -- input done -- log text file
every 45 min physucal actvity -ex.mp3  -- input done log text file

9-5 sit on computer

"""

import datetime
import time
def getdate_time():
    return datetime.datetime.now()

datetime = str(getdate_time())

def office_time(currenttime):
    
    if currenttime > '09:00:00' and currenttime < '17:00:01':
        return True
    else:
        return False
    
Number_of_times_drink_water = 18  # 18 times we will drink water
drink_after_20min = 1200 # value in sec

eye_ex= 1800  # 30 mins = 1800 sec

physical_ex = 2700 # 45mins == 2700sec 



currenttime = time.strftime('%H:%M:%S') # It gives us current time

water_taken_at = time.time()
eye_ex_done_at = time.time()
physical_ex_done_at = time.time()

sleep_time = 60

while office_time(currenttime):

    if Number_of_times_drink_water > 0:
        if(time.time() - water_taken_at) > drink_after_20min:
            print ("Time to drink water")
            while True and Number_of_times_drink_water < 18:
                if input("Enter 'done' after drinking: ").lower() == 'done':
                    water_taken_at = time.time()
                    with open ('water_track.txt', 'a') as f:
                        f.write(f'Water taken at: {water_taken_at}')
                        break
                Number_of_times_drink_water = Number_of_times_drink_water -1


    if(time.time() - eye_ex_done_at) > eye_ex:
        print ("Do the Eye Exercise")
        while True:
            if input("Enter 'done' after EYE Rotation: ").lower() == 'done':
                eye_ex_done_at = time.time()
                with open ('eyes_exercise_track.txt', 'a') as f:
                    f.write(f'Eyes Rotated At:  {eye_ex_done_at}')
                    break

    if (time.time() - physical_ex_done_at) > physical_ex:
        print("Move!! Move!! Move!!!!!")
        while True:
            if input("Enter 'done' after Moving: ").lower() == 'done':
                physical_ex_done_at = time.time()
                with open('physical_exercise_track.txt', 'a') as f:
                    f.write(f'moved At:  {eye_ex_done_at}')
                    break

time.sleep(sleep_time)
currenttime = time.strftime('%H:%M:%S')
time_after_sleep= time.strftime('%H:%M:%S')

with open('track_every60s.txt', 'a') as f:
    f.write(f'CHECKED AT:  {time_after_sleep}')
