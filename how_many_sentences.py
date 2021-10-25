# How many sentences?Hackerrank Intern test
def countSentences(wordSet, sentences):
    # Write your code here
    result = []
    for i in range(len(sentences)):
      words = sentences[i].split(" ")
      totalCount = 0
      for word in words:
        cnt = countAnagrams(word,wordSet)
        if (cnt == 0):
          continue
        totalCount = cnt if totalCount==0 else totalCount*cnt
      result.append(totalCount)
    return('\n'.join(map(str,result)))

def countAnagrams(word,wordset):
  anagramCnt = 0
  for i in range(len(wordSet)):
    if(isAnagram(word,wordSet[i])):
      anagramCnt += 1
  return anagramCnt

def isAnagram(word,word2):
  if(len(word)!=len(word2)):
    return False
  elif(sorted(word) == sorted(word2)):
    return True
  else:
    return False
