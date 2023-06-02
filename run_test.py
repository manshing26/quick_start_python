import os
import unittest
from testing.test_pdf import gen_sample
from testing.test_email import login_and_send

class TestAll(unittest.TestCase):
    
    def test_pdf(self):
        if os.path.isfile('tmp/test_pdf.pdf'):
            os.remove('tmp/test_pdf.pdf')
        self.assertEqual(gen_sample(),None)
        self.assertTrue(os.path.isfile('tmp/test_pdf.pdf'))
        
    def test_email(self):
        self.assertTrue(login_and_send())
        
        
if __name__ == "__main__":
    unittest.main()