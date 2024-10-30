import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from pprint import pprint
pprint(sys.path)
from main import main as func_main
from unittest import TestCase, main





class UiTest(TestCase):
    def test_answer(self):
        self.assertEqual(func_main(), "Congratulations! You have successfully registered!")


if __name__ == '__main__':
    main()

    
    
    # "Congratulations! You have successfully registered!"