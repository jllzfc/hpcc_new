from django import template
register = template.Library()

@register.filter
def groupbydate(ls,field,fmt='%Y%m'):
    arr = []
    arrd = {}
    for r in ls:
        if hasattr(r,field):
            dt = getattr(r, field)
            if not dt:
                raise Exception('%s.%s=%s' % (r, field, dt))
            key = dt.strftime(fmt)
            if key not in arrd:
                arrd[key] = {
                    'list':[],
                    'key':key
                }
                arr.append(arrd[key])
            d = arrd[key]
            d['date'] = dt
            d['list'].append(r)
        else:
            raise Exception('%s has no field %s' % (r, field))
    return arr

@register.filter
def pageurl(request, page):
    import re
    curpath = request.get_full_path()
    dr = re.compile(r'page=[0-9]*', re.S)
    dd = dr.sub('', curpath)
    if '?' not in dd:
        dd = dd + '?'
    if not dd.endswith('&') and not dd.endswith('?'):
        dd = dd + '&'
    dd = dd + 'page=%s' % page
    return dd
