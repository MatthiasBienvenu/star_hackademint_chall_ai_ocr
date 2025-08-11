import os
from PIL import Image
import pytesseract as pt
import numpy as np
import cv2


def unrotate(pil_img: Image.Image) -> Image.Image:
    # Convert PIL to OpenCV format
    img_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    # Convert to grayscale and invert
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)

    # Threshold to binary
    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Get coordinates of the non-zero pixels
    coords = np.column_stack(np.where(bw > 0))

    if coords.shape[0] < 10:
        print("Not enough content to determine skew.")
        return pil_img  # Return original if not enough text

    angle = cv2.minAreaRect(coords)[-1]

    if angle > 45:
        angle = -angle + 90
    else:
        angle = -angle

    (h, w) = img_cv.shape[:2]
    center = (w // 2, h // 2)

    # jsp pk mais le rotation est correcte à n*90 deg près donc dans le doute on met les +0, +90, +180 et +270
    M = [
        cv2.getRotationMatrix2D(center, angle + 90*i, 1.0)
        for i in range(4)
    ]
    unrotated = [
        cv2.warpAffine(img_cv, M[i], (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        for i in range(4)
    ]

    # Convert back to PIL
    return [
        Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        for img in unrotated
    ]



images = [Image.open(f"corbeille/{i}.png") for i in range(len(os.listdir("corbeille")))]
unrotated = [x for img in images for x in unrotate(img)]

words = [pt.image_to_string(im).strip().lower() for im in unrotated]

for i, w in enumerate(words):
    if "gwilherm" in w:
        print(f"{i//4}.png")
        break
