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
            key = dt.strFtime(fmt)
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
