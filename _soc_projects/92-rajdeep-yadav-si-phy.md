---
layout: soc-project
image: /images/project92.jpg
title: Si-Phy
mentor: "Rajdeep Yadav"
category: "Development"
application_procedure: "none"
weight: 92
ribbon: new
contact:
- Email - <a target="_blank" href="mailto:rajdeepyadav004@gmail.com">rajdeepyadav004@gmail.com</a>
- Whatsapp - 9079241867


---



---
Si-Phy is a short form for silicon physics. Physics simulated on a silicon chip. 


<!--break-->

No. of mentees: 4

Pre-requisites: Basic knowledge of Object oriented programming, and obviously a bit of mechanics knowledge.  

My goal is to create a light-weight physics engine(particularly for newtonian mechanics), that can be further used to create a lot of interesting simulations (some of which I have mentioned below). Depending on how familiar you guys are with C++ and python, we’ll choose one of these languages to build our engine. 

Two things need to be developed in this project, first will be the physics engine itself, which will do all our physics calculations. Second will be a renderer, which will display our objects on screen. I plan to make the renderer as simple as possible, in turn we’ll focus on various physics systems. 

I want to include the following features in the physics engine: 
- Gravity: We’ll start with simulating a ball doing free fall under gravity. 
- Friction and Normal forces
- Strings and springs
- Collisions
- Torque 

We’ll need the following features from the renderer. 
- Ability to display simple 3D shapes.
- Basic lighting
- Traces (To track movement of the objects)

Depending on circumstances, we’ll also create some interesting simulations with our engine. What you wanna do with it is completely up to you, however just as a starting point I’m mentioning a few things that we can do. 

- Simple Harmonic motion. 
- N-pendulum: Pendulums get extremely interesting when we link them. A very simple example: https://www.youtube.com/watch?v=QXf95_EKS6E. 
- Tensegrity, the “impossible” table: https://i.pinimg.com/originals/ae/17/f5/ae17f5be987f05a170f6dc84ef54544e.jpg 

What I expect from the proposal: 
- Your familiarity with c++ and python. 
- Your motivation to do the project. 
- An interesting simulation you want to do with the project. This will be the major selection criteria. Describe what you want to do, and what exact components will be needed to build the simulation (For example, to build n-pendulum, you need to model gravity and strings). Also, don't get over ambitious :P

It does not need to be a long proposal. Keep it short and to the point. Feel free to contact me if you want help in determining what components are needed for the proposal. 

<!--break-->

### Tentative Project Timeline
<!--break-->

|Week Number  | Tasks to be Completed|
|--- | --- | 
|**Week 1** |One or two of you will work with me on the renderer, and others will work on implementing a world with (uniform) gravity.|
|**Week 2-3** |We'll work on extending the model. Integrate Friction, Normal, strings etc with the systems. The work will be divided, so some of you will work on let's say friction and normal, while some of you will work on Strings and springs. |
|**Week 4-5** | Developing your own simulation. You'll work individually to use the physics engine to build a simulation model of your own, most likely the one you submitted in the proposal. |