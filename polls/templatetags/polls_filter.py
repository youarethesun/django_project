from django import template
register = template.Library()

@register.inclusion_tag("polls/show_forms.html")
def show_forms(form):
    context = dict()
    context['form'] = form
    return context

