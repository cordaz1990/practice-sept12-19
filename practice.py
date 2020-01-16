def all_anagrams(filename):
    d = {}
    for line in open(filename):
       word = line.strip().lower()
       t = signature(word)
      if t not in d:
        d[t] = [word]
      else:
        d[t].append(word)
    
    return d
    
    
 def all_anagrams(filename):
     d = {}
    for line in open(filename):
      word = line.strip().lower()
      t = signature(word)
      d.setdefault(t,[]).append(word)
   
    return d
