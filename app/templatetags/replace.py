from django import template
register = template.Library()

@register.filter(name='replacer')
def replace(string, args):
    import re
    search = args.split(args[0])[1]
    replace = args.split(args[0])[2]

    return re.sub(search, replace, string)
