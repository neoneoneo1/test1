#Красивый выводтекста с форматированием
import pprint
t=[['one','two','two2'],['three','four']]
pprint.pprint(t,width=20)

import textwrap
doc=u"Настоящий Протокол информационного взаимодействия устанавливает связи между УСК-80 и БРЭО на МиГ-29UPG (МиГ-29UPG UB), а также определяет Логику работы УСК-80 (далее по тексту – «УСК»)."
#print(textwrap.fill(doc.decode('utf8'),width=20))
print(textwrap.fill(doc,width=20))
