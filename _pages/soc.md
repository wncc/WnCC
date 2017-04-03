---
layout: default
title: SoC
permalink: /soc/
banner: /images/soc.jpg
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
        <h2>Seasons Of Code</h2>
        <p> an initiative by <a href="https://stab-iitb.org/wncc">The Web and Coding Club, IIT Bombay</a></p>
        <ul class="actions">
            <li><a href="#one" class="button big special">Join The Force</a></li>
        </ul>
        <ul class="actions">
            <li><a href="#two" class="button big special">Projects</a></li>
        </ul>
        <ul class = "actions">
        	<li><a href = "#four" class="button big special">FAQs</a></li>
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
					<a target = "_balnk" href="https://docs.google.com/forms/d/e/1FAIpQLSc5ZqQvIgxVK-Tf-uWEKcyCg2BrDM0Iu4QVj5RzoP6Y5TZtNA/viewform" class="button big special">Become a Padawan</a>
				</section>
			</div>
			<div class="6u">
				<section class="special box">
					<img class="icon major" src="{{ '/svg/light-siber.svg' | prepend: site.baseurl }}" />
					<h3>Master</h3>
					<p>I can feel you code. It gives you focus. It makes you stronger. Your focus determines your reality. Use the force and someday you will be the most powerful Jedi ever.</p>
					<a target = "_blank" href="https://docs.google.com/forms/d/e/1FAIpQLSd57osi_wuufUt9caLo5q3QFXNzjXBhcuaKtj2RTK5OG5JFfw/viewform" class="button big special">Become a Master</a>
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
		{% assign projects = site.soc_projects | sort:"weight"  %}
            {% for project in site.soc_projects%}
            {% if project.ribbon == "completed" %}
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
						<h3>{{ project.title }}</h3>
						<h4>- {{ project.mentor }}</h4>
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
						<h4>- {{ project.mentor }}</h4>
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

<section id="four" class="wrapper style1">
	<div class = "4u">
		<h2>Frequently Asked Questions</h2>
		<section id = "Is the Season of Code(SoC) a recruiting program?">
			<h3>Is the Season of Code a recruiting program?</h3>
			<p>No this is not a recruiting program. If you are interested in working for FOSSEE, please visit this <a href="http://fossee.in/jobs">link</a></p>
		</section>

<section id = "Is SoC considered an internship, a job, or any form of employment?">
			<h3>Is SoC considered an internship, a job, or any form of employment?</h3>
			<p>No. SoC is an activity for only IIT Bombay students perform as independent developers for which they are paid a stipend.
			</p>
		</section>

<section id = "Are mentoring organizations required to use the code produced by students?">
			<h3>Are mentors/mentoring organizations required to use the code produced by students?</h3>
			<p>No. While we hope that all the code that comes out of this program will find a happy home, we don’t require the mentors/organizations to use the student's' code.
			</p>
		</section>

<section id = "Where does SoC occur?">
			<h3>Where does SoC occur?</h3>
			<p>Season of Code occurs entirely online; there is no requirement to travel as part of the program. Although it would be better if done from Institute itself
			</p>
		</section>

<section id = "Do I get a room retention if I am doing SoC">
			<h3>Do I get a room retention if I am doing SoC?</h3>
			<p>No. Activities like ITSP, SURP etc. offer room retention.</p>
		</section>

<section id = "What can I do to help spread the word about GSoC?">
			<h3>What can I do to help spread the word about SoC?</h3>
			<p>You can share the website link. Share the official facebook post and encourage your friends to pariticipate in it!
			</p>
		</section>

<section id = "Can I participate in SoC as both a mentor and a student?">
			<h3>Can I participate in SoC as both a mentor and a student?</h3>
			<p>No. We want to make sure that each project and student receives sufficient attention, and we feel this could create a bad experience for those involved. Please choose whether participation as a mentor or a student is more appealing to you and plan to apply accordingly.
			</p>
		</section>

<section id = "What if I have more questions?">
			<h3>What if I have more questions?</h3>
			<p>Feel free to ping <a href = "https://www.facebook.com/nihal111">Nihal Singh</a> or <a href = "https://www.facebook.com/sajalnarang">Sajal Narang</a>. You can also directly message <a href="https://www.facebook.com/wncc.iitb/">WnCC</a>.
			</p>
		</section>

<section id = "What programming language(s) should I know to participate in SoC?">
			<h3>What programming language(s) should I know to participate in SoC?</h3>
			<p>The programming language you need to know depends on the project you are going select. Learn a new programming language is not a tough job. In the past people with CS 101 as their coding backgrounds have also done SoC. For learning new languages you can refer to <a href = "http://wncc-iitb.org/wiki/index.php/The_Web_and_Coding_Club">Grundy</a>.
			</p>
		</section>

<section id = "Can I submit more than one proposal?">
			<h3>Can I submit more than one proposal?</h3>
			<p>Yes you surely can. Just fill the Padawan form multiple times with links to your proposals.
			</p>	
		</section>

<section id = "Can a group submit a proposal together to work on a single project?">
			<h3>Can a group submit a proposal together to work on a single project?</h3>
			<p>No, only an individual may work on a given project.
			</p>
		</section>

<section id = "Should I send proposals directly to the mentoring organizations?">
			<h3>Should I send proposals directly to the mentoring organizations?</h3>
			<p>No only the proposals given in the Padawan will be considered valid.
			</p>
		</section>

<section id = "What are the eligibility requirements for participation?">
			<h3>What are the eligibility requirements for participation?</h3>
			<p>There is only requirement which is enthusiasm to learn!
			</p>
		</section>

<section id = "How much time does SoC participation take?">
			<h3>How much time does SoC participation take?</h3>
			<p>You are expected to spend around 25+ hours a week working on your project during the 2 month coding period.
			</p>
		</section>
</section>

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
