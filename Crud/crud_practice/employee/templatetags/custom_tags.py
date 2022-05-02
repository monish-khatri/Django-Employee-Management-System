from django import template
from urllib.parse import urlencode
from collections import OrderedDict

register = template.Library()


@register.simple_tag
def url_replace(request, field, value, direction='',for_class = False):
    dict_ = request.GET.copy()
    class_name = ''
    if field == 'order_by' and field in dict_.keys():
      if dict_[field].startswith('-') and dict_[field].lstrip('-') == value:
        dict_[field] = value
        class_name = 'headerSortDown'
      elif dict_[field].lstrip('-') == value:
        dict_[field] = "-" + value
        class_name = 'headerSortUp'
      else:
        dict_[field] = direction + value
    else:
      dict_[field] = direction + value

    if for_class:
       return class_name
      
    else:
      return urlencode(OrderedDict(sorted(dict_.items())))
