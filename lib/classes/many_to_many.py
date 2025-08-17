class Article:
    all = []  
    
    def __init__(self, author, magazine, title):
       
        self._author = author
        self._magazine = magazine  
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        
        if hasattr(self, '_title'):
            pass

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
       
        self._magazine = value


class Author:
    def __init__(self, name):
        
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
       
        if hasattr(self, '_name'):
            pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
       
        magazine_set = set()
        for article in self.articles():
            magazine_set.add(article.magazine)
        return list(magazine_set)

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        articles = self.articles()
        if not articles:
            return None
        
        categories = set()
        for article in articles:
            categories.add(article.magazine.category)
        return list(categories)


class Magazine:
    all = []  
    
    def __init__(self, name, category):
       
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
       

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = set()
        for article in self.articles():
            authors.add(article.author)
        return list(authors)

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        articles = self.articles()
        if not articles:
            return None
        
        
        author_counts = {}
        for article in articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        
        max_articles = 0
        top_magazine = None
        
        for magazine in cls.all:
            article_count = len(magazine.articles())
            if article_count > max_articles:
                max_articles = article_count
                top_magazine = magazine
        
        return top_magazine if max_articles > 0 else None