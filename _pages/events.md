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
    padding: 2%;	
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

{% assign years = 'a,b' |split: ',' %}
{% assign years = years |pop: 2 %}
{% for event in site.events %}
	{% assign years = years |push: event.year %}
{% endfor %}

{% assign years = years |uniq %}

<div class="tab" style="text-align : center">
{% for year in years%}
 <button class="tablinks" onclick="openType(event, '{{ year }}')" {% if forloop.last %} id="defaultOpen" {% endif %}> {{ year }}
 </button>
{% endfor %}
<br/><br/>

{% for year in years%}
<div id="{{ year }}" class="tabcontent">
	<div class="container">

				{% assign eventList = 'a,b' |split: ',' %}
				{% assign eventList = eventList | pop: 2 %}
	            {% for event in site.events %}
		            {% if event.year == year %}
		            	{% assign eventList = eventList |push: event %}
		            {% endif %}
	            {% endfor %}
              {% assign eventList = eventList | sort: "weight" %}
	            {% for event in eventList reversed %}
		            {% capture thecycle %}
		            {% cycle year: '0', '1' ,'2' %}
		            {% endcapture %}
                    {% assign cycleidx = thecycle | plus: 0 %}
		            {% if cycleidx == 0 or forloop.first %}
		            <!-- Creating a new row after every three elements -->
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
					{% if cycleidx == 2 or forloop.last %}
		    			</div>
					{% endif %}	
            {% endfor %}

		<div style="text-align: center;">
		<!-- <a href="#" class="button big special">View All Events</a> -->
		</div>
	</div>
</div>
{% endfor %}




<script>
function openType(evt, year) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(year).style.display = "block";
    evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();

</script>			


