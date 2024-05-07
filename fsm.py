"""FSM module"""

import random
from constants import SAD_MEME, CHAD_STRING, ALIEN_MEME

def prime(fn):
    """Decorator for states to send input"""
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper

class DailyRoutineFSM:
    """Daily Routine FSM class"""
    def __init__(self):
        self.wake_up = self._create_wake_up()
        self.breakfast = self._create_breakfast()
        self.lunch = self._create_lunch()
        self.dinner = self._create_dinner()
        self.sleep = self._create_sleep()
        self.rest = self._create_rest()

        self.programming = self._create_programming()
        self.debugging = self._create_debugging()
        self.reading_documentation = self._create_reading_documentation()

        self.going_to_zhytomyr = self._create_going_to_zhytomyr()

        self.current_time = 7 # 0-24
        self.tiredness = random.randint(1, 30) # 0-100
        self.apetite = random.randint(0, 20) # 0-100

        self.current_state = self.sleep
        self.stopped = False
        self.had_dinner = False
        self.had_lunch = False

    def send(self, action):
        """Sends actions"""
        try:
            self.current_state.send(action)
        except StopIteration:
            self.stopped = True

    def does_match(self):
        """In the end of the game used
        to check if current state is sleep"""
        return self.current_state == self.sleep and self.had_dinner

    @prime
    def _create_sleep(self):
        while True:
            action = yield

            if self.current_time >= 24:
                print("You haven't finished a day till midnight")
                print("Game over")
                self.stopped = True

            elif action == "wake_up" and self.current_time == 7:
                print("You barely woken up, but you did it. Congratulations!!!")
                print("Your actions: 'sleep' or 'have_breakfast', choose one:")
                self.current_time += 0.25
                self.current_state = self.wake_up
                self._change_apetite(5)
                self._change_tiredness(-5)

            elif action == "wake_up" and self.current_time > 7:
                print("You woken up")
                print("Your actions: 'sleep' or 'have_breakfast', choose one:")
                self.current_time += 0.25
                self.current_state = self.wake_up
                self._change_apetite(5)
                self._change_tiredness(-5)

            elif action == "wake_up" and self.current_time <7:
                print("It is too early, you just can't wake up => 🛌🛌🛌🛌🛌🛌")
                print("Your actions: 'wake_up' or 'sleep', choose one:")
                self.current_time += 0.25
                self._change_apetite(5)
                self._change_tiredness(-5)
                self.current_state = self.wake_up

            elif action == "sleep":
                print("=> 🛌🛌🛌🛌🛌🛌")
                print("Your actions: 'wake_up' or 'sleep', choose one:")
                self.current_time += 0.25
                self._change_apetite(5)
                self._change_tiredness(-5)
            else:
                print("Wrong choice, try again!")
                print("Your actions: 'wake_up' or 'sleep', choose one:")

    @prime
    def _create_wake_up(self):
        while True:
            action = yield

            if self.current_time >= 24:
                print("You haven't finished a day till midnight")
                print("Game over")
                self.stopped = True

            elif action == 'sleep':
                print("=> 🛌🛌🛌🛌🛌🛌")
                print("Your actions: 'wake_up' or 'sleep', choose one:")
                self.current_time += 0.25
                self.current_state = self.sleep
                self._change_apetite(5)
                self._change_tiredness(-5)

            elif action == "have_breakfast":
                print("😋😋😋😋😋")
                print("Your actions: 'programming' (you have no options 🙃), choose one:")
                self.current_time += 1
                self.current_state = self.breakfast
                self._change_apetite(-20)
                self._change_tiredness(-10)
            else:
                print("Wrong choice, try again!")
                print("Your actions: 'sleep' or 'have_breakfast', choose one:")

    @prime
    def _create_breakfast(self):
        while True:
            action = yield

            if self.current_time >= 24:
                print("You haven't finished a day till midnight")
                print("Game over")
                self.stopped = True

            elif action == 'programming':
                self.current_time += 0.5
                self.current_state = self.programming
                print("👩‍💻👩‍💻👩‍💻👩‍💻👩‍💻👩‍💻👩‍💻")
                print("Possible outcomes: 'success' or 'error' , choose one:")
                self._change_apetite(5)
                self._change_tiredness(5)
            else:
                print("Wrong choice, try again!")
                print("Your actions: 'programming' (you have no options 🙃), choose one:")

    @prime
    def _create_programming(self):
        while True:
            action = yield

            if self.current_time >= 24:
                print("You haven't finished a day till midnight")
                print("Game over")
                self.stopped = True

            elif (action == 'success' or action == 'error') and self.tiredness >= 80:
                print("You are too tired to code, your tiredness is more that 80")
                print("Your choices: 'rest' or 'have_lunch' or 'have_dinner', choose one:")

            elif action == 'success':
                print(CHAD_STRING)
                print("Good job!!!")
                self.current_time += 0.5
                if self._is_time_for_dinner():
                    print("You did well, so you come back to programming\n\
Your choices: 'error' or 'success' or 'have_dinner' or 'rest', choose one: ")
                elif self._is_time_for_lunch():
                    print("You did well, so you come back to programming\n\
Your choices: 'error' or 'success' or 'have_lunch' or 'rest', choose one: ")
                else:
                    print("You did well, so you come back to programming\n\
Your choices: 'error' or 'success' or 'rest', choose one: ")
                self._change_apetite(5)
                self._change_tiredness(5)

            elif action == "error":
                print(SAD_MEME)
                print("You have an error so you go debugging")
                if self._is_time_for_dinner():
                    print("Your choices: 'error' or 'success' or \
'have_dinner' or 'rest', choose one: ")
                elif self._is_time_for_lunch():
                    print("Your choices: 'error' or 'success' or \
'have_lunch' or 'rest', choose one: ")
                else:
                    print("Your choices: 'error' or 'success' or 'rest', choose one: ")
                self.current_state = self.debugging
                self.current_time += 0.5
                self._change_apetite(5)
                self._change_tiredness(5)

            elif action == "have_lunch" or action == "have_dinner":
                self._process_eating(action)

            elif action == "rest":
                print("Time to regain strength for coding...")
                print("Your choices: 'programming', 'rest', 'have_lunch', 'have_dinner' ")
                self.current_state = self.rest
                self._change_apetite(5)
                self._change_tiredness(-20)
                self.current_time += 0.5

            else:
                print("Wrong choice, try again!")
                if self._is_time_for_dinner():
                    print("Your choices: 'error' or 'success' or 'have_dinner', choose one: ")
                elif self._is_time_for_lunch():
                    print("Your choices: 'error' or 'success' or 'have_lunch', choose one: ")
                else:
                    print("Your choices: 'error' or 'success', choose one: ")

    @prime
    def _create_debugging(self):
        while True:
            action = yield

            if self.current_time >= 24:
                print("You haven't finished a day till midnight")
                print("Game over")
                self.stopped = True

            elif (action == 'success' or action == 'error') and self.tiredness >= 80:
                print("You are too tired to code, your tiredness is more that 80")
                print("Your choices: 'rest' or 'have_lunch' or 'have_dinner', choose one:")

            elif action == 'success':
                print(CHAD_STRING)
                if self._is_time_for_dinner():
                    print("You did well, so you come back to programming\n\
Your choices: 'error' or 'success' or 'have_dinner' or 'rest', choose one: ")
                elif self._is_time_for_lunch():
                    print("You did well, so you come back to programming\n\
Your choices: 'error' or 'success' or 'have_lunch' or 'rest', choose one: ")
                else:
                    print("You did well, so you come back to programming\n\
Your choices: 'error' or 'success' or 'rest', choose one: ")
                self.current_time += 0.5
                self.current_state = self.programming
                self._change_apetite(5)
                self._change_tiredness(5)

            elif action == 'error' and random.random() > 0.6:
                print(SAD_MEME)
                print("As you are full of despair, you go reading a documentation")
                print("Your choices: 'success' or 'error' or 'rest', choose one: ")
                self.current_time += 0.5
                self.current_state = self.reading_documentation
                self._change_apetite(5)
                self._change_tiredness(5)

            elif action == 'error':
                print(SAD_MEME)
                print("Unfortunately! You continue debugging")
                if self._is_time_for_dinner():
                    print("Your choices: 'error' or 'success' or \
'have_dinner' or 'rest', choose one: ")
                elif self._is_time_for_lunch():
                    print("Your choices: 'error' or 'success' or \
'have_lunch' or 'rest', choose one: ")
                else:
                    print("Your choices: 'error' or 'success' or 'rest', choose one: ")
                self.current_time += 0.5
                self._change_apetite(5)
                self._change_tiredness(5)

            elif action == "have_lunch" or action == "have_dinner":
                self._process_eating(action)

            elif action == "rest":
                print("Time to regain strength for coding...")
                print("Your choices: 'programming', 'rest', 'have_lunch', 'have_dinner' ")
                self.current_state = self.rest
                self._change_apetite(5)
                self._change_tiredness(-20)
                self.current_time += 0.5

            else:
                print("Wrong choice, try again!")
                if self._is_time_for_dinner():
                    print("You did well, so you come back to programming\
    Your choices: 'error' or 'success' or 'have_dinner', choose one: ")
                elif self._is_time_for_lunch():
                    print("You did well, so you come back to programming\
    Your choices: 'error' or 'success' or 'have_lunch', choose one: ")
                else:
                    print("You did well, so you come back to programming\
    Your choices: 'error' or 'success', choose one: ")

    @prime
    def _create_reading_documentation(self):
        while True:
            action = yield

            if self.current_time >= 24:
                print("You haven't finished a day till midnight")
                print("Game over")
                self.stopped = True

            elif (action == 'success' or action == 'error') and self.tiredness >= 80:
                print("You are too tired to code, your tiredness is more that 80")
                print("Your choices: 'rest', choose one:")

            if action == 'success':
                self.current_time += 0.5
                self.current_state = self.going_to_zhytomyr
                print(ALIEN_MEME)
                print("You are going to Zhytomyr... and disappear...")
                print("There is no way out of Zhytomyr...")
                print("Your choices: 'give_up', choose one: ")
                self._change_apetite(5)
                self._change_tiredness(5)

            elif action == "error":
                print(SAD_MEME)
                print("Unfortunately! You continue debugging")
                print("Your choices: 'success' or 'error' or 'rest', choose one: ")
                self.current_time += 0.5
                self.current_state = self.debugging
                self._change_apetite(5)
                self._change_tiredness(5)

            elif action == "rest":
                print("Time to regain strength for coding...")
                print("Your choices: 'programming', 'rest', 'have_lunch', 'have_dinner' ")
                self.current_state = self.rest
                self._change_apetite(5)
                self._change_tiredness(-20)
                self.current_time += 0.5

            else:
                print("Wrong choice, try again!")
                print("Your choices: 'success' or 'error' or 'rest', choose one: ")

    @prime
    def _create_going_to_zhytomyr(self):
        while True:
            action = yield
            if action != "give_up":
                print('You are stuck, there is no way out!')
                print("Your choices: 'give_up', choose one: ")
            else:
                print("Game over")
                self.stopped = True

    @prime
    def _create_lunch(self):

        while True:
            action = yield
            if self.current_time >= 24:
                print("You haven't finished a day till midnight")
                print("Game over")
                self.stopped = True

            elif action == 'programming' and self.tiredness >= 80:
                print("You are too tired to code, your tiredness is more that 80")
                print("Your choices: 'rest', choose one:")

            elif action == 'programming':
                print("👩‍💻👩‍💻👩‍💻👩‍💻👩‍💻👩‍💻👩‍💻")
                print("Possible outcomes: 'success' or 'error' or 'rest' or 'have_dinner', choose one:")
                self.current_time += 0.5
                self.current_state = self.programming

            elif action == "rest":
                print("Time to regain strength for coding...")
                print("Your choices: 'programming', 'rest', 'have_dinner' ")
                self.current_state = self.rest
                self._change_apetite(5)
                self._change_tiredness(-20)
                self.current_time += 0.5

            else:
                print("Wrong choice, try again!")
                print("Your actions: 'programming' (you have no options 🙃), choose one:")

    @prime
    def _create_dinner(self):

        while True:
            action = yield

            if self.current_time >= 24:
                print("You haven't finished a day till midnight")
                print("Game over")
                self.stopped = True

            elif action == 'sleep':
                print("You go to bed => 🛌🛌🛌🛌🛌🛌🛌🛌🛌")
                print("Game successfully ended")
                print("YOU WON!!!")
                self.stopped = True
                self.current_state = self.sleep
            else:
                print("Wrong choice, try again!")
                print("Your choices: 'sleep' (time to go to bed 🛌), choose one: ")

    @prime
    def _create_rest(self):
        while True:
            action = yield
            if action == 'programming' and self.tiredness >= 80:
                print("You are too tired to code, your tiredness is more that 80")
                print("Your choices: 'rest' or 'have_lunch' or 'have_dinner', choose one:")

            if action == 'programming':
                print("👩‍💻👩‍💻👩‍💻👩‍💻👩‍💻👩‍💻👩‍💻")
                print("Possible outcomes: 'success' or 'error', choose one:")
                self.current_state = self.programming
                self._change_apetite(5)
                self._change_tiredness(5)
                self.current_time += 0.5

            elif action == "rest":
                print("Time to regain strength for coding...")
                print("Your choices: 'programming', 'rest', 'have_lunch', 'have_dinner' ")
                self._change_apetite(5)
                self._change_tiredness(-20)
                self.current_time += 0.5

            elif action == "have_lunch" or action == "have_dinner":
                self._process_eating(action)
            else:
                print("Wrong choice, try again!")
                print("Your choices: 'sleep' (time to go to bed 🛌), choose one: ")

    def _is_time_for_lunch(self):
        return self.current_time >= 12

    def _is_time_for_dinner(self):
        return self.current_time >= 18

    def _change_tiredness(self, amount):
        if self.tiredness + amount < 0:
            self.tiredness = 0
        elif self.tiredness + amount > 100:
            self.tiredness = 100
        else:
            self.tiredness += amount

    def _change_apetite(self, amount):
        if self.apetite + amount < 0:
            self.apetite = 0
        elif self.apetite + amount > 100:
            self.apetite = 100
        else:
            self.apetite += amount

    def _process_eating(self, action):
        if action == "have_lunch" and self._is_time_for_lunch() \
    and self.apetite >= 30 and not self.had_lunch:
            print("Time for lunch you go eating😋😋😋😋😋")
            print("Your choices: 'programming' or 'rest', choose one: ")
            self.current_state = self.lunch
            self.current_time += 1
            self._change_tiredness(-10)
            self._change_apetite(-20)
            self.had_lunch = True

        elif action == "have_lunch" and not self._is_time_for_lunch():
            print("It is too early to have lunch, you can have lunch only after 12 AM")
            if self.current_state == self.rest:
                print("Your choices: 'programming' or 'rest', choose one: ")
            else:
                print("Your choices: 'success' or 'error' or 'rest', choose one: ")

        elif action == "have_lunch" and self.had_lunch < 30:
            print("You already had a lunch")
            if self.current_state == self.rest:
                print("Your choices: 'programming' or 'rest', choose one: ")
            else:
                print("Your choices: 'success' or 'error' or 'rest', choose one: ")

        elif action == "have_lunch" and self.apetite < 30:
            print("You don't have apetite to eat, minimum apetite - 30")
            if self.current_state == self.rest:
                print("Your choices: 'programming' or 'rest', choose one: ")
            else:
                print("Your choices: 'success' or 'error' or 'rest', choose one: ")

        elif action == "have_dinner" and self._is_time_for_dinner() and self.apetite >= 30:
            print("Time for dinner you go eating😋😋😋😋😋")
            print("Your choices: 'sleep' (time to go to bed 🛌), choose one: ")
            self.current_state = self.dinner
            self.current_time += 1
            self._change_tiredness(-10)
            self._change_apetite(-20)
            self.had_dinner = True

        elif action == "have_dinner" and not self._is_time_for_dinner():
            print("It is too early to have dinner, you can have lunch only after 6 PM")
            if self.current_state == self.rest:
                print("Your choices: 'programming' or 'rest', choose one: ")
            else:
                print("Your choices: 'success' or 'error' or 'rest', choose one: ")

        elif action == "have_dinner" and self.apetite < 30:
            print("You don't have apetite to eat, minimum apetite - 30")
            if self.current_state == self.rest:
                print("Your choices: 'programming' or 'rest', choose one: ")
            else:
                print("Your choices: 'success' or 'error' or 'rest', choose one: ")
