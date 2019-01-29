class Trade:
    Status='ACCEPTED'
    Side='buy'
    Vol=123
    
    def toString(self):
        return self.Side+' '+ str(self.Vol) + ' Status: '+ self.Status

t = Trade()
print(t.Status)
print(t.Vol)
print(t.toString())
t.Side='sell'
print(t.toString())
