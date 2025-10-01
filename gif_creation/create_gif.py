import imageio.v3 as iio

filenames = "C:\Git\Codedex\gif_creation\\dino1.png", "C:\Git\Codedex\gif_creation\\dino2.png", "C:\Git\Codedex\gif_creation\\dino3.png", "C:\Git\Codedex\gif_creation\\dino4.png"
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("dino.gif", images, duration = 500, loop = 0)