---
layout: default
title: Showcase
permalink: /showcase/
banner: /images/showcase.jpg
show-in-header: true
---

<!-- Banner -->
<section id="banner" style="background-image:url({{ page.banner | prepend: site.baseurl }})">
    <div class="inner">
        <h2 >Showcase</h2>
        <h3 style="color: #fff; font-weight: 600;">The Hall of Fame</h3>
        <!-- <ul class="actions">
            <li><a href="#one" class="button big special">Join The Force</a></li>
        </ul>
        <ul class="actions">
            <li><a href="#two" class="button big special">Projects</a></li>
        </ul> -->
    </div>
</section>


<!-- Main -->
<section id="main" class="wrapper style1">
    <header class="major">
       <!--  <h2>No Sidebar</h2>
        <p>Tempus adipiscing commodo ut aliquam blandit</p> -->
    </header>
    <div class="container">
    {% assign projects = site.showcase_projects | sort:"weight"  %}
    {% for project in site.showcase_projects%}
        <div class="row">
            <div class="12u">
                <section class="special">
                    <a href="{{ project.repo }}" class="hyperlink-nodecoration">
                        <h2 style="font-weight: 500;" id="{{ project.title }}">{{ project.title }}</h2>
                    </a>
                	<a href="{{ project.website }}" class="image fit">
                        <img src="{{ project.image | prepend: site.baseurl }}" alt="" />
                    </a>
                    <div style="margin: 0 auto;">
                        <a href="{{ project.github }}"><img src="{{ project.avatar }}" alt="" class="avatar"/></a>
                        <a href="{{ project.github }}" class="hyperlink-nodecoration"><h3 style="font-weight: 400;">{{ project.author }}</h3></a>
                    </div>
                    <h4 style="font-weight: 500;">
                    {% if project.category %}
	                    {% for category in project.category %}
	                     • {{ category }}
	                    {% endfor %}
                    {% endif %}
                    </h4>
                    <p>{{ project.content}}</p>
                    <!-- <ul class="actions">
                        <li><a href="#" class="button alt">Learn More</a></li>
                    </ul> -->
                </section>
            <hr class="major" />
            </div>
        </div>
    {% endfor %}
    </div>
</section>
