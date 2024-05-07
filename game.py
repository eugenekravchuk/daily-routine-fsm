"""Module with a game logic"""

from fsm import DailyRoutineFSM
from constants import SIGMA_STRING

fsm = DailyRoutineFSM()

print("Rules:")
print(" - You can have lunch only from 12AM and dinner from 6PM")
print(" - To eat you have to have apetite more that 30")
print(" - To do programming you have to have tiredness less than 80")
print("You have possible states: sleep, wake_up, breakfast, \
programming, debugging, reading_documentation, lunch, dinner and one secret state ...")
print()
print("Your goal: have dinner and go to sleep before midnight")
print("If you fail to do that, you loose...")
print()
print("Let's start our game...")
print()
print("***********************************")
print("You are sleeping now and alarm ringing\n\
Your actions: 'wake_up' or 'sleep', choose one:")
while not fsm.stopped:
    print("Current time: " + str(fsm.current_time))
    print("Apetite: " + str(fsm.apetite))
    print("Tiredness: " + str(fsm.tiredness))
    action = input(">> ")
    print()
    fsm.send(action)

if fsm.does_match():
    print(SIGMA_STRING)
    print("Day completed successfully!")
else:
    print("Day did not complete successfully!")
