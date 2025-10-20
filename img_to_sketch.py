import argparse
import cv2 as cv
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img', help='image path to convert to sketch', type=str)
    parser.add_argument('--out', help='image name output result', type=str)
    args = parser.parse_args()

    img = cv.imread(args.img)
    # draw sketch
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    inv_gray_img = 255 - gray_img
    blur_inv_gray_img = cv.GaussianBlur(inv_gray_img, (21,21), sigmaX=0, sigmaY=0)
    inv_blur = 255 - blur_inv_gray_img
    sketch = cv.divide(gray_img, inv_blur, scale=256)
    # save to same folder
    ori_folder_path = os.path.dirname(args.img)
    new_save_path = os.path.join(ori_folder_path, args.out)
    cv.imwrite(new_save_path, sketch)