---
layout: default
title: Blogs
permalink: /blogs/
banner: /images/blogs.jpg
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
        <h2 style="font-weight: 400;">WnCC Blogs</h2>
        <h3 style="color: #ffffff;  font-size : 40px;">We code. We blog. We conquer.</h3>
        <!-- <ul class="actions">
            <li><a href="#one" class="button big special">Join The Force</a></li>
        </ul>
        <ul class="actions">
            <li><a href="#two" class="button big special">Projects</a></li>
        </ul> -->
    </div>
</section>


<!-- One -->
<section id="one" class="wrapper style2">
	<header class="major">
		<h2>List of Blog Posts:</h2>
		<p>Good judgment comes from experience, and experience comes from bad judgment. Turn your wounds into wisdom.</p>
	</header>
<div class="container">
<!-- the following line is optional to sort by weight -->
		{% assign projects = site.blogs | sort:"weight"  %}
            {% for project in site.blogs%}
            {% capture modulo %}{{ forloop.index0 | mod:2 }}{% endcapture %}
            {% capture thecycle %}{% cycle '1', '2' %}{% endcapture %}
            <!-- Creating a new row after every three elements -->
            {% if thecycle == '1' or forloop.first %}
            	<div class="row">
            {% endif %}
				<div class="6u">
					<section class="special">
						<a href="{{ project.url | prepend: site.baseurl }}" class="image fit">
                            <img src="{{ project.image | prepend: site.baseurl }}" alt="{{ project.title }}" />
                        </a>
                        <a href="{{ project.url | prepend: site.baseurl }}" class="image fit">
						<h2>{{ project.title }}</h2>
						</a>
						<h3>-
						{% for author in project.author%}
				            {{ author }}&nbsp;
			        	{% endfor %}</h3>
			        	{% if project.category %}
						<h4>- {{ project.category }}</h4>
						{% endif %}
						<h4>{{ project.description }}</h4><br>
						<ul class="actions">
							<li><a href="{{ project.url | prepend: site.baseurl}}" class="button alt">Read More</a></li>
						</ul>
					</section>
				</div>
			{% if thecycle == '2' or forloop.last %}
    			</div>
			{% endif %}
			{% endfor %}
		<div style="text-align: center;">
		<!-- <a href="#" class="button big special">View All Blogs</a> -->
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
