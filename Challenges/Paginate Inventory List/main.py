def paginate_items(items, page_size):
    list_of_pages = []
    start = 0
    
    while start < len(items):
        page = items[start : start + page_size]
        list_of_pages.append(page)
        start += page_size

    return list_of_pages
