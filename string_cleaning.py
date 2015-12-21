import re as re

def findSubString(chunk,sub):
    starting_index = []
    for i in xrange(len(chunk)):
        if(chunk[i] == sub[0]):
            if (chunk[i:i+len(sub)] == sub):
                starting_index.append(i)
    return starting_index

def answer(chunk,word):
    length = len(word)
    results = []
    potentials = findSubString(chunk,word)
    if potentials == []:
        return chunk
    for i in potentials:
        str_copy = chunk[0:i] + chunk[i+length:len(chunk)]
        if word not in str_copy:
            if str_copy not in results:
                results.append(str_copy)
        else:
            new_potentials = findSubString(str_copy, word)
            for j in new_potentials:
                str_copy1 = str_copy[0:j] + str_copy[j+length:len(str_copy)]
                if word not in str_copy1:
                    if str_copy1 not in results:
                        results.append(str_copy1)
                else:
                    new_potentials_2 = findSubString(str_copy1, word)
                    for k in new_potentials_2:
                        str_copy2 = str_copy1[0:k] + str_copy1[k+length:len(str_copy1)]
                        if word not in str_copy2:
                            if str_copy2 not in results:
                                results.append(str_copy2)
                        else:
                            while word in str_copy2:
                                str_copy2 = re.sub(word, "", str_copy2)
                            if str_copy2 not in results:
                                results.append(str_copy2)


    min_len = len(min(results, key=len))
    results = filter(lambda x: len(x)== min_len, results)
    results.sort()
    return results[0]

for _ in xrange(10000):
    answer("lololololo", "lol")

if not answer("lololololo", "lol") == "looo":
    print answer("lololololo", "lol")
else:
    print "True"
if not answer("goodgooogoogfogogooood", "goo") == "dogfood":
    print answer("goodgooogoogfogogooood", "goo")
else:
    print "True"
if not answer("aabb", "ab") == "":
    print answer("aabb", "ab")
else:
    print "True"
if not answer("lolollolol", "lol") == "o":
    print answer("lolollolol", "lol")
else:
    print "True"
if not answer("owowowwwowowowwoowow", "wow") == "oowoo":
    print answer("owowowwwowowowwoowow", "wow")
else:
    print "True"
if not answer("abcd", "abcd") == "":
    print answer("abcd", "abcd")
else:
    print "True"
if not answer("timing is...", "everything") == "timing is...":
    print answer("timing is...", "everything")
else:
    print "True"
# .268s
# .223
