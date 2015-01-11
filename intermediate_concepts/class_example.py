#!/usr/bin/python
#sfischer

class Publications(object):
    def __init__(self, title, numberOfPages, publicationDate, timesRead):
        self.title = title
        self.numberOfPages = numberOfPages
        self.publicationDate = publicationDate 
        self.timesRead = timesRead
    
    def addRead(self, i=1):
        if (i<1):
            return
        self.getNumPages += i

    def getTitle(self):
        return self.title
    
    def getNumPages(self):
        return self.numberOfPages
    
    def getPubDate(self):
        return self.publicationDate
    
    def getTimesRead(self):
        return self.timesRead

class Books(Publications):
    bookcount=0
    def __init__(self, title, numberOfPages, publicationDate, timesRead, author, ISBN):
        super(Books,self).__init__(title, numberOfPages, publicationDate, timesRead)
        self.author = author
        self.ISBN = ISBN
        Books.bookcount+=1

    def __str__(self):
        return "Title:" + self.title + "\nauthor" + self.author + "\nPages" + str(self.numberOfPages)

    def __del__(self):
        Books.bookcount -=1

    def getAuthor(self):
        return self.author
    
    def getISBN(self):
        return self.ISBN

    @classmethod    
    def getBookCount():
        return Books.bookCount

class Periodicals(Publications):
    percount=0
    def __init__(self, title, numberOfPages, publicationDate, timesRead, Volumes, issueNumbers):
        super(Periodical,self).__init__(title, numberOfPages, publicationDate, timesRead)
        self.Volumes = Volumes
        self.issueNumbers = issueNumbers
        periodicals.percount+=1


    def __str__(self):
        return "Title:" + self.title + "\nVolume" + self.Volumes + "\nPages" + str(self.numberOfPages)

    def __del__(self):
        Periodicals.percount -=1

    def getVolumes(self):
        return self.Volumes
    
    def getIssueNumbers(self):
        return self.issueNumbers
    
    @classmethod
    def getPeriodicalCount():
        Periodicals.percount += 1
        return Periodicals.percount

book1 = Books("Lord of the Rings", 1002, "03/2/96", 1000, "Sean Fischer", 9123)

print book1

print "Book Count" + str(book1.getBookCount())

print "book1 title" + book1.getTitle

print "book1 author" + book1.getAuthor

print "Original Times Read" + str(book1.getTimesRead())

book1.addread()
print "Increment of 1" +str(book1.getTimesRead)

book1.addread(2)
print "Increment of 2" +str(book1.getTimesRead)

book1.addread(-1)
print "decrement of 1" +str(book1.getTimesRead)

book2 = Books("Hobbit", 10, "03/2/96", 1000, "Corey smith", 9023)

print book2

print "Book count after books" + str(book2.getBookCount)

#_______________________OTHER METHODS_________________
print ""

print "book2 ISBN" + str(book2.getISBN())

print "book2 page" + str(book2.getTimesRead())

print "book2 pub date" + str(book2.getPubDate)
#________________--PERIDICAL TEST________________________-
#break
print ""

per1 = Periodicals("People", 12, "08/05/13", 1, 55, "publicationDate")

print per1

print "per1 Volumes" + str(per1,getVolumes())

print "per1 Issue number" + str(per1.getIssueNumbers)

print "per count" + str(per1.getPeriodicalCount)
