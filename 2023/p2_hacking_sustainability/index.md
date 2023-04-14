---
layout: default
exclude: False
---

# Hacking Sustainability

{% for article in site.pages %}
    {% if article.identifier == 'p2_2023' %}
    {% if article != page %}
{% if article.image %}
<img class="p2-img" src="{{article.image}}"/>
{% endif %}
  <strong><a href="{{ article.url | relative_url }}">{{ article.title }}</a></strong><br/>
<small>_By {{ article.author }}_.</small>
<br/>
<small>{{ article.summary | truncate: 350 }}</small>
<br/>
<small>[Paper]({{article.paper}}).</small>
{%- if article.website %}
<small>[Website]({{article.website}}).</small>
{% endif -%}
{%- if article.source -%}
<small>[Source code]({{article.source}}).</small>
{% endif -%}
<br/>
<div class="clearfix"></div>
  {% endif %}
  {% endif %}
{% endfor %}



<br/><br/><br/><br/>

---


## How to contribute

To add a new article, follow the instructions below:

1. Fork the repo of the website on Github: <https://github.com/luiscruz/course_sustainableSE/>
2. Create a new markdown file inside the directory `2023/p2_hacking_sustainability`
  - Use the following filename format: `g<group_number>_<1/2meaningful_keywords>.md`
  - Use the file `gX_template.md` has a template
  - If you want to add images, add it to `2023/img/p2_hacking_sustainability/g<group_number>_<1/2meaningful_keywords>/`
3. Commit, Push.
4. Submit a pull request.

**Explaining the template.** Although it is a markdown (.md) file, you will only be filling the YAML header with some keys and values. In particular, you must fill `author`, `title`, `summary` with a quick description of the project (max 200 characters), and `paper` with a url link to the paper. **Optionally**, you can also fill `image` with the url of a logo or image related to the project, `source` with a link to the source code of the project, and `website` with a link to the project's website **when applicable**.

Before submitting the pull request, you should test whether your file is rendering properly in the website. The easiest way to check it is by running the docker container, as instructed in the Github Readme.

Your page should be listed here: http://localhost:4000/course_sustainableSE/2023/p2_hacking_sustainability

If you don't want to deal with jekyll, you can do it the slow and expensive way: 1) enable *github pages* in your fork repo 2) check your the deployed page. (I don't recommend it, though)

*Note: let me know if you run into any issue or if there's any step you think should be explained here.*

