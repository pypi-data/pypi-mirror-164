"""
Template filter for search views
"""

# Standard Library
import re

# Django
from django.template.defaulttags import register
from django.utils.safestring import mark_safe

# AA Forum
from aa_forum.constants import SEARCH_STOPWORDS


@register.filter
def highlight_search_term(text: str, search_phrase: str) -> str:
    """
    Highlight the search term in search results
    :param text:
    :param search_phrase:
    :return:
    """

    querywords = search_phrase.split()
    search_phrase_terms = [
        word for word in querywords if word.lower() not in SEARCH_STOPWORDS
    ]
    highlighted = text

    for search_term in search_phrase_terms:
        highlighted = re.sub(
            f"(?i)({(re.escape(search_term))})", "{«}\\1{»}", highlighted
        )

    return mark_safe(
        highlighted.replace(
            "{«}", '<span class="aa-forum-search-term-highlight">'
        ).replace("{»}", "</span>")
    )
