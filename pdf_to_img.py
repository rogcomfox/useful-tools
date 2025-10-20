# import module
from pdf2image import convert_from_path
import argparse
import os
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser('', add_help=False)
    parser.add_argument('--filename', type=str, required=True)
    args = parser.parse_args()
    dir = Path(args.filename).stem
    os.mkdir(dir)

    # Store Pdf with convert_from_path function
    images = convert_from_path(args.filename)
    os.chdir(dir)

    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')
    