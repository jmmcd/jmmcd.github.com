jmmcd.github.com
----------------

This is the source code for my blog/small website on github, where I
host some code.


TODO
----

* I want to be able to write ```&not;&not;``` as a bullet point, and
apparently
[it's possible](http://www.alistapart.com/articles/taminglists/), but
I can't make it work yet.

    #custom-gen ul li:before {
    content: "\00BB \0020";
    }
	    

* I want to able to write something like ```{% include /code/ga.py
  %}``` in my posts, and get a source code file included and
  highlighted.
