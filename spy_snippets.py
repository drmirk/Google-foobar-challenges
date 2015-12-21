def answer(document, searchTerms):
  document = " " + document + " "
  locations = {}
  len_doc = len(document)
  potential_ranges = []
  potential_strings = {}
  s = " "
  if len(searchTerms) == 1:
    return searchTerms[0]
  for term in searchTerms:
    term_cop = " " + term + " "
    doc_copy = document
    doc_loc = 0
    len_term = len(term_cop)
    locations[term] = [[],[]]
    while term in doc_copy:
      loc = doc_copy.find(term_cop) + doc_loc
      locations[term][0].append(loc)
      locations[term][1].append(loc + len_term)
      doc_copy = document[loc+len_term: len_doc]
      doc_loc = loc + len_term
  for start_term, start_locs in locations.iteritems():
    for start_position in start_locs[0]:
      for start_term, end_locs in locations.iteritems():
        for end_position in end_locs[1]:
          if start_position + len(start_term) < end_position:
            potential_ranges.append([start_position, end_position])
  if len(potential_ranges) ==1:
    return document[potential_ranges[0][0]:potential_ranges[0][1]]
  for potentials in potential_ranges:
    contains_all = True
    doc_list = document[potentials[0]:potentials[1]].strip().split(" ")
    for term in searchTerms:
      if term not in doc_list:
        contains_all = False
    if contains_all:
      try:
        if len(potential_strings[potentials[0]])> len(doc_list):
          potential_strings[potentials[0]] = doc_list
      except KeyError:
        potential_strings[potentials[0]] = doc_list
  if len(potential_strings) == 1:
    return s.join(potential_strings.values()[0])
  min_len = len(min(potential_strings.values(), key=len))
  potential_strings = {loc:words for (loc, words) in potential_strings.iteritems() if len(words) == min_len}

  return s.join(potential_strings[min(potential_strings.keys())])

# print answer("the things", ["the"]) == "the"

print answer("what word to do do what word to", ["what", "to", "do"]) == "what word to do"
print len("what word to do do what word to")

print answer("all the things in the world", ["all", "the", "world"]) == "all the things in the world"
print len("all the things in the world")

print answer("a b c d a", ["a", "c", "d"]) == "c d a"

print answer("many google employees can program", ["google", "program"]) == "google employees can program"
print len("many google employees can program")

print answer("world there hello hello where world", ["hello", "world"]) == "world there hello"
print len("world there hello hello where world")

print answer("I hope it all works. hop off it", ["hop", "it"]) == "hop off it"
print len("I hope it all works. hop off it")

print answer("this is a a best thing word wrod word word word word this encyclopedia blog thing", ["this", "thing"]) == "this encyclopedia blog thing"
print len("this is a a best thing word wrod word word word word this encyclopedia blog thing")

print answer("igloos are in the loos", ["loos", "are"])== "are in the loos"
print len("igloos are in the loos")

print answer("i hope you are hopping over to your hop scotch event.", ["hop","you"]) == "you are hopping over to your hop"

# print answer("p k g u p o y z e q s n x v f f w o d j w f e q c n r l n a z x t l q t h m x k b p j m y v e b b u",
#     ["j", "z", "v"])
# print "z e q s n x v f f w o d j"

print answer("c r i l n h y h z w e o b h q b q f x a c o y c l v l n k j r o m p d z q n c v q k a o j s d x n d b k c y v b v n m f y m b m j l h i c q z c q i k", ["b", "s", "q"])


'''
c r i l n h y h z w e o b h q b q f x a c o y c l v l n k j r o m p d z q n c v q k a o j s d x n d b k c y v b v n m f y m b m j l h i c q z c q i k
['b', 's', 'q']
q k a o j s d x n d b
q n c v q k a o j s d x n d b
'''

print answer("this is a a a best thing word wrod word word word word this encyclopedia blog thing", ["word", "encyclopedia"]) == "word this encyclopedia"
