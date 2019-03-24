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
      self.list[self.size+1] = data
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
      pos = pos//2
    
    #for i in range(1,self.size+1):
      #print(self.list[i])
  
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
      
    while 2*pos-1 < self.size:
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
    if (len(a) + a[1]) < (len(b) + b[1]): return -1
    if (len(a) + a[1]) == (len(b) + b[1]): return 0
    return 1
