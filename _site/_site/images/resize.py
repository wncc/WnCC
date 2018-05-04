from PIL import Image
import glob

images = glob.glob("*")
print images
ignored = ['banner.jpg', 'coding.jpg', 'pic01.jpg', 'pic02.jpg', 'pic03.jpg', 'seasons.jpg', 'soc.jpg', 'resize.py','HoldTheBeat.png','JARVIS.jpg','404.png','collaborations','team','initiatives','yahoohacku-eventCover.jpg']

for image in images:
    if image not in ignored:
        print image
        im = Image.open(image)
        w,h = im.size
        aspectratio= w*1.0/h
        req_ratio = 1920.0/1080

        print "OG width: " + str(int(w)) + " OG height: " + str(int(h))
        if aspectratio > req_ratio:
            w = h*req_ratio
            im = im.resize((int(round(w)), int(round(h))), Image.ANTIALIAS)
        else:
            h = w/req_ratio
            im = im.resize((int(round(w)), int(round(h))), Image.ANTIALIAS)
        print "New width: " + str(int(round(w))) + " New height: " + str(int(round(h)))
        im.save(image)