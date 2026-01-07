---
layout: default
exclude: False
---

# Measuring Software Energy Consumption

{% assign articles = site.pages | sort: 'group_number' %}
{% for article in articles %}
    {% if article.identifier == 'p1_measuring_software_2026' %}
    {% if article != page %}
{% if article.image %}
<img class="p2-img" src="{{article.image}}"/>
{% endif %}
<strong><a href="{{ article.url | relative_url }}">Group {{ article.group_number }}: {{ article.title }}</a></strong><br/>
<!-- <small>Posted on {{article.date | date_to_string}}.</small><br/> -->
<small>
{%- if article.authors %}
_By {{ article.authors | map: 'name' | join: ', '}}_
{% else %}
_By {{ article.author }}_
{% endif -%}
.</small>
<br/>
<small>{{ article.summary | truncate: 200 }}</small>
<div class="clearfix"></div>
<br/>
  {% endif %}
  {% endif %}
{% endfor %}

---

## How to contribute

To add a new article, follow the instructions below:

1. Fork the repo of the website on Github: <https://github.com/luiscruz/course_sustainableSE/>
2. Create a new markdown file inside the directory `2026/p1_measuring_software`
  - Use the file `gX_template.md` as a template
  - Use the following filename format: `g<group_number>_<1/2meaningful_keywords>.md`
  - If you want to add images, add it to `2025/p1_measuring_software/img/g<group_number>_<1/2meaningful_keywords>/`
3. Commit, Push.
4. Submit a pull request.

Before submitting the pull request, you should test whether your file is rendering properly in the website. The easiest way to check it is by running the docker container, as instructed in the Github Readme.

Your page should be listed here: http://localhost:4000/course_sustainableSE/2025/p1_measuring_software

If you don't want to deal with jekyll, you can do it the slow and expensive way: 1) enable *github pages* in your fork repo 2) check your the deployed page. (I don't recommend it, though)

*Note: let me know if you run into any issue or if there's any step you think should be explained here.*

