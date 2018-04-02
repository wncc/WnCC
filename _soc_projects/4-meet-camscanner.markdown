---
layout: soc-project
image: /images/camscanner.jpg
title: Panorama in Cam-Scanner
mentor: "Meet Udeshi"
category: "Image Processing"
weight: 75
ribbon: completed
stipend: INR 3000
contact:
- <a target="_blank" href="https://gitter.im/wncc/SoC_CamScanner">Gitter</a>
- Facebook- <a target="_blank" href="https://www.facebook.com/udiboy1209">Meet Udeshi</a>
mentees:
- Nived
- Bhishma Dedhia
---

Each one of us must have used the Cam-scanner app on Android phones for quick and good quality scanning of documents. But what if you have to scan a really big document? Or maybe you want to capture more detail?

<!--break-->

We will be looking at ways to capture multiple images of sections of a single document and "stitching" them together to get a scan-quality image, using methods very similar to those used for capturing panorama images. Though it is more fun to experiment with the algorithms using test images, at the end of the project one can hope for an Android app which implements this stitching in real time.

Referenes-

- [https://github.com/udiboy1209/cs663-document-scanner](https://github.com/udiboy1209/cs663-document-scanner)
- [https://github.com/udiboy1209/cs663-document-scanner/blob/master/report/doc_scan.pdf](https://github.com/udiboy1209/cs663-document-scanner/blob/master/report/doc_scan.pdf)


### Week 0
* Finalization of algorithm to calculate inliers
* Implemented Feature Detection using ORB
* Currently working on Feature Matching  

### Week 1
* Implemented Feature Matching and ORB
* Identified Issues in Feature Detection
* Resolved Mixed Color Channel Issue

### Week 2
* Optimized ORB and Feature Matching algo
* Added Image Alignment
* Started working on Homography

### Week 3
* Warping Images to Global Coordinate
* Implemented Image Averaging
* Working on Multiband Blending
