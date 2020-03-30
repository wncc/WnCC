---
layout: soc-project
image: /images/workbench_tool.png
title: Computer Vision Workbench
mentor: 
- Vishal Kaushal
category: "Development, Image Processing, Machine Learning, Deep Learning"
application_procedure: "proposal"
mentees:
- Aniket Sadashiva
weight: 46
ribbon: new
contact: 
- Email/Hangouts - vishal.kaushal@gmail.com
---

---

Extracting potentially useful information from videos, like presence of faces, humans, specific objects, motion, tracking etc. is an indispensable part of video analysis.

<!--break-->

Recent advancements in deep learning have demonstrated good accuracies on many of these tasks, however these models do not yet generalize well to the unseen real-world deployments.

<!-- break-->

Though the accuracy numbers for these off the shelf models have been reported and can be computed on standard existing datasets, there is currently no way to estimate how would these models perform when challenged in real-world deployments. This makes it necessary to have at least a qualitative comparison of different models against each other on such challenging, unlabelled videos.

<!-- break-->

To enable this, we envision a workbench tool (Python GUI) which will make it easy to compare any two models on a given video for a given task and "see" how they perform. It will be released as open source software. This tool will help understand the "real" strengths and weaknesses of different models for different tasks and will help give important directions to undertake future research.

<!-- break-->

To begin with we can focus on the following computer vision tasks: Motion detection, Face detection, Face recognition, Human detection, Head detection, Object detection, Tracking. A typical use of this tool will involve selecting the task, selecting a video, selecting two models/algorithms to compare and as a result seeing a side by side comparison of the analyzed video played synchronously along with other measurable parameters like time taken etc.

<!--break-->

### Tentative Timeline:

| Week | Work |
| --- | --- |
|Week 1  | Understanding the various computer vision tasks involved |
|Week 2  | Motion Detection - stand alone implementations using various alternate techniques |
|Week 3  | Face Detection - stand alone implementations using various alternate off the shelf models/techniques |
|Week 4  | Object detection - stand alone implementations using various alternate off the shelf models/techniques |
|Week 5  | Tool design, architecture and skeleton implementation |
|Week 6  | Integrating motion detection in tool |
|Week 7  | Integrating face detection in tool |
|Week 8  | Integrating object detection in tool |
|Week 9  | Face recognition |
|Week 10 | Human detection |
|Week 11 | Head detection |
|Week 12 | Tracking |
|Week 13 | Buffer/Enhancements/Closure |
