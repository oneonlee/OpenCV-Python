import cv2
import numpy as np

# Change the values you want, between 0 to 255.
value_b = 244
value_g = 244
value_r = 244

# You should use the image file with a transparent background, such as '.png'. 
overlay_img = cv2.imread('ship.png', cv2.IMREAD_UNCHANGED)

overlay_img_h, overlay_img_w, overlay_img_c = overlay_img.shape

background_img = np.zeros((overlay_img_h, overlay_img_w, 3), dtype=np.uint8)
background_img[:] = (value_b, value_g, value_r)

overlay_alpha = overlay_img[:, :, 3:] / 255.0
background_alpha = 1.0 - overlay_alpha

background_img[:, :] = overlay_alpha * overlay_img[:, :, :3] + background_alpha * background_img[:, :]

cv2.imshow("img", background_img)
cv2.waitKey(0)