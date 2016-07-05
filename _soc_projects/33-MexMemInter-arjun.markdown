---
layout: soc-project
image: /images/matlab.jpg
title: MEX Memory Interfacing
mentor: "Arjun Rao"
category: Scientific Computing
weight: 170
mentees:
---

The aim of this project is to remove the annoyances typically faced when writing a MEX program so as to be able to write meaningful, clean MEX (Short for MATLAB EXtensions) code.

<!--break-->

MEX is MATLAB's way of enabling you to use C to perform computations that would be painfully slow when written in MATLAB itself. 


While an elegant interface for C, it lacks several niceties that C++ provides. The Library MexMemoryInterfacing that I have worked on aims to bridge that gap to enable C++ programmers to elegantly access the MEX Interface all the while dealing with familiar constructs such as vectors, RAII, type inference.

The current repository can be accessed at 

[https://github.com/maharjun/MexMemoryInterfacing](https://github.com/maharjun/MexMemoryInterfacing)

(Partially Open Source since it depends on proprietary MATLAB Software. The code of MexMemoryInterface is completely Open Source)
