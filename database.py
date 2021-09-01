# print("This is the database.py module")
# print("It's name is {}".format(__name__))

import Blood_Calculator as BC
# from Blood_Calculator import HDL_Analysis
# from Blood_Calculator import * #(imports everything, avoid this)

answer = BC.HDL_Analysis(55)
print("The analysis of 55 HDL is {}".format(answer))

answer2 = BC.LDL_Analysis(200)
print("The analysis of 200 LDL is {}".format(answer2))