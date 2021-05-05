from os import listdir
import imageio


def giffer(num_iteration, name):
    filenames = []
    for i in range(0, num_iteration):
        filenames.append(str(i) + '.png')
    # end

    dir = '/plots/'
    images = []
    for filename in filenames:
        images.append(imageio.imread(dir + str(filename)))
    imageio.mimsave("/src/" + name, images, fps=8)
# end
