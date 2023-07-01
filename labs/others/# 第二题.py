# 第二题 
# Array0backed List --> Problem :move element 




# start code

class ArrayList:
    def __init__(self):
        self.data = []
        self.count = 0
    def __getitem__(self, idx):
        return self.data[idx]

    def __setitem__(self ,idx,val):
        self.data[idx] = val
    
    def __len__(self):
        return self.count

    def append(self, val):
        self.count + =1
        self.data.append(None)
        self.data[len(self) -1] =val
    def move(self, src, dst):
        # your code
