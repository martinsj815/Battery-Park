---
layout: default
title: Battery Park
description: From Chemistry to Technology
---


# Welcome to Battery Park!
<br><br>

<div class="content-container">
    <div class="columns">
        <div class="column">
            <ul>Batteries play a crucial role in our daily lives, powering everything from smartphones to electric vehicles. As the demand for higher performance increases and the availability of battery constituent resources becomes scarcer, there is an urgent need to concentrate on developing batteries with optimized parameters through efficient resource allocation.</ul>
            <ul>The website is tailored to provide comprehensive information spanning from their fundamental chemistry to their present utilization across industries. We welcome technology enthusiasts, students, and even industry professionals seeking knowledge and insights from this fascinating realm of science and technology.</ul>
        </div>
        <div class="column">
            <img src="https://github.com/donghee1025/Battery-Park/blob/main2/docs/image_home.jpg?raw=true" alt="ECell" style="width:500px; height:auto;">
        </div>
    </div>
    <div class="sidebar" style="flex: 30%; padding: 15px; border-left: 1px solid #ddd;">
        <section class="latest-posts" style="margin-bottom: 20px;">
            <h2>Latest Posts</h2>
            {% for post in site.posts limit:3 %}
            <div class="sneak-peek" style="border: 2px solid #ddd; border-radius: 8px; padding: 10px; margin-bottom: 15px;">
                <h3>&#9656; <a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
            </div>
            {% endfor %}
        </section>
        <div style="border-top: 3px solid #007ACC; margin: 20px 0;"></div>
        <section class="calculator" style="border: 2px solid #ddd; border-radius: 8px; padding: 10px;">
            <h2>Check out the Calculator</h2>
            <div class="sneak-peek">
                <h3><a href="https://martinsj815.github.io/Battery-Park/Calculator">Go to the link</a></h3>
            </div>
        </section>
    </div>
</div>
