---
layout: default
---

<div id="post">
{{ content }}
</div>

{% if site.disqus %}
  <div id="comments">
    <h2>Comments</h2>
    <div id="disqus_thread"></div>
    <script type="text/javascript">
      var disqus_identifier = "{{ page.url }}";
      (function() {
       var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
       dsq.src = 'http://{{ site.disqus.id }}.disqus.com/embed.js';
       (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
      })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript={{ site.disqus.id }}">comments powered by Disqus.</a></noscript>
    <a href="http://disqus.com" class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a>
  </div>
{% endif %}


<div id="related">
  <h3>Related Posts</h3>
  <ul class="posts">
    {% for post in site.related_posts limit:3 %}
      <li><a href="{{ post.url }}">{{ post.title }}</a><span>{{ post.date | date_to_string }}</span> </li>
    {% endfor %}
  </ul>
</div>

