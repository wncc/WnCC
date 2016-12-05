---
layout: soc-project
image: /images/meteor.jpg
title: Photometric Redshift
mentor: "Kumar Ayush"
category: Scientific Computing
weight: 80
mentees:
- Kaustubh Vyas
- Kaushik Vyas
- Kalpesh Krishna
---
A scientific computing project aimed at calculating redshifts of extra-galactic objects from photometric data.

<!--break-->

<p>
Redshifts caluclated from spectroscopic data is accurate but it is time expensive to measure the spectrum. There is a correlation between photometric data which is easier and faster to measure and the redshift which can be used to calculate <i>photometric</i> redshifts. We are currently trying to write a neural network in Keras to compute photometric z from photometric magnitudes.
</p>

<h3>Week 1</h3>
<ul>
    <li>Make SkyServer accounts</li>
    <li>Get familiar with SQL</li>
    <li>Look into how CasJobs work</li>
    <li>Look into DR12 data schema</li>
</ul>
<h3>Week 2</h3>
<ul>
    <li>Get data from DR12.SpecPhotoAll</li>
    <li>Filtering bad data out</li>
    <li>Trying K-nearest neighbour training from scikit learn</li>
    <li>Try simple Neural Network Models on Keras</li>
    <li>Single hidden layer with mse loss and RMSprop optimizer works average, with sigmoid activation on last layer</li>
    <li>Our inputs are psf_Mag_u/g/i/r/z and/or their linear combinations but all of them give the same output</li>
    <li>We suspect we still have a lot of bad data in various form and heavier pre-processing is needed</li>
</ul>
