import numpy as np

blue = np.zero((2,3,3),np.uint8)

blue[:,:,0] = 255
blue.itemset((0:2,2:3,0),0)

print(blue)