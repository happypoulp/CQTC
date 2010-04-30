from django import template
import math

register = template.Library()

@register.inclusion_tag('extension/paginator.html', takes_context=True)
def paginator(context, object_list_name='object_list', adjacent_pages=2):
    page_obj = context['page_obj']
    paginator = context['paginator']
    page_numbers = [n for n in \
                    range(page_obj.number - adjacent_pages, page_obj.number + adjacent_pages + 1) \
                    if n > 1 and n <= context['pages']-1] # we exlude first and last page since they always exist

    # Nb of items in the current list page
    results_this_page = context[object_list_name].count()

    paginate_bys = [10, 25, 50, 100, 200]
    try:
        paginate_bys.index(context['results_per_page'])
    except ValueError:
        paginate_bys.append(context['results_per_page'])
    paginate_bys.sort()

    # This enable to stay more or less at the same position in list when changing nb of items per page
    for index, paginate_by in enumerate(paginate_bys):
        paginate_bys[index] = {'paginate_by': paginate_by, 'optimal_page': int(math.ceil((((page_obj.number - 1)*context['results_per_page'])+1)/float(paginate_by)))}

    has_hidden_previous = not (page_obj.number == 1) and (page_obj.number - adjacent_pages - 1 > 1)
    has_hidden_next = not (page_obj.number == paginator.num_pages) and (page_obj.number + adjacent_pages + 1 < paginator.num_pages)

    return {
        'hits': context['hits'],
        'results_per_page': context['results_per_page'],
        'results_this_page': results_this_page,
        'page_obj': page_obj,
        'paginator': paginator,
        'pages': context['pages'],
        'page_numbers': page_numbers,
        'show_first': 1 not in page_numbers,
        'show_last': context['pages'] not in page_numbers,
        'is_first' : page_obj.number == 1,
        'is_last' : page_obj.number == paginator.num_pages,
        'has_hidden_previous' : has_hidden_previous,
        'has_hidden_next' : has_hidden_next,
        'paginate_bys': paginate_bys
        }

