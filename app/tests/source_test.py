import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the source class
    '''
    
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_source = Source('ansa','ANSA.it','news analysis','general','en','us','url')
            
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))