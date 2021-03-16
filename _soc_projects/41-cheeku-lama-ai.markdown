---
layout: soc-project
image: /images/cheeku-lama.jpg
title: L.A.M.A. AI using Reinforcement Learning
mentor: "Kumar Ayush, Anuj Shetty"
category: "Machine Learning, Development"
application_procedure: "none"
weight: 66
ribbon: new
stipend: INR 5000
contact:
- Facebook - <a target="_blank" href="https://www.facebook.com/cheekujodhpur">Kumar Ayush</a>&nbsp;<a target="_blank" href="https://www.facebook.com/shetty.anuj">Anuj Shetty</a>

- <a target="_blank" href="mailto:cheekujodhpur@gmail.com,anujshetty248@gmail.com">Email ID</a> - cheekujodhpur@gmail.com, anujshetty248@gmail.com

mentees:
- Akash Cherukuri
- Anirudh Mittal
- Jayesh Singla
- S. Anand Natarajan

---

Implementation of an RL based AI for playing L.A.M.A.

<!--break-->

### L.A.M.A.
[L.A.M.A.](https://boardgamegeek.com/boardgame/266083/llm) is a board game. It fits all the criteria I would look for. It is small to carry, easy to understand, quick to play and most importantly, a good mix of strategy and randomness. You can play it sober and not sober and have fun.

<!--break-->

### Pre-requisites
- Basic proficiency in Python

<!--break-->

### Tentative Project Timeline

We expect about 100 hours of work spread over ten weeks.

<!--break-->

|Week Number  | Tasks to be Completed|
|--- | --- | 
|**Week 1** |Play L.A.M.A. with us, and with your project group, and with friends to familiarise yourself with it. Then, enable logging for all state changes in the web game. As of now, no information is stored.|
|**Week 2** |Write a naive AI. Instead of expecting a player response, the game should be able to query a response from this AI submodule. We fill the naive AI with heuristics about the best strategy. Performance of the naive AI serves as benchmark for later experiments.|
|**Week 3** |Buffer|
|**Week 4** |Implement an interface that allows us to run games with all players as AI. The current web interface with its laughable GUI is not required at all for this. Rather, this interface or framework should allow us to program multiple runs of the game with varying set of parameters. In other words, set up an experimentation lab.|
|**Week 5** |Try out Q-Learning examples on the web. There is not sufficient time for us to understand all the mathematics behind RL techniques, but we can understand how to use these as a skill. You can deep dive into the book in references, at your own convenience.|
|**Week 6-7** |Implement Q-learning for our AI|
|**Week 8** |Measure performance against benchmark. This will also involve hyperparameter search and analysing performance across the hyperparameter grid.|
|**Week 9** |Buffer|
|**Week 10**|Documentation Week. You write blogs about your experience, shoot a video etc.

<!--break-->

### Secondary Learning Goals
Apart from learning about RL, you can expect to learn about the following:
- RPC (Remote Procedure Calls)
- FSM (Finite State Machines)
- AWS (Amazon Webservices)

<!--break-->

### References
- [Project Repository](https://github.com/cheekujodhpur/projectlama)
- [Web Game](https://kumar-ayush.com/lama/)
- [RL Book, Sutton & Barto 2nd Ed](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)
- [Q-Learning Tutorial](https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/)
