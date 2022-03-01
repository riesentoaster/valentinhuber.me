---
title: fragen
language: deutsch
---
- Eine Frage [vorschlagen](mailto:frage@valentinhuber.me?subject=Vorschlag für eine Frage)
- Eine [zufällige Frage](/fragen/random.html) generieren

{% for cat in site.data.fragen %}

## {{cat.title}}
> [Zufällige Frage aus {{ cat.title }}](/fragen/random.html?category={{cat.title}})
{% for frage in cat.entries %}
- {{ frage -}}
{% endfor -%}
{% endfor -%}