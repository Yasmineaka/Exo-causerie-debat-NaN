from typing import Any

class Array:

    tab = []
    
    def __init__(self,*args):
        self.tab = list(args)
                   
    def at(self,indice:int)->Any or None:
        try:
            return self.tab[indice]
        except IndexError:
            return None
        
    def concat(self,tabT:list[Any])->Any or None:
        if type(tabT) == list:
            tabl=self.copie()
            for i in tabT: tabl.append(i)
            return  self.tab
        raise TypeError ("L'élément doit être un tableau") 
    
    def fill(self,rpl:Any,a:int,b:int=-1)->Any or None: 
        if a<self.length() and b<self.length():
            if b<0:
                b=self.length()+b
            tableau=self.copie()
            for _ in range(a,b+1):
                tableau[_]= rpl
            return tableau
        raise TypeError ("les indices sont supperieurs a la taille du tableau")

        # for i in self.tab:
        #     self.tab(i)
        #     print(self.tab(i))
        # self.tab.append(rpl)
        # return self.tab
    

    def copie(self)-> list[Any]:
        return [item for item in self.tab]


    
    def length(self):
        cpt = 0
        for i in self.tab:
          cpt += 1
        return cpt
    
    def push(self, *args):
        self.tab = self.tab + list(args)
        return self.tab

    def filtre(self,func)-> list[Any]:
        """Filtre le tableau en  fonction du bouleen"""
        result = []
        for i in self.tab:
            if func(i):
                result.append(i)
        return result
    
    def my_map(self,func):
        """return un nouveau tableau"""
        result = []
        for i in self.tab:
            result.append(func(i))
        return result

    def incluse(self, element:Any):
        return element in self.tab
    
      
if __name__ == "__main__":
    test = Array(23,56,"2","cd")
    test2 = Array(2,4,5)
    #print(test2.my_map(lambda a: a*2))
    print(test.at(12))
    print(test.concat([1,2,3]))
    print(test.fill("salut",2))
    print(test.length())
    print(test.push(2,3,4))
    print(test.filtre(lambda x:  type(x) is int))
    print(test.my_map(lambda x : f'{x}salut'))
    print(test.incluse(3))