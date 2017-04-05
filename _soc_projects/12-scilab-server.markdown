---
layout: soc-project
image: /images/server.jpg
title: Scilab server
mentor: "Srikant Patnaik"
category: "Development"
weight: 30
ribbon: FOSSEE
application_procedure: "proposal"
contact: "FOSSEE"
stipend: INR 50000
---

Enchancing the Scilab server to efficiently load and deliver results to the user.

<!--break-->

Scilab Textbook Companion (TBC) is one of the flagship activities undertaken by FOSSEE. It is a collection of code for each solved example of a standard textbook. We have active Scilab and Python TBCs. Students and faculty of colleges have created more than 500 Scilab TBC and a similar number of Python TBC. As there are about 50,000 scripts in 500 TBCs, it becomes a valuable resource for documentation, function usage search and also as a subject learning material. More details could be fetched from [here](http://www.scilab.in/Textbook_Companion_Project).

Unlike other scripting languages, Scilab loads a huge set of libraries in the background. Thus a single instance causes considerable consumption of computer resources.This would create a problem if we want to have parallel instances of Scilab.

We have thought of a couple of solutions to this problem.

- Fixing the Scilab core to only load libraries which are called in the program at the run time.
- Developing an atoms module to accept code from various threads and pipe them to a single Scilab instance.

The atoms module shall do the following:

1. It should decode communication packet(code) received from user
2. Execute Scilab code in a protected environment 
3. Return the result/error to the user
4. Clear the Scilab memory

In the case of overloading on a single Scilab instance, there should be an intermediate program to monitor and initiate a new Scilab instance. This autoscaling operation should happen seamlessly. The autoscaling program should keep track of user requests.
