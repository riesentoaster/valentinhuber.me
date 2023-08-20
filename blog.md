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

## all posts