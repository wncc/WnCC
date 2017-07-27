---
layout: soc-project
image: /images/scilab.png
title: Scilab-Julia Interface
mentor: "Shamika Mohanan"
category: "Development"
weight: 10
ribbon: progress
application_procedure: "proposal"
stipend: INR 10000
mentees:
- Harshith Goka
---

Create an interface that can call any Julia function from Scilab console and displays the output of the Julia function on Scilab console. 

<!--break-->

### Applicant profile:
The applicant should-

- Have excellent coding skills in C and C++
- Know how to call functions from external libraries in C/C++ code
- Know how to compile C/C++ code by linking against external libraries

### Suggested reading:

- [Scilab API](https://help.scilab.org/docs/5.5.2/en_US/section_204636e951f595409bc6782bb8e1d2d9.html)
- [Embedding Julia in C](http://docs.julialang.org/en/release-0.4/manual/embedding/)

### Week 0

* Read through the Scilab API and how to build and load libraries in Scilab.
* Created a test library for familiarising myself with the Scilab API.
* Also successfully linked Julia to the test library and called a function in Julia.

### Week 1

* Wrote a code converting a scilab double matrix to a Julia double matrix and vice versa
* Debugging the above conversion code 
* Resolved an issue in double conversion 
* Added conversion code similar to double for boolean

### Week 2
* Converted to efficient copying of data from scilab to Julia
* Added support for multiple outputs of a function
* Added code for Integer data types
* Fixed a bug regarding scalar return types
* Added macOS Julia libraries and tried linking them

### Week 3
* Added support for scalar types conversions for all three types
* Added boolean support completed and tested
* Added code for Hypermat doubles extraction from scilab but can’t inject into julia environment
* Added similar code for Hypermat int and boolean conversion

### Week 4
* Debugged the Hypermat conversions for double data types
* Added Hypermat conversions for boolean and int data types
* Added Scalar String conversion to and fro Scilab and Julia

### Week 5
* Added complex scalars conversions
* Added support for array of strings
* Added Double complex arrays conversion
* Created the function “evalJulia”, to just evaluate a string in Julia

### Week 6
* Tried to build the code on Windows, but there was a compiler compatibility problem
* Was able to create a sparse in Julia from scilab
* Completed the sparse matrix conversion
* Julia 0.6 released and ported the code to the latest release, there was a change in the way of storing Boolean Matrices, fixed that
* Made the code more modular, and added functionality to import julia packages
* Handling Void Julia return type

### Week 7
* Added support for non-scilab compatible types by storing them as pointers to Julia variable in Scilab. 
* Added another function to get any Global Variables in Julia to use as argument to the Functions
* Restructured the code to match a scilab toolbox, added a shell script to install julia packages before importing the julia package in Scilab
