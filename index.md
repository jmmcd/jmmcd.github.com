---
layout: default
title: James McDermott
permalink: /index.html
---

James McDermott
====================



<div>
  <h2>Blog Posts</h2>
  <ul class="posts">
{% for post in site.posts %}
    <li><a href="{{ post.url }}">{{ post.title }}</a><span>{{ post.date | date_to_string }}</span> </li>
    {% endfor %}
</ul>
</div>

