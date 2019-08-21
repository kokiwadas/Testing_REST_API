from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b1 = Blog('Test_1', 'Test Author')
        b2 = Blog('Test_2', 'Test Author Numero Due')
        self.assertEqual(b1.__repr__(), 'Test_1 by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'Test_2 by Test Author Numero Due (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        b2 = Blog('Test_1', 'Test Author Two')
        b2.posts = ['test', 'test1']
        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'Test_1 by Test Author Two (2 posts)')
