---
layout: soc-project
image: /images/virtuallab.jpg
title: Building a Generic Remote Triggered Virtual Lab Interface
mentor: "Rupak Rokade"
category: "Development"
weight: 50
ribbon: FOSSEE
application_procedure: "proposal"
contact: "FOSSEE"
---

A Virtual Laboratory is an online facility aimed at providing a laboratory experience to students. Unlike Simulation Virtual Labs, Remote Triggered Virtual Labs (RT labs for short) is that category of Virtual Labs which enables the student to access a real experimental setup, remotely. One such facility is available for a laboratory setup known as “Single Board Heater System”, SBHS for short.

<!--break-->

 The SBHS RT lab can be accessed [here](http://vlabs.iitb.ac.in/sbhs/). To understand what is SBHS, see the spoken tutorial available [here](http://goo.gl/lYdhRi). If you want to quickly learn how to access SBHS RT labs click [here](http://goo.gl/vs5P9d). A good documentation on this is available [here](http://sbhs.fossee.in/downloads) under the “Documentation” section. The document contains a dedicated chapter which attempts to explain the Client-Server architecture.

### Shortcomings in the current solution:

- The solution is very specific to SBHS experimental setup. The architecture cannot work without re-writing a few modules if there is even a slight change in the hardware.
- There are some known software bugs which make a few SBHS unusable. These bugs are random and are currently unsolved.
It has very less admin specific features.

 
### Problem Statement:

- You are expected to come up with a more generic solution for RT labs in general. The solution should be robust, low on maintenance, automated and easily adaptable for a new hardware experimental setup, with minimum changes in the code. You may think of a central interface to customise the web solution as per the new hardware. For example, a number of inputs-outputs, protocol etc.
- The solution should have all the features of the existing SBHS RT lab solution. You can propose better alternatives, though.
- The solution has to be well documented with a regular version controlling/ backup setup.
- The admin should have easy interfaces to do health checkup of the hardware(s), bypassing all the user rules and also should be able to download users experimental data files based on the slot date-time value. Basically, the admin should have an easy control over the server without being a domain expert.
