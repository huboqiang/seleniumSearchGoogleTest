from images2gif import writeGif
from PIL import Image
import os

for idx in [0, 1]:
    file_names = sorted((fn for fn in os.listdir('images/%d' % (idx)) if fn.endswith('.png') ))
    images = [Image.open("images/%d/%s" % (idx, fn)) for fn in file_names]
    filename = "browser%d.GIF" % (idx+1)
    writeGif(filename, images, duration=0.5)
