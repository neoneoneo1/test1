import timeit
tt=timeit.Timer('v=a; c=b','a=10;b=20')
print tt.timeit()
tt=timeit.Timer('v,c=a,b','a=10;b=20')
print tt.timeit()

#Хз тесты своих функций какие-то
import doctest
def average(values):
    """comment
    print average(20,30,70)
    """
    return 3/len(values)
doctest.testmod()
average(['1'])

#тоже тесты тира гугловских
import unittest
class TestMy(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20,30,70],70,0))
        
unittest.main()
