import weakref, gc
class A:
    def __init__(self,val):
        self.value=val
    def __repr__(self):
        return str(self.value)
a=A(10)
wr=weakref.WeakValueDictionary()
wr['wr1']=a
print wr['wr1']
del a
gc.collect()
#После удаления слабой ссылки все переменные сслающиеся на ней удаляются и выполняется очистка мусора
#print wr['wr1']
#print wr