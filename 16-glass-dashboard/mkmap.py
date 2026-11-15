# Lens map for a W x H rounded rectangle: R/G = how far to sample INWARD near the rim (128 = no shift). Usage: mkmap.py W H radius rim_px out.png
import numpy as np, sys
from PIL import Image
W, H, rad, rim = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
y, x = np.mgrid[0:H, 0:W] + 0.5
px, py = x - W / 2, y - H / 2
qx, qy = np.abs(px) - (W / 2 - rad), np.abs(py) - (H / 2 - rad)
d = rad - np.hypot(np.maximum(qx, 0), np.maximum(qy, 0)) - np.minimum(np.maximum(qx, qy), 0)   # distance inside the edge
# outward normal: corner = from the corner centre, straight side = the nearer axis
nx = np.where((qx > 0) & (qy > 0), qx, np.where(qx > qy, 1.0, 0.0)) * np.sign(px)
ny = np.where((qx > 0) & (qy > 0), qy, np.where(qx > qy, 0.0, 1.0)) * np.sign(py)
n = np.hypot(nx, ny) + 1e-9
t = np.clip(1 - d / rim, 0, 1); f = t * t * (3 - 2 * t) * (d >= 0)   # 0 in the middle -> 1 at the edge
R, G = 128 - 127 * f * nx / n, 128 - 127 * f * ny / n
img = np.dstack([R, G, np.full_like(R, 128)]).clip(0, 255).astype(np.uint8)
assert img[H // 2, W // 2].tolist() == [128, 128, 128] and img[1, W // 2, 1] > 200 and img[H // 2, 1, 0] > 200, "map: centre neutral, top rim pushes down, left rim pushes right"
Image.fromarray(img).save(sys.argv[5], optimize=True)
