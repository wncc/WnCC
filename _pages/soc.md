---
layout: default
title: SoC
permalink: /soc/
banner: /images/soc.jpg
show-in-header: true
---

<head>
	<style>
    div.tab {
    float : center;
    align-content: :center;
    width: 100%;
    overflow: hidden;
    border: 1px solid #ccc;
    background-color: #f1f1f1;
}

/* Style the buttons inside the tab */
div.tab button {
    background-color: inherit;
    float: center;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 14%;
    transition: 0.3s;
    font-size: 25px;
}

/* Change background color of buttons on hover */
div.tab button:hover {
    background-color: #ddd;
}

/* Create an active/current tablink class */
div.tab button.active {
    background-color: #ccc;
}


    .tabcontent {

    display: none;
    padding: 6px 12px;
    border: 1px solid #ccc;
    border-top: none;
}

</style>
</head>

<!-- Banner -->
<section id="banner" style="background-image:url({{ page.banner | prepend: site.baseurl }})">
    <div class="inner">
        <h2>Seasons Of Code 2018</h2>
        <p> An Initiative By <a href="https://www.wncc-iitb.org/">The Web and Coding Club, IIT Bombay</a><br/><br/>
        Tentative Dates: <a href="https://calendar.google.com/event?action=TEMPLATE&tmeid=N3ZxOHNlNDFtcnY2bzFhNXJpZjVmbDk2MDMgYWJlZW45QG0&tmsrc=abeen9%40gmail.com">16th May - 16th July</a></p>
        <ul class="actions">
            <li><a href="#one" class="button big special">Join The Force</a></li>
        </ul>
        <ul class="actions">
            <li><a href="#two" class="button big special">Projects</a></li>
        </ul>
        <ul class = "actions">
        	<li><a href = "faq.html" class="button big special">FAQ</a></li>
        </ul>
    </div>
</section>

<!-- Three -->
<section id="three" class="wrapper style1">
	<div class="container">
		<div class="row">
			<div class="8u">
				<section>
					<h2>What is Seasons of Code?</h2>
					<a href="#" class="image fit"><img src="{{ '/images/coding.jpg' | prepend: site.baseurl }}" alt="" /></a>
					<p>Seasons of Code is a programme launched by the WnCC, along the lines of GSoC without much greenery though. The incentive is similar to ITSP, based on the current form of it, the fundamental difference is that one can choose from the ideas offered by mentors who are senior undergrads, doctorate students or professors, and in some exceptional cases, startups. We plan to have a really long timeframe though, until the next winter extending this programme into a mentorship of sorts into the semester. It is not just about development by the way. We have some mentors ready to take up programmes regarding competitive coding and scientific computation too.
					</p>
				</section>
			</div>
			<div class="4u">
				<section>
					<h3>Why should you participate?</h3>
					<p>Seasons of Code gives you an amazing opportunity to learn and dive into coding under the mentorship of the best in our institute. Our list of projects gives you a chance to pick up and work on any topic you are enthusiastic about.</p>
					<ul class="actions">
						<li><a href="#two" class="button alt">Projects</a></li>
					</ul>
				</section>
				<hr />
				<section>
					<h3>Types of Projects</h3>
					<ul>
						<li>Development</li>
						<li>Open Source</li>
						<li>Scientific Computation</li>
						<li>Competitive Coding</li>
					</ul>
				</section>
			</div>
		</div>
	</div>
</section>

<section id="one" class="wrapper style2">
	<header class="major">
		<h2>Join The Force</h2>
		<p>Do. Or do not. There is no try.</p>
	</header>
	<div class="container">
		<div class="row">
			<div class="6u">
				<section class="special box">
					<img class="icon major" src="{{ '/svg/light-siber-one.svg' | prepend: site.baseurl }}" />
					<h3>Padawan</h3>
					<p>The Force is strong with you. Train yourself to let go of everything you fear to lose. The Force will be with you always. Ready are you?</p><br>
					<a target = "_blank" href="https://docs.google.com/forms/d/e/1FAIpQLScF3u5o_D-6G4E8-jl5ftqDN27tLpnAmR5ThE81OKrMHuFzuQ/viewform?usp=sf_link" class="button big special">Become a Padawan</a>
				</section>
			</div>
			<div class="6u">
				<section class="special box">
					<img class="icon major" src="{{ '/svg/light-siber.svg' | prepend: site.baseurl }}" />
					<h3>Master</h3>
					<p>I can feel you code. It gives you focus. It makes you stronger. Your focus determines your reality. Use the force and someday you will be the most powerful Jedi ever.</p>
					<a target = "_blank" href="https://goo.gl/forms/1WXW4oSDwlCHD4313" class="button big special">Become a Master</a>
				</section>
			</div>
		</div>
	</div>
</section>

<!-- Two -->
<section id="two" class="wrapper style1">
	<header class="major">
		<h2>List of Projects</h2>
		<p>Your eyes can deceive you. Don’t trust them.</p>
	</header>

<div class="tab" style="text-align : center">
  <button class="tablinks" onclick="openType(event, 'running')" id="defaultOpen">Running Projects</button>
  <button class="tablinks" onclick="openType(event, 'completed')">Completed Projects</button>
</div>
<br/>

<div id="completed" class="tabcontent">
<div class="container">
<!-- the following line is optional to sort by weight -->
		{% assign projects = site.soc_projects | sort:"weight"  %}
            {% for project in site.soc_projects%}
            {% if project.ribbon == "completed" %}
            {% capture modulo %}{{ forloop.index0 | mod:3 }}{% endcapture %}
            {% capture thecycle %}{% cycle '1', '2' ,'3' %}{% endcapture %}
            <!-- Creating a new row after every three elements -->
            {% if thecycle == '1' or forloop.first %}
            	<div class="row">
            {% endif %}
				<div class="4u">
					<section class="special">
						<a href="{{ project.url | prepend: site.baseurl }}" class="image fit">
                            <img src="{{ project.image | prepend: site.baseurl }}" alt="{{ project.title }}" />
                            <!-- {% if page.ribbon != '' %} -->
                            <div class = "ribbon {{project.ribbon}}"><span>{{project.ribbon}}</span></div>
                            <!-- {% endif %} -->
                        </a>
                        <a href="{{ project.url | prepend: site.baseurl }}" class="image fit">
						<h3>{{ project.title }}</h3>
						</a>
						<h4>-
						{% for mentor in project.mentor%}
				            {{ mentor }}&nbsp;
			        	{% endfor %}</h4>
						<h4>- {{ project.category }}</h4>
						<p>{{ project.content | split:'<!--break-->' | first }}</p>
						<ul class="actions">
							<li><a href="{{ project.url | prepend: site.baseurl}}" class="button alt">Learn More</a></li>
						</ul>
					</section>
				</div>
			{% if thecycle == '3' or forloop.last %}
    			</div>
			{% endif %}
			{% endif %}
            {% endfor %}
		<div style="text-align: center;">
		<!-- <a href="#" class="button big special">View All Projects</a> -->
		</div>
	</div>
</div>

<div id="running" class="tabcontent">
<div class="container">
		{% assign projects = site.soc_projects | sort:"weight"  %}
            {% for project in site.soc_projects%}
            {% if project.ribbon != "completed" %}
            {% capture modulo %}{{ forloop.index0 | mod:3 }}{% endcapture %}
            {% capture thecycle %}{% cycle '0', '1' ,'2' %}{% endcapture %}
            <!-- Creating a new row after every three elements -->
            {% if thecycle == '0' or forloop.first %}
            	<div class="row">
            {% endif %}
				<div class="4u">
					<section class="special">
						<a href="{{ project.url | prepend: site.baseurl }}" class="image fit">
                            <img src="{{ project.image | prepend: site.baseurl }}" alt="{{ project.title }}" />
                            <!-- {% if page.ribbon != '' %} -->
                            <div class = "ribbon {{project.ribbon}}"><span>{{project.ribbon}}</span></div>
                            <!-- {% endif %} -->
                        </a>
                        <a href="{{ project.url | prepend: site.baseurl }}" class="image fit">
						<h3>{{ project.title }}</h3>
						</a>
						<h4>-
						{% for mentor in project.mentor%}
				            {{ mentor }}&nbsp;
			        	{% endfor %}</h4>
						<h4>- {{ project.category }}</h4>
						<p>{{ project.content | split:'<!--break-->' | first }}</p>
						<ul class="actions">
							<li><a href="{{ project.url | prepend: site.baseurl}}" class="button alt">Learn More</a></li>
						</ul>
					</section>
				</div>
			{% if thecycle == '2' or forloop.last %}
    			</div>
			{% endif %}
			{% endif %}
            {% endfor %}
		<div style="text-align: center;">
		<!-- <a href="#" class="button big special">View All Projects</a> -->
		</div>
	</div>
</div>



<script>
function openType(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();

</script>			
