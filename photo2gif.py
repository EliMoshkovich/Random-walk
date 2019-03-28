from PIL import Image, ImageDraw


# class p2g():

    # def create(self):
        # im = Image.new("RGB", (200, 200), 'green')
        # names = ['img{:02d}.gif'.format(i) for i in range(2)]
        # pos = 0
        # for n in names:
        #     frame = im.copy()
        #     draw = ImageDraw.Draw(frame)
        #     draw.ellipse((pos, pos, 50+pos, 50+pos),
        #                  'red')
        #     frame.save(n)
        #     pos += 10
        #
        # # Open all the frames
        # images = []
        #
        # for n in names:
        #     frame = Image.open(n)
        #     images.append(frame)

images = ['books_read1.png','books_read2.png']
# Save the frames as an animated GIF
im=[]
im.save('anicircle.gif',
               save_all=True,
               append_images=images[1:],
               duration=100,
               loop=0)
images[0].save('anicircle.gif',
               save_all=True,
               append_images=images[1:],
               duration=100,
               loop=0)