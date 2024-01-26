import numpy as np
from scipy.spatial.transform import Rotation as R

# SENSOR TRANSFORM ON CAR AXIS
# ZY'X''
# in degrees
Rx = 100 # roll
Ry = 0 # pitch
Rz = 90 # yaw

# translation in meters
Tx = 0.5
Ty = 0.16
Tz = 1.14

# ATTENTION: "ZYX" is case-sensitive
r_tf = R.from_euler('ZYX', [Rz, Ry, Rx], degrees=True)
r_tf_matrix = r_tf.as_matrix()

# translation matrix
t = np.matrix([[Tx], [Ty], [Tz]])

print("R_tf={}".format(r_tf_matrix))
print()

# INTRINSICS
fx = 241
fy = 238
cx = 636
cy = 548

# IMAGE COORDS
u = 872
v = 423
d = 1.9
x = np.matrix([[u], [v], [d]])

# IMAGE PLANE TO CAMERA FRAME
X_camera = np.matrix([
    [(u - cx) / fx],
    [(v - cy) / fy],
    [1]
    ])

# normalize to the distance (euclidean)
X_camera = X_camera / np.linalg.norm(X_camera) * d

# TRANSFORM TO CAR FRAME
X = (r_tf_matrix * X_camera) + t

print("X={}".format(X))