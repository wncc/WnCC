---
layout: soc-project
image: /images/debabrata-road.jpg
title: Road Network 3D Rendering using OpenGL
mentor: "Debabrata Mandal"
category: "Computer Graphics, UI Design"
application_procedure: "none"
weight: 53
ribbon: new
contact:
- Slack - <a target="_blank" href="soc-2020workspace.slack.com"> Workspace </a>  

- Email - <a target="_blank" href="mailto:mandaldebabrata123@gmail.com">mandaldebabrata123@gmail.com</a>

mentees:
- Aman Yadav 
- Devansh Jain

---


This project focuses on the task of creating a UI for visualizing traffic flow in a city(a road network) using OpenGL.
The problem of traffic congestion has seen different types of approaches from using simple heuristics to complex machine learning based approaches to predict correct traffic signals in a road network.
This project does not aim to solve the traffic congestion problem! It will merely serve as a tool to help solving the aforementioned problem. 

<!--break-->

### Details of Project :
We will be using OpenGL to render a city and its various components. Elaborating the previous line , we will be creating models in C++ using OpenGL to simulate objects like roads, cars, traffic signals, road junctions etc (UI should be able to read object meshes provided by user for models). All this can be modeled in OpenGL without significant efforts , but the important part is to integrate the UI with the visual platform for e.g. rendering turns on roads as realistically as possible(using curve interpolations).
The UI must be as simplistic as possible . This means user should be able to provide the road network in the form of a road network file or graphical description for simpler models like spheres etc.
The major part of the project would be on improving a crude UI developed at first and adding extra features(as proposed by mentees).
For example possible additions could be - 
1. Allowing widely varying dimensions of vehicle models 
2. Check for collisions and abort with proper messaging or feedback.

### Project Requirements - 
Good level of experience with C++ , beginners level experience using OpenGL libraries in C++ is desirable. 
Note: This would be a coding intensive project and ability to debug your own code is a must.

### Reading Material:
- [Research Paper](https://ieeexplore.ieee.org/document/7312683)
- [OpenGL](http://www.opengl-tutorial.org/) 
- Other resources are widely available online

### Tentative Project Timeline
<!--break-->

|Week Number  | Tasks to be Completed|
|--- | --- | 
|**Week 1** |Learn using OpenGL in C++ , i.e. start with view transformations, window creation, hierarchical modeling , GLSL Shading, camera positioning etc.|
|**Week 2** |Start coding simple models like spheres, cubes, cylinders, surfaces.|
|**Week 3** |Learn texture mapping for complex figures and add define basic prototypes for users like vehicles|
|**Week 4** |Design a basic UI in C++ to read in obj files and initialize objects correspondingly in the renderer.|
|**Week 5** |Learn Bezier curve(or any other) interpolation to determine trajectories and store in proper file formats.|
|**Week 6** |Learning basics of animation in OpenGL and render the first road network animation. |
|**Week 7** | Modify UI to let user switch between multiple traffic light junctions to visualize performance.|
|**Week 8** |Testing for collisions, add multiple vehicle models to 3D renderer. |
