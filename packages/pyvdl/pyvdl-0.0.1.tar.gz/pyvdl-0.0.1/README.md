# vectors-draw-lib or pyvdl
## request
matplotlib

numpy

cv2
## doc and example
'''

    import pyvdl
    class circle(pyvdl.obj):
        def __init__(self, r=pyvdl.np.pi):
            self.radius = r
        def render(self, x, y):
            a = self.abs_(x, y)
            return a - self.radius
    c = pyvdl.render(circle(50), 500, 500)
    pyvdl.show(c)
    pyvdl.save("circle.png", c)

'''

'''

    create new object:
        class test(pyvdl.obj):
            def __init__(self):
                pass
            def render(self, x, y):
                pass
    render:
        c = pyvdl.render(test(), 500, 500)
    show:
        pyvdl.show(c)
    save:
        pyvdl.save("circle.png", c)
        
'''