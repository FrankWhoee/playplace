import imageio as iio

# read an image
# img = iio.imread("Swift_Folklore.jpg")
# for i in img:
#     for j in i:
#         print(j)
with open("Swift_Folklore.jpg", "rb") as f:
    print(f.read(1000000))
        # Do stuff with byte.