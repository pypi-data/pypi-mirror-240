class RunNs:
    def __init__(self) -> None:
        self.counter = 0

    def Run(self,fun,n,args=()):
        cR = self.counter 
        if cR!= n:
            fun(*args)
            self.counter += 1
            return f"Function Runtime count {self.counter}"
        else:
            return None
            
        
