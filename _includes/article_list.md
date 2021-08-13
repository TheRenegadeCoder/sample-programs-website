<ul>
{% if include.collection %}
  {% assign sorted_posts = (include.collection | sort: 'title') %}
  {% for article in sorted_posts %}  
    {% assign date = article.date | date_to_long_string %}
    {% assign author = article.authors | first %}
    {% assign author = site.data.authors[author].name %}
    {% unless article.url == page.url %}
      <li>
        <a href="{{ article.url | relative_url }}">{{ article.title }}</a> on {{ date }} by {{ author }}
      </li>
    {% endunless %}
  {% endfor %}
{% else %}
Currently, there are no articles. If you'd like to begin contributing, head
over to the repo to get started.
{% endif %}
</ul>
