class BoggleTrie():
   
   def __init__(self):
      self.root = TrieNode()
   
   def add_word(self, word: str):
      '''
      Adds a word to the Trie.
      '''
      current_node = self.root
      for char in word:
         if char not in current_node.children:
            current_node.children[char] = TrieNode()
         current_node = current_node.children[char]
      current_node.is_word = True

   def is_valid_word(self, word: str):
      '''
      Checks to see if the input word exists within the trie. Returns True if
      input word describes a path in the trie and the final TrieNode has a True
      is_word field. Otherwise returns False.
      '''
      pass

   def is_valid_prefix(self, prefix: str):
      '''
      Checks to see if the input prefix is a valid prefix to any words stored
      in the Trie. If the input is a valid prefix, returns True if the final
      node in the path has children nodes. Otherwise returns False.
      '''
      pass

   class TrieNode():
      def __init__(self, children = {}, is_word = False):
         self.children = children
         self.is_word = is_word