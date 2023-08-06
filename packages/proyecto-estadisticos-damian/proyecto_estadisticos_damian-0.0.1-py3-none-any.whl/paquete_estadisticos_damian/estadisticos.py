class Estadisticos:
  def __init__(self,x:list):
        self.x=x
        self.n=len(self.x)
        self.c=self.x.count
  def media(self):
    return sum(self.x)/len(self.x)
  def mediana(self):
    mitad= len(self.x)//2
    self.x.sort()
    if not len(self.x) % 2:
      return (self.x[mitad -1]+ self.x[mitad])/2.0
    return self.x[mitad]
  def moda(self):
    modal=[]
    con = 0
    for num in self.x:
        if self.x.count(num) > con:
            modal=[]
            modal.append(num)
            con = self.x.count(num)
        elif self.x.count(num)==con:
            if not num in modal:
                 modal.append(num)
                 con = self.x.count(num)
    return modal
  def varianza(self):
    y=[]
    for i in self.x:
      y.append((i-(sum(self.x)/len(self.x)))**2)
    return (sum(y))/(len(self.x)-1)
  def desviacion(self):
   return self.varianza()** 0.5
  def coeficiente_desv(self):
    return ((self.varianza()** 0.5)/(sum(self.x)/len(self.x)))
  def curtosis(self):
    y=[]
    for i in self.x:
      y.append(((i)-(sum(self.x)/len(self.x)))**4)
    #return sum(y)
    return (sum(y)/((self.n)*(self.desviacion()**4)))
  def simetria(self):
    y=[]
    for i in self.x:
      y.append(((i)-(sum(self.x)/len(self.x)))**3)
    #return sum(y)
    return (sum(y)/((self.n)*(self.desviacion()**3)))