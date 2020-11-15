def favoriteGenre(userToBooks, genreToBook):
    d = dict()
    bookToGenre = dict()
    
    # invert genreToBook
    for genre in genreToBook:
        bookLst = genreToBook[genre]
        for book in bookLst:
            bookToGenre[book] = genre
    
    for user in userToBooks:
        biggestCount = 0
        mostLikedGenres = []
        
        counts = collections.defaultdict(int)
        
        bookLst = userToBooks[user]
        for book in bookLst:
            genre = bookToGenre[book]
            counts[genre] += 1
            if counts[genre] > biggestCount:
                biggestCount = counts[genre]
                mostLikedGenres = [genre]
            elif counts[genre] == biggestCount:
                mostLikedGenres.append(genre)
        
        d[user] = mostLikedGenres
    return d 
print(favoriteGenre(userMap,genreMap))
