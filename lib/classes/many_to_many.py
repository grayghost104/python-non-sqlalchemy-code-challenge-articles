class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)


    def get_title(self):
        return self._title
    def set_title(self,value):
        # print("attripute exists? ",hasattr(self, "title"))
        if type(value) is str and 5<= len(value) <=50 and not hasattr(self, "title"):
            self._title = value
        else:
            print("Not valid title/ cannot change")
    title = property(get_title,set_title)

    # def get_title(self):
    #     return self._title
    # def set_title(self, value):
    #     if type(value) is str and 5>= len(value) <=50 and not hasattr(self, "title"):
    #         self._title = value 
    # title= property(get_title, set_title)

    # def get_title(self):
    #     return self._title
    # def set_title(self, value):
    #     if type(value) is str and 5>= len(value) <= 50 and not hasattr(self, " "):
    #     # if type(value) is str and 5 >= len(value) <= 50 and not hasattr(self, "title"):
    #         self._title = value
    #     # else:
    #     #     print("Not valid") 
    # title = property(get_title,set_title)

    def get_author(self):
        return self._author
    def set_author(self, value):
        if type(value) is Author and not hasattr(self, "Author"):
            self._author = value
    author = property(get_author, set_author)

    def get_magazine(self):
        return self._magazine
    def set_magazine(self, value):
        if type(value) is Magazine and not hasattr(self, "Magazine"):
            self._magazine = value 
    magazine = property(get_magazine, set_magazine)
        
class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def get_name(self):
        return self._name
    def set_name(self,value):
        # print("attripute exists? ",hasattr(self, "name"))
        if type(value) is str and 0 < len(value) and not hasattr(self, "name"):
            self._name = value
        else:
            print("Not valid name/ cannot change")
    name = property(get_name,set_name)

    # def get_name(self):
    #     return self._name
    # def set_name(self, value):
    #     if type(value) is str and 0 > len(value) and not hasattr(self, "name"):
    #         self._name = value 
    #     # else:
    #         # print("Not valid")
    # name = property(get_name, set_name)

    def articles(self):
        my_articles = []
        for article in Article.all:
            if article.author == self:
                my_articles.append(article)
        return my_articles


    def magazines(self):
        my_magazine = []
        for article in Article:
            if article.author == self and article.magazine not in my_magazine:
                my_magazine.append(article.magazine)
        return my_magazine

    # def magazines(self):
    #     my_magazine = []
    #     for magazine in Magazine.all:
    #         if magazine.author == self and magazine.article not in my_magazine:
    #             my_magazine.append(magazine.article)
    #     return my_magazine

    def add_article(self, magazine, title):
        return Article(
            # author=self, 
            magazine=magazine, 
            title=title
        )

    def topic_areas(self):
        unique = []
        for article.author.category in Article.all:
            if article.author.category == self:
                unique.append(article.author.category)
            else:
                None
        return str(unique)

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def get_name(self):
        return self._name
    def set_name(self, value):
        if type(value) is str and 2 <= len(value) <= 16:
            self._name = value
        else:
            print("Not valid") 
    name = property(get_name, set_name)

    def get_category(self):
        return self._category
    def set_category(self, value):
        if type(value) is str and 0 > len(value):
            self._category = value
        else:
            print("Not valid") 
    category = property(get_category, set_category)

    def articles(self):
        published_article = []
        for article in Article.all:
            if article.author == self:
                published_article.append(article)
        return published_article

    def contributors(self):
        my_auth = []        
        for author.magazine in Author.all:
            if author.magazine == self and author.article not in my_auth:
                my_auth.append(author.article)
                
    def article_titles(self):
        all_both=[]
        for article in Article.all:
            if article.title == self:
                all_both.append(article.title)
        return all_both
                

    def contributing_authors(self, value):
        more_2 = []
        count = 0
        for author.magazine in Magazine.author:
            if author.magazine == self and type(value) is str:
                count += 1
            if author.magazine == self:
                count += 1
            if count == 2:
                return more_2
            else: 
                None
            more_2.append(author.magazine)
    def count_articles(self,article):
        count = 0
        for article in Article.all:
            if article.magazine == self:
                count+=1
        return count

    # @classmethod
    # def top_publisher(cls)
    #     currMax = 0
    #     currMaxM = None 
    #     for magazine in Magazine.all:
    #         article_count = magazine.count_articles()
    #         if article_count > currMax:
    #             currMax = article_count
    #             currMaxM = magazine
    #     return currMaxM
    #         else:
    #             None 