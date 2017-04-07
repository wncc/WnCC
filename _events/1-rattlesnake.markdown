---
layout: EventDisplay
image: /images/rattlesnakecover.jpg
title: Rattlesnake
year: 2016
date: "Jan 14 | 2016"
weight: 10
---

This was an introductory session to Python. Students were encouraged to build a tic-tac-toe app ground up using Python 

<!--break-->

The one day workshop was followed by a series of weekly problems which required  interested students to submit their solution in Python.

-[Beginner's Guide to Python](http://wncc-iitb.org/wiki/index.php/Python_Workshop_Resources)

-[Tic-Tac-Toe Code](http://wncc-iitb.org/wiki/index.php/Python_Workshop_Resources)

<!-- jQuery 3.x.x -->
<script src="//code.jquery.com/jquery-3.2.0.min.js"></script>
<!-- jQuery 1.x -->
<script src="//ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<!-- Latest jQuery library -->
<script src="//code.jquery.com/jquery-latest.min.js"></script>
<script src="jquery.slides.js"></script>

<head>
  <style>
    /* Prevents slides from flashing */
    #slides {
      display:none;
    }
  </style>

   <script src="http://code.jquery.com/jquery-latest.min.js">
   </script>
   <script src="jquery.slides.min.js">
   </script>

<script>
    $(function(){
      $("#slides").slidesjs({
        width: 940,
        height: 528
      });
    });

    $(function(){
  	  $("#slides").slidesjs({
    navigation: {
      active: false,
      effect: "fade"
    }
  });
});
 </script>
</head>
<body>
  <div id="slides">
    <img src="/images/rattlesnake1.jpg">
    <img src="/images/rattlesnake2.jpg">
    <img src="/images/rattlesnake3.jpg">
    <img src="/images/rattlesnake4.jpg">
  </div>
</body>
