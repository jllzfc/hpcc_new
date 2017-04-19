def get_queryfilters(param, trans=None):
    q = {}
    for k in param:
        if k.startswith("q__"):
            v = param[k]
            if v:
                q[k[3:]] = v if not trans or v not in trans else trans[v]
    return q

def get_pageinfo(param,size=10,page=1):
    size = 'size' in param and int(param['size']) or size
    if size < 0:
        size = 100000

    page = 'page' in param and int(param['page']) or page
    start = size * (page - 1)

    return (size, page, start)


def warp_query(query, trans=None, param=None):
    if param:
        qs = get_queryfilters(param, trans)
        from django.db.models import Q
        nqs = {}
        Q()
        for k, v in qs.items():
            if '__or__' in k:
                ks = k.split('__or__')
                q = Q(**{ks[0]: v})
                for nk in ks[1:]:
                    q = q | Q(**{nk: v})
                query = query.filter(q)
            else:
                nqs[k] = v
        if nqs:
            query = query.filter(**nqs)
            #     print size, page, start

    if param and 'sort' in param:
        query = query.order_by(u'%s%s' % ('-' if 'order' in param and param['order'] == 'desc' else '', param['sort']))
    if param and 'orderby' in param:
        query = query.order_by(*[v.strip() for v in param['orderby'].split(',') if v.strip()])

    return query

def gen_pager(query,trans=None,size=10,page=1,param=None):
    start = 0
    if param:
        size, page, start = get_pageinfo(param, size,page)
    else:
        size, page = int(size), int(page)
        start = size * (page - 1)

    query = warp_query(query, trans, param)

    count = query.count()
    rawquery = query
    items = query[start:size * page]
    firstpage = 1
    lastpage = (count - 1) / size + 1

    res = {
        'itemsquery': items,
        'rawquery': rawquery,
        'items': items,
        'count': count,
        'page': page,
        'size': size,
        'start': start,
        'prevpage': page - 1 if page > 1 else 1,
        'nextpage': page + 1 if page < lastpage else lastpage,
        'prev': page - 1 if page > 1 else False,
        'next': page + 1 if page < lastpage else False,
        'first': firstpage if page > firstpage else False,
        'last': lastpage if page < lastpage else False,
        'lastpage': lastpage,
        'firstpage': firstpage,
        }
    res['needpager'] = res['next'] or res['prev']
    return res