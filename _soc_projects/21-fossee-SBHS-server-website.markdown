---
layout: soc-project
image: /images/virtuallab.jpg
title: SBHS Virtual lab server and website
mentor: 
- Rupak Rokade
category: "Development"
weight: 72
ribbon: FOSSEE
application_procedure: "proposal"
contact: "FOSSEE"
stipend: INR 30000
openings: 2
---

A Virtual Laboratory is an online facility aimed at providing an laboratory experience to students. This project involves improving SBHS remote-triggered virtual lab server and website.

<!--break-->

Unlike Simulation Virtual Labs, Remote Triggered Virtual Labs (RT labs for short) is that category of Virtual Labs which enables the student to access a real experimental setup, remotely. One such facility is available for a laboratory setup known as “Single Board Heater System”, SBHS for short. The SBHS RT lab can be accessed [here](http://vlabs.iitb.ac.in/sbhs/). To understand what is SBHS, see the spoken tutorial available [here](http://goo.gl/lYdhRi). If you want to quickly learn how to access SBHS RT labs see [this](http://goo.gl/vs5P9d). A good documentation/manual on this is available [here](http://sbhs.fossee.in/downloads) under the “Documentation” section. The document contains a dedicated chapter which attempts to explain the Client-Server architecture.

A few bugs/features to be addressed:

- There are two main bugs which result in "no connection" to the server and "no communication" with the hardware. They have to be identified and resolved.
- An admin interface is required where he/she can carry out certain tests and check for the server health, easily. For example, there has to be a web facility for the admin to test a particular SBHS and acquire the results, bypassing the common user rules.
- An admin interface is also required to check all webcams.
- An admin interface is also required to download users data files based on slot date-time.
- Needs test cases to check the server functionality.
- Some Version Controlling issues have to be fixed.
- Automated health monitoring has to be implemented to remove the non-working SBHS units and report to admin.
- The current server handles all the load, including hardware interface. Enable load sharing with a connected computer.
