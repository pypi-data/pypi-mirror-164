from .libs import *
from .other import *
def show(img):
    plt.imshow(img)
def save(name, img):
    cv2.imwrite(name, np.array(img))
def addrend(r1, r2, width, heigth):
    out = []
    for i in range(width):
        out.append([])
        for j in range(heigth):
            r1_ = r1[i][j]
            r2_ = r2[i][j]
            if r1_ == (0, 0, 0) and not r2_ == (0, 0, 0):
                out[len(out)-1].append(r2_)
            elif not r1_ == (0, 0, 0) and r2_ == (0, 0, 0):
                out[len(out)-1].append(r1_)
            else:
                out[len(out)-1].append(r1_)
    return out