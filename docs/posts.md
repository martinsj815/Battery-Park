---
layout: default
title: Battery Park
description: From Chemistry to Technology
---

# Posts <i class="arrow right"></i>

<hr style="background: linear-gradient(#4a8049, #d8f5d0); height: 5px; border: none;">
<br><br>

{% for post in site.posts %}
  <article class="post">
    <p class="post-date">{{ post.date | date: "%B %d, %Y" }}</p>
    <p>{{ post.excerpt }}</p>
    <a href="{{ post.url | relative_url }}">link</a>
    <br>
  </article>
{% endfor %}
