def group_books_by_author(books):
    author_to_titles = {}
    
    for book in books:
        author = book["author"]
        title = book["title"]
        
        if author not in author_to_titles:
            author_to_titles[author] = []
            
        author_to_titles[author].append(title)
            
    return author_to_titles