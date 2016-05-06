from PIL import Image
import glob

images = glob.glob("*.jpg")
print images
ignored = ['banner.jpg', 'coding.jpg', 'pic01.jpg', 'pic02.jpg', 'pic03.jpg', 'seasons.jpg', 'soc.jpg']

for image in images:
    if image not in ignored:
        print image
        im = Image.open(image)
        h = im.height
        w = im.width
        aspectratio= w*1.0/h
        req_ratio = 1920.0/1080

        print "OG height: " + str(int(h)) + " OG width: " + str(int(w))
        if aspectratio > req_ratio:
            w = h*req_ratio
            im = im.resize((int(w), int(h)), Image.ANTIALIAS)
        else:
            h = w/req_ratio
            im = im.resize((int(w), int(h)), Image.ANTIALIAS)
        print "New height: " + str(int(h)) + " New width: " + str(int(w))
        im.save(image)
        im.close
    

