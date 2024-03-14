class Article:
    all =  []
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        self.title = title
        self.author = author
        self.magazine = magazine
        author.add_article(magazine, self)
        Article.all.append(self)

    @property
    def immutable_str(self):
        return self._title  
    



    def author(self):
        return self.author

    
    def magazine(self):
        return self.magazine

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must not be empty")
        self.name = name
        self._articles = []
        self.magazines = []

    # @property
    # def name(self):
    #     return self._name
    
 
    def articles(self):
        return self._articles
    

  

    # def __str__(self):
    #     return f"Author: {self.name}"
    
    def magazines(self):
        return self.magazines
       

    def add_magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        if magazine not in self.magazines:
         self.magazines.append(magazine)

    def add_article(self, magazine, article):
        self._articles.append(article)
        self.add_magazine(magazine) 
        return article
         
    # def add_article(self, magazine, title):
    #     if not isinstance(magazine, Magazine):
    #         raise TypeError("Magazine must be an instance of Magazine")
    #     if not isinstance(title, str):
    #         raise TypeError("Title must be a string")
    #     if len(title) < 5 or len(title) > 50:
    #         raise ValueError("Title must be between 5 and 50 characters")
        
    #     article = Article(self, magazine, title)  # Instantiate Article
    #     self._articles.append(article)
    #     return article     

    def topic_areas(self):
        topic_areas_set = set()
        for article in self._articles:
            topic_areas_set.add(article.magazine.category)
        return list(topic_areas_set)




class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not 2 <= len(name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters long")
        self.name = name

        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must not be empty")
        self.category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    def articles(self):
        return self._articles

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("Article must be an instance of Article")
        self._articles.append(article)

    def contributors(self):
        return list(set(article.author for article in self._articles))


    def article_titles(self):
        if self._articles:
            return [article.title for article in self._articles]
        return None

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            if article.author in authors_count:
                authors_count[article.author] += 1
            else:
                authors_count[article.author] = 1

        contributing_authors = [author for author, count in authors_count.items() if count > 2]
        if not contributing_authors:
            return []
        return contributing_authors

  




# Create instances of Author and Magazine
author = Author("Khalid")
magazine = Magazine("Tech Magazine", "Technology")

# Test initializing Article instance
article = Article(author, magazine, "Python Programming")

# For test purpose of the Article instances
# print("Article Title:", article.title)  
print("Article Author:", author.name) 
# print("Article Magazine:", article.magazine.name) 


