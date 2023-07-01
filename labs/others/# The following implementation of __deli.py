# The following implementation of __delitem__ (given that idx is a positive, valid index) in an array-backed list doesn’t appear to work correctly. How would you go about fixing it?

for i in range(len(self.data)-1, idx, -1):
    self.data[i-1] = self.data[i]
del self.data[len(self.data)-1]


for i in range(idx, len(self.data) - 1):
    self.data[i] = self.data[i + 1] 
del self.data[len(self.data) - 1]