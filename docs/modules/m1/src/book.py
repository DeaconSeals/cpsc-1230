class Book:
   def __init__(self, author, title, pages):
      self.author = author
      self.title = title
      self.pages = pages

   def __eq__(self, other):
      if id(self) == id(other): return True

      if not isinstance(other, Book): return False

      return self.title == other.title and self.author == other.author

   def __lt__(self, other):
      if not isinstance(other, Book):
         raise TypeError(f"Book not comparable with {other.__class__}")

      if self.author < other.author: return True

      if self.title < other.title: return True

      return False