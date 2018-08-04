---
layout: soc-project
image: /images/cheeku-montecarlo.gif
title: Monte Carlo Path Tracing Renderer
mentor: "Kumar Ayush"
category: "Computer Graphics"
application_procedure: "proposal"
weight: 65
ribbon: in progress
stipend: INR 3000
contact:
- Facebook - <a target="_blank" href="https://www.facebook.com/cheekujodhpur">Kumar Ayush</a>
- <a target="_blank" href="mailto:https://cheekujodhpur@gmail.com">Email ID</a> - cheekujodhpur@gmail.com
mentees:
- Abeen Bhattacharya
- Sneha Sunil Bhakare
- Darshan Tank
- Navnit Kumar

---

---

This internship involves the implementation of a Monte Carlo Path Tracer.

<!--break-->

### Monte Carlo Path Tracing Renderer
In this project, you will implement a Monte Carlo Path Tracer. A path tracer is a kind of renderer in computer graphics. A renderer is responsible for generating the image or the graphics that you see on your screen. Even this text that you are reading is displayed via a font renderer. Path tracers are often used for photorealistic rendering, which means generating an image indistinguishable from a photograph. At the end of the project, you can expect to have a code capable of producing such images.

<!--break-->

As a primer, you should read Andrew Glassner's [Introduction to Ray Tracing](https://www.goodreads.com/book/show/1441550.An_Introduction_to_Ray_Tracing)

<!--break-->

### Pre-requisites
- At least two years of experience with CPP, awareness of gcc and make
- A basic course on DSA

<!--break-->

### Tentative Project Timeline

I expect about 100 hours of work spread over ten weeks.

<!--break-->

|Week Number  | Tasks to be Completed|
|--- | --- | 
|**Week 1** |Read the book|
|**Week 2** |Write an XML parser. This is the submodule that reads the scene.|
|**Week 3** |Write the skeleton of the graphics pipeline. This involves implementing coordinate transformations|
|**Week 4** |Implement the Ray and Object class. Most of the Path Tracing routine can be summarised as measuring intersection of instances of Ray class with instances of the Object class.|
|**Week 5** |Implement Direct Lighting and Whitted Ray Tracing|
|**Week 6** |Implement Recursive Rays to capture higher order light paths|
|**Week 7** |Debugging buffer & Implement Jittering and Supersampling|
|**Week 8** |Monte Carlo enters. Learn Sampling. Implement Diffuse Sampling and Area lights. Effects like soft shadows and colour bleeding start to appear|
|**Week 9** |Debugging Buffer|
|**Week 10**|Documentation, Generating Scenes, Videos

<!--break-->

### Secondary Learning Goals
Apart from learning about path tracers and rendering, you can expect to learn about the following:
- Monte Carlo Sampling
- Basics of ImageMagick
- OpenMP Parallelization.

<!--break-->

### Repositories
The project will be done in groups of two. We will consider minor variations
in the raytracers, Swati ([swati-rt](https://github.com/wncc/swati-rt)) and Revati ([revati-rt](https://github.com/wncc/revati-rt))
