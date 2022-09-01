jmmcd.github.com
----------------

This is the source code for
[my blog/small website on github](http://jmmcd.github.com), where I
host some code. It uses Github pages, which uses Jekyll, which uses
Liquid templating and Markdown. Thanks to
[uberduper](http://danhixon.github.com/), one of the Github pages
example pages: I've copied some css and layouts from there.



TODO
----

* I want to be able to write ```&not;&not;``` as a bullet point, and
apparently
[it's possible](http://www.alistapart.com/articles/taminglists/), but
I can't make it work yet. It would use something like this:
```#custom-gen ul li:before {content: "\00BB \0020";}```


* I want to able to write something like ```{% include /code/ga.py
%}``` in my posts, and get a source code file included and
highlighted.
