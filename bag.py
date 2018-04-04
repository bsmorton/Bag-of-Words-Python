from collections import defaultdict
from goody import type_as_str

class Bag:
    def __init__(self,l=[]):
        self.d=defaultdict()
        for item in l:
            self.d.update({item:0})
        for item in l:
            self.d[item]+=1
    
    def __repr__(self):
        result=[]
        for a,b in self.d.items():
            for k in range(b):
                result.append(a)
        return 'Bag('+str(result)+')'    
    
    def __str__(self):
        return 'Bag('+''.join([str(item)+'['+str(self.d[item])+'],' for item in self.d.keys()])[:-1]+')'       

    def __len__(self):
        return sum([val for val in self.d.values()])

    def unique(self):
        return len(self.d.keys())

    def __contains__(self, s: str):
        return s in self.d.keys()

    def count(self,s:str):
        if self.__contains__(s):
            return self.d[s]
        else:
            return 0
        
    def add(self,s:str):
        if self.__contains__(s):
            self.d[s]+=1
        else:
            self.d.update({s:1})
            
    def __add__(self, right):
        try:
            b=Bag()
            for c,d in self.d.items():
                for val in range(d):
                    b.add(c)
        
            for c,d in right.d.items():
                for val in range(d):
                    b.add(c)
        
            return b
        except:
            raise TypeError
    
    def remove(self,s:str):
        if s in self.d.keys():
            self.d[s]+=-1
            if self.d[s]==0:
                self.d.pop(s)
        else:
            raise ValueError
        
    def __eq__(self,right):
        if type(self)!=type(right):
            return False
        return self.d==right.d
    
    def __ne__(self,right):
        if type(self)!=type(right):
            return True
        return self.d!=right.d
    
    def __iter__(self):
        def gen(d2):
            for item in d2:
                for val in range(d2[item]):
                    yield item
        return gen(self.d.copy())
          
    
        
        
        
        
        
if __name__ == '__main__':
    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
