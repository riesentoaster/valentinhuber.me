---
layout: overview
header: blog
title: blog
---
## categories
{% assign cats = "" | split: ","%}
{% for c in site.categories %}
  {% assign thiscat = c | first | split: " "%}
  {% assign cats = cats | concat: thiscat %}
{%- endfor %}
{% assign cats = cats | sort %}

{% for c in cats %}
- [{{c}}]({{c}})
{%- endfor %}


---

## languages
{% for l in site.data.languages -%}
{% assign posts = site.posts | where: "language", l.name -%}
{% if posts != empty %}
- [{{l.name}}]({{l.overview}})
{%- endif -%}
{% endfor %}

## all posts