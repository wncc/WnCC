---
layout: default
title: Events
permalink: /events/
banner: /images/events.jpg
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
        <h2>Events</h2>
    </div>
</section>


<!-- Two -->
<section id="two" class="wrapper style1">
	<header class="major">
		<h2>List of Events</h2>
		<p>Go on. Check them out.</p>
	</header>

<div class="tab" style="text-align : center">
  <button class="tablinks" onclick="openType(event, '2017')" id="defaultOpen">2017</button>
  <button class="tablinks" onclick="openType(event, '2016')" id="tab2016">2016</button>
</div>
<br/>

<div id="2016" class="tabcontent">
	<div class="container">
		{% assign eventList = site.events | sort:"weight"  %}
            {% for event in site.events%}
	            {% if event.year == 2016 %}
		            {% capture modulo %}{{ forloop.index0 | mod:3 }}{% endcapture %}
		            {% capture thecycle %}{% cycle '0', '1' ,'2' %}{% endcapture %}
		            <!-- Creating a new row after every three elements -->
		            {% if thecycle == '0' or forloop.first %}
		            	<div class="row">
		            {% endif %}
						<div class="4u">
							<section class="special">
								<a href="{{ event.url | prepend: site.baseurl }}" class="image fit">
									<img src="{{ event.image | prepend: site.baseurl }}" alt="{{ event.title }}"/>
								</a>
		                        <a href="{{ event.url | prepend: site.baseurl }}" class="image fit">
		                        	<h3>{{ event.title }}</h3>
		                        </a>
								<h4>{{ event.date | date: "%B %-d, %Y"}}</h4>
								<p>{{ event.content | split:'<!--break-->' | first }}</p>
								<ul class="actions">
									<li><a href="{{ event.url | prepend: site.baseurl}}" class="button alt">Learn More</a></li>
								</ul>
							</section>
						</div>
					{% if thecycle == '2' or forloop.last %}
		    			</div>
					{% endif %}
				{% endif %}
            {% endfor %}
		<div style="text-align: center;">
		<!-- <a href="#" class="button big special">View All Events</a> -->
		</div>
	</div>
</div>

<div id="2017" class="tabcontent">
	<div class="container">
		{% assign eventList = site.events | sort:"weight"  %}
            {% for event in site.events%}
	            {% if event.year == 2017 %}
		            {% capture modulo %}{{ forloop.index0 | mod:3 }}{% endcapture %}
		            {% capture thecycle %}{% cycle '0', '1' ,'2' %}{% endcapture %}
		            <!-- Creating a new row after every three elements -->
		            {% if thecycle == '0' or forloop.first %}
		            	<div class="row">
		            {% endif %}
						<div class="4u">
							<section class="special">
								<a href="{{ event.url | prepend: site.baseurl }}" class="image fit">
		                            <img src="{{ event.image | prepend: site.baseurl }}" alt="{{ event.title }}" />
		                        </a>
		                        <a href="{{ event.url | prepend: site.baseurl }}" class="image fit">
									<h3>{{ event.title }}</h3>
								</a>
								<h4>{{ event.date | date: "%B %-d, %Y"}}</h4>
								<p>{{ event.content | split:'<!--break-->' | first }}</p>
								<ul class="actions">
									<li><a href="{{ event.url | prepend: site.baseurl}}" class="button alt">Learn More</a></li>
								</ul>
							</section>
						</div>
					{% if thecycle == '2' or forloop.last %}
		    			</div>
					{% endif %}
				{% endif %}
            {% endfor %}
		<div style="text-align: center;">
		<!-- <a href="#" class="button big special">View All Events</a> -->
		</div>
	</div>
</div>
</section>



<script>
function openType(event, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    var newurl;
    newurl="{{site.baseurl}}"+"{{page.permalink}}"+"?year="+cityName; 
    window.history.pushState({path:newurl},'',newurl);
    
    document.getElementById(cityName).style.display = "block";
    event.currentTarget.className += " active";
}
var link="{{page.permalink}}"+"?year=";
if (document.URL.endsWith(link + "2016")) {
    document.getElementById("tab2016").click();
}
else {
    document.getElementById("defaultOpen").click();
}

</script>			



