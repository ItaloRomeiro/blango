from django import template
from django.utils.html import format_html
from blog.models import Post

register = template.Library()

@register.filter(name="author_details")
def author_details(author, current_user=None):
    # Se o autor for o usuário atual, exibir "me"
    if current_user and hasattr(current_user, "id") and author and getattr(author, "id", None) == current_user.id:
        return "me"

    if not author:
        return ""

    # Tentar nome completo; se não existir, usar username
    full_name = getattr(author, "get_full_name", lambda: "")()
    if full_name:
        return full_name

    username = getattr(author, "username", "")
    return username or str(author)

@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def endrow():
    return "</div>"

@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)


@register.simple_tag
def endcol():
    return "</div>"

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    return {"title": "Recent Posts", "posts": posts}
