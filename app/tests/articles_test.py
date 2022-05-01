import unittest
from app.models import Articles, Source

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the source class
    '''
    
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_articles = Articles("engadget", "Engadget", "Igor Bonifacic", "Apple’s second-generation AirPods are back down to $100","If you missed the chance to buy Apple’s second-generation AirPods when they were $100 a few weeks ago", "https://www.engadget.com/amazon-airpods-beats-studio-pro-sale-164248746.html", "https://s.yimg.com/os/creatr-uploaded-images/2020-07/c9ee07d0-c117-11ea-b67f-851aefcf30f2", "2022-05-01T16:42:48Z", "If you missed the chance to buy Apples second-generation AirPods when they were $100 a few weeks ago")
            
    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))