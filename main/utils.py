def get_pageinfo(param,size=10,page=1):
    size = 'size' in param and int(param['size']) or size
    if size < 0:
        size = 100000

    page = 'page' in param and int(param['page']) or page
    start = size * (page - 1)

    return (size, page, start)