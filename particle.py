import numpy as np
import os
import math
import time

theta = 0
pi = np.pi
center = (15, 15)
r = 2

width, height = (30, 30)

n_iter = 360

electron_distance = 7



def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


# a**2 + b**2 - c**2 / 2ab
def calc_theta(current_pos):
    cu_x, cu_y = current_pos
    c_x, c_y = center
    # a_pow_2 = (c_x-cu_x)**2 + (c_y-cu_y)**2
    # b_pow_2 = r**2
    # c_pow_2 = (c_x+r-cu_x) ** 2 + (c_y-cu_y) ** 2

    a = euclidean_distance(c_x, c_y, cu_x, cu_y)
    b = euclidean_distance(cu_x, cu_y, c_x, c_y)
    c = euclidean_distance(c_x+r, c_y, cu_x, cu_y)


    cos_theta = (a**2 + b**2 - c**2) / (2 * a * b)

    angle = math.degrees(math.acos(cos_theta))

    return angle


for _ in range(n_iter):
    theta += 1
    for x in range(width+1):
        for y in range(height+1):
			# drawing circle
            c_x, c_y = center
            
            if euclidean_distance(x, y, c_x, c_y) >= electron_distance-0.5 and euclidean_distance(x, y, c_x, c_y) < electron_distance+0.5:
                cu_angle = calc_theta((x, y))
                if (theta%360) + 0.5 >= cu_angle and cu_angle >= (theta%360) -0.5:
                    if theta % 360 < 180 and y-c_y<0:
                        # print(theta, cu_angle, x, y)
                        print("x", end="")
                    elif theta % 360 > 180 and y-c_y>0:
                        # print(theta, cu_angle, x, y)
                        print("y", end="")
                else:
                    print(" ", end="")

            elif euclidean_distance(x, y, c_x, c_y) <= r:
                print("*", end="")
            else:
                print(" ", end="")
		
        print("\n")
    
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')