import cv2
import numpy as np

# Image load kar
# img = cv2.imread("/home/shoarya/Desktop/open-cv/pexels-eugeniofr-30005297.jpg")

# Resize (optional)
def circle(img):
    img = cv2.resize(img, (300, 300))

    # Mask banao
    mask = np.zeros_like(img)
    h, w = img.shape[:2]
    center = (w//2, h//2)
    radius = min(center[0], center[1])

    # Circle draw kar mask me
    cv2.circle(mask, center, radius, (255, 255, 255), -1)

    # Mask apply kar
    circular = cv2.bitwise_and(img, mask)
    return circular
    # Save kar circular image
    # cv2.imwrite("circular_profile.png", circular)
