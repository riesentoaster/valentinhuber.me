---
layout: overview
header: blog
title: blog
---
## categories
{% for c in site.categories %}
- [{{c | first}}](/{{c | first}})
{% endfor %}

## languages
{% for l in site.data.languages %}
{% assign posts = site.posts | where: "language", l.name %}
{% if posts != empty %}
- [{{l.name}}]({{l.overview}})
{% endif %}
{% endfor %}

## all posts