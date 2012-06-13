---
layout: default
title: James McDermott
permalink: /index.html
---

A list of links:

* [My homepage](http://www.skynet.ie/~jmmcd)
* [My other blog](http://a4.posterous.com)
* [My soundcloud page](http://soundcloud.com/jmmcd)
* [GP Distances](https://github.com/jmmcd/GPDistance)
* [Source for this website](https://github.com/jmmcd/jmmcd.github.com)
* [PonyGE](http://ponyge.googlecode.com)
* [GP Benchmarks](http://groups.csail.mit.edu/EVO-DesignOpt/GPBenchmarks/)
* [Liquid templating](https://github.com/shopify/liquid/wiki/liquid-for-designers)



<div id="home">
  <h2>Blog Posts</h2>
  <ul class="posts">
    {% for post in site.posts %}
      <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
</div>

