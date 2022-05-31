import imageio

files = [
    r"\Users\danec\Desktop\Seminar Material\images\base.jpeg"
]

bad_nodes = [21, 31, 81, 88, 102, 199]

for it in range(250):
    if it not in bad_nodes:
        files.append(rf"\Users\danec\Desktop\Seminar Material\images\update_{it}.jpeg")

jpeg_dir = r'\Users\danec\Desktop\Seminar Material\animation'
images = []
for file_name in files:
    # print(file_name)
    images.append(imageio.imread(file_name))
imageio.mimsave(r'\Users\danec\Desktop\Seminar Material\animation\animation_5fps.gif', images, fps=5)