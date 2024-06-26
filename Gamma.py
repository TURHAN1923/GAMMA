import cv2
import numpy as np

img = cv2.imread("trk.jpg")

for gamma in [0.1, 0.5, 1.5, 2.2]:
    
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype=np.uint8)
    
    cv2.imwrite('gamma_transformed_' + str(gamma) + '.jpg', gamma_corrected)
