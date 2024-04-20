#importing function file
import printing_functions
printing_functions.printing(16, 'biography', 'photo', 'replica')

#from function file importing specific function
from printing_functions import printing
printing_functions.printing(8, 'book copy', 'statement', 'application form')

#importing function and alias function name
from printing_functions import printing as pr
pr(9, 'my statement', 'paperwork')

#importing function and giving alias to it
import printing_functions as prf
prf.printing(7, 'rules', 'copyrights')

#importing all functions
from printing_functions import *
printing(9, 'my last print', 'love letter')