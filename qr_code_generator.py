# import argparse
import qrcode

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--link', help="link for qr code generation", type=str, required=True)
    # parser.add_argument('--out_name', help="output name of generated qr code", type=str, required=True)
    # args = parser.parse_args()

    # main code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=1
    )
    qr.add_data("https://www.figma.com/proto/YPfsPv0hpQyt0Ju0BQNmX6/SkillFnab?page-id=1%3A13&node-id=967-3783&p=f&viewport=51%2C393%2C0.13&t=Jdtl0n2454Aj5ygp-1&scaling=scale-down&content-scaling=fixed&starting-point-node-id=265%3A3459")
    qr.make(fit=True)
    
    # create image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("skillfnab_prototype_qr.png")