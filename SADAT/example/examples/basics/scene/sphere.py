# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

"""
This example demonstrates how to create a sphere.
"""

import sys

import np as np
from vispy import scene
from vispy.visuals.transforms import STTransform
import numpy as np

canvas = scene.SceneCanvas(keys='interactive', bgcolor='white',
                           size=(800, 600), show=True)

view = canvas.central_widget.add_view()
view.camera = 'arcball'

# sphere1 = scene.visuals.Sphere(radius=1, method='latitude', parent=view.scene,
#                                edge_color='black')
#
# sphere2 = scene.visuals.Sphere(radius=1, method='ico', parent=view.scene,
#                                edge_color='black')

#cube = scene.visuals.Cube(color=(0.5, 0.5, 1, 0), edge_color='black', parent=view.scene)

box = scene.visuals.Box(width=1, height=2, depth=3, color=(0.5,0.5,1,0), edge_color='black', parent=view.scene)
# sphere3 = scene.visuals.Sphere(radius=1, rows=10, cols=10, depth=10,
#                                method='cube', parent=view.scene,
#                                edge_color='black')

#sphere1.transform = STTransform(translate=[-2.5, 0, 0])
#cube.transform = STTransform(translate=[2.5, 0, 0])

view.camera.set_range(x=[-3, 3])

if __name__ == '__main__' and sys.flags.interactive == 0:
    canvas.app.run()
