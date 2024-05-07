# Programmist Day Routine Game
<img src="https://github.com/eugenekravchuk/daily-routine-fsm/assets/81439861/319d24dd-4ff2-4114-9f24-1e8fd5780584" width="400">

# Architecture
The whole game concept is based on FSM (Finite State Machine) <br/>
Tha machine used in the game is below:<br/><br/>
<img src="https://github.com/eugenekravchuk/daily-routine-fsm/assets/81439861/bd85f45b-d90b-4620-9699-76bbd06bacf9" width="600">

Also you can view it [here](https://www.figma.com/file/4JUdsV5ANTm8asC2KZwxUR/fsm_lab?type=whiteboard&node-id=0%3A1&t=qFkUun0aU0BkkOQO-1)

# Instalation
```python
git clone https://github.com/eugenekravchuk/daily-routine-fsm.git
cd daily-routine-fsm
python game.py
```

# Rules
You start playing from a start state - 'sleep' <br/>
And also you have four parameters that will influence your choices (time of the day, tiredness and apetite) <br/>
With every input you more to a different state <br/>
The goal of the game is to get back to a sleep state till midnight <br/>
But you can't just sleep all day) You have to have dinner and then go to sleep <br/>
If you fail to do that - you loose <br/>

P.S. Also, don't go to Zhytomyr, there is no way out of there...

# Restrictions:
- You can have lunch only from 12AM and dinner from 6PM
- To eat you have to have apetite more that 30
- To do programming you have to have tiredness less than 80

