#!/usr/bin/python3
import sys
from pqueue import *
    
def genneighbors(length,current,mywordlist):
  #gives us all the neighbors
  neighbors = {}
  neighbors[current] = []
  index = 0
  while index < length:
    j = 97
    #change one letter of m everytime
    #print("index: " + str(index) )
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
    if len(words) > 1:     
      wordpairs.append(words[0])
      wordpairs.append(words[1])
    
  #length of list
  length = len(wordpairs[0])
  print("length of words: " + str(length))
  
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
    print("finding path from " + first + " to " + second)
    
    #my_cmp compares list lengths + sum of first element, which is g(n). h(n) can be incorporated by appending 0 or smtg
    frontier = PQueue(my_cmp)
    
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
    explored = {-1}
    specialctr = 0
    
    #we need to find the first instance when h(n) + g(n) is 0 and this suffices bc we keep on working with the minimum g(n) + h(n)
    #note that after finding all neighbors, the dictionary dissapears so you'll have to push all the info to Pqueue
    #Read his art
    while specialctr == 0 and frontier.peek()[0] != second:
      current = frontier.peek()[0]
      path = frontier.peek()[2:]
      allneighbors = genneighbors(length,current,mywordlist)[current]
      #print("all neighbors of " + current + ":")
      #print(allneighbors)
      explored.add(current)
      frontier.pop()
      newlen = len(allneighbors)
            
      for neighbor in allneighbors:
        #in the form of a dictionary
        if neighbor not in explored:
          k = []
          for r in path:
            k.append(r)
          k.append(current)
          k.insert(0,neighbor)

          #compute h_n
          index1 = 0
          h_n = 0
          test = list(current)
          while index1 < length:
            if test[index1] != second1[index1]:
              h_n+=1
            index1+=1

          k.insert(1,h_n)
          frontier.push(k)
        #else:
          #print(neighbor + " has been explored")
          newlen-=1
          #if newlen == 0:
            #print("bad path from " + first + " to " + second)
            #frontier.pop()
            #g = open(outfile,'w')           
            #g.write(first + "," + second + "\n" )
            #g.close()
            #specialctr = 1
              
      
    #towrite[first] = string of things you want
    i+=2
    print("shortest distance from " + first + " to " + second)
    bestpath = frontier.peek()[2:]
    bestpath.append(frontier.peek()[0])
    print(bestpath)
    towrite.append(','.join(bestpath))

    #when fully computed, add length and path to dictionary

  towrite = '\n'.join(towrite)
  #g is what we will return
  g = open(outfile,'w')
  g.write(towrite)
  g.close()

            
#$ ./fred.py A.txt(words of same length) B.txt
def main():
  Process(sys.argv[1],sys.argv[2])

main()
