#!/usr/bin/python3
import sys

class PQueue:
    
  def OrdinaryComparison(a,b):
    if a < b: return -1
    if a == b: return 0
    return 1

  #what does self refer to
  def __init__(self, comparator = OrdinaryComparison):
    self.cmpfunc = comparator
    self.size = 0
    self.list = [0]
  
  #push an element onto the queue.
  #data in the form of a list
  def push(self, data):   
    #for x in data:
    if self.size == len(self.list) - 1:
      self.list.append(data)
    else:
      self.list[self.size] = data
    self.size += 1
    pos = self.size
      #print("size")
      #print(self.size)
      #print("0th:")
      #print(self.list[0])
     
    while pos > 1 and self.cmpfunc(self.list[pos//2], self.list[pos]) == 1:
      val = self.list[pos]
      self.list[pos] = self.list[pos//2]
      self.list[pos//2] = val
      pos=pos//2
    
    #for i in range(1,self.size+1):
     # print(self.list[i])
  
  def push_all(self,lst):
    for x in lst:
      if self.size == len(self.list) - 1:
        self.list.append(x)
      else:
        self.list[self.size] = x
      self.size += 1
      pos = self.size
      #print("size")
      #print(self.size)
      #print("0th:")
      #print(self.list[0])
     
      while pos > 1 and self.cmpfunc(self.list[pos//2], self.list[pos]) == 1:
        val = self.list[pos]
        self.list[pos] = self.list[pos//2]
        self.list[pos//2] = val
        pos=pos//2

  
  def internal_list(self):
    i = 1
    lst = []
    while i <= self.size:
      lst.append(self.list[i])
      i+=1
    return lst
                         
  #pop the smallest element off the queue or None if the queue is empty.
  def pop(self):
    if self.size == 0:
      return None

    if self.size == 1:
      self.size -= 1
      return self.list[1]

    pos = 1
    ret = self.list[1]
    
    self.list[1] = self.list[self.size]
    self.size -= 1
      
    while 2*pos+1 <= self.size:
      if self.cmpfunc(self.list[pos], self.list[2*pos+1]) == 1 or self.cmpfunc(self.list[pos], self.list[2*pos]) == 1:
        if self.cmpfunc(self.list[2*pos+1], self.list[2*pos]) == -1:
          val = self.list[pos]
          self.list[pos] = self.list[2*pos+1]
          self.list[2*pos+1] = val
          pos *= 2
          pos += 1
        else:
          val = self.list[pos]
          self.list[pos] = self.list[2*pos]
          self.list[2*pos] = val
          pos *= 2
      else:
        return ret

    if 2*pos == self.size and self.cmpfunc(self.list[pos], self.list[2*pos]) == 1:
        val = self.list[pos]
        self.list[pos] = self.list[2*pos]
        self.list[2*pos] = val
        
    return ret
    
  
  #return the smallest element in queue without disturbing the queue.  It should return None if the queue is empty.
  def peek(self):
    if self.size == 0:
      return None
    return self.list[1]
  
  #pop() every element off the queue into a list (in order) that it returns.
  #If the queue was empty, it returns an empty list.  Once this function returns, the queue is empty.
  def tolist(self):
    sorted = []
    iterations = self.size
    while (iterations >= 1):
      sorted.append(self.pop())
      iterations -= 1
    return sorted
  
  def my_cmp(a,b):
    if len(a) + a[1] < len(b) + b[1]: return -1
    if len(a) + a[1] == len(b) + b[1]: return 0
    return 1
    
def genneighbors(current,mywordlist):
  #gives us all the neighbors
  neighbors = {}
  neighbors[current] = []
  index = 0
  while index < length:
    j = 97
    #change one letter of m everytime
    print("index: " + str(index) )
    while j < 123:
      m = list(current)
      m[index] = chr(j)
      m = "".join(m)
      #print(m in mywordlist)
      if m in mywordlist:
        if m == current:
          pass
        else:
          #contains all the neighbors and allows us to process it
          val = neighbors[current]
          val.append(m)
          neighbors[current] = val
      j+=1
    index+=1
  return neighbors

def Process(infile,outfile):
  #f has pair of words to apply wordladder to
  f = open(infile, 'r')
  check = f.read().split('\n')
  f.close()

  p = 0
  wordpairs = []
  for k in check:
    words = k.split(',')
    wordpairs.append(words[0])
    wordpairs.append(words[1])

    
  #length of list
  length = len(wordpairs[0])
  print(length)
  
  #word list
  dictall = open('dictall.txt','r')
  wordlist = dictall.read().split('\n')
  dictall.close()
  
  mywordlist = []
  
  #get all words of same length
  for k in wordlist:
    if len(k) == length:
      mywordlist.append(k)
  #print(k)
  
  towrite = []
      
  
  i = 0
  while i < len(wordpairs):
    #dictionary gives us all neighbors, which will be appended to Pqueue
    first = wordpairs[i]
    second = wordpairs[i+1]
    print("finding path from word " + first + " to word " + second)
    
    #my_cmp compares list lengths + sum of first element, which is g(n). h(n) can be incorporated by appending 0 or smtg
    frontier = Pqueue(my_cmp)
    
    #Finding h(n)
    first1 = list(first)
    second1 = list(second)
    h_n = 0
    g_n = 0
    index = 0
    
    while index < length:
      if first1[index] != second1[index]:
        h_n+=1
      index+=1
      
    frontier.push([first,h_n])
    explored = {}
    
    #we need to find the first instance when h(n) + g(n) is 0 and this suffices bc we keep on working with the minimum g(n) + h(n)
    #note that after finding all neighbors, the dictionary dissapears so you'll have to push all the info to Pqueue
    #Read his art
    while frontier.peek()[1] != second:
      for current in frontier.peek():
        #in the form of a dictionary
        allneighbors = genneighbors(current,mywordlist)
        explored.add(current)
        for neighbors in allneighbors:
          if neighbors in explored:
            break
          k = allneighbors[neighbors]
          k.insert(0,neighbors)
          
          #compute h_n
          index1 = 0
          h_n = 0
          while index1 < length:
            if first[index1] != second[index1]:
              h_n+=1
            index1+=1
            
          k.insert(1,h_n)
          frontier.push(k)                  
      
    #towrite[first] = string of things you want
    i+=2
    print(frontier.peek())
    towrite.append(frontier.peek())

    #when fully computed, add length and path to dictionary

  
  #g is what we will return
  g = open(outfile,'w')
  for k in towrite:    
    g.write(k + "," + str( len(dictionary[k])) + "\n" )
  g.close()

            
#$ ./fred.py A.txt(words of same length) B.txt
def main():
  Process(sys.argv[1],sys.argv[2])

main()
