# ----------------
# User Instructions
#
# Implement twiddle as shown in the previous two videos.
# Your accumulated error should be very small!
#
# Your twiddle function should RETURN the accumulated
# error. Try adjusting the parameters p and dp to make
# this error as small as possible.
#
# Try to get your error below 1.0e-10 with as few iterations
# as possible (too many iterations will cause a timeout).
# No cheating!
# ------------
import math as mth
import random
import numpy as np
import matplotlib.pyplot as plt
# import scipy as sc
# ------------------------------------------------
#
# this is the Robot class
#

class Robot(object):
    def __init__(self, length=20.0):
        """
        Creates robot and initializes location/orientation to 0, 0, 0.
        """
        self.x = 0.0
        self.y = 0.0
        self.orientation = 0.0
        self.length = length
        self.steering_noise = 0.0
        self.distance_noise = 0.0
        self.steering_drift = 0.0

    def set(self, x, y, orientation):
        """
        Sets a robot coordinate.
        """
        self.x = x
        self.y = y
        self.orientation = orientation % (2.0 * np.pi)

    def set_noise(self, steering_noise, distance_noise):
        """
        Sets the noise parameters.
        """
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.steering_noise = steering_noise
        self.distance_noise = distance_noise

    def set_steering_drift(self, drift):
        """
        Sets the systematical steering drift parameter
        """
        self.steering_drift = drift

    def move(self, steering, distance, tolerance=0.001, max_steering_angle=np.pi / 4.0):
        """
        steering = front wheel steering angle, limited by max_steering_angle
        distance = total distance driven, most be non-negative
        """
        if steering > max_steering_angle:
            steering = max_steering_angle
        if steering < -max_steering_angle:
            steering = -max_steering_angle
        if distance < 0.0:
            distance = 0.0

        # make a new copy
        # res = Robot()
        # res.length = self.length
        # res.steering_noise = self.steering_noise
        # res.distance_noise = self.distance_noise
        # res.steering_drift = self.steering_drift

        # apply noise
        steering2 = random.gauss(steering, self.steering_noise)
        distance2 = random.gauss(distance, self.distance_noise)

        # apply steering drift
        steering2 += self.steering_drift

        # Execute motion
        turn = np.tan(steering2) * distance2 / self.length

        if abs(turn) < tolerance:
            # approximate by straight line motion
            self.x += distance2 * np.cos(self.orientation)
            self.y += distance2 * np.sin(self.orientation)
            self.orientation = (self.orientation + turn) % (2.0 * np.pi)
        else:
            # approximate bicycle model for motion
            radius = distance2 / turn
            cx = self.x - (np.sin(self.orientation) * radius)
            cy = self.y + (np.cos(self.orientation) * radius)
            self.orientation = (self.orientation + turn) % (2.0 * np.pi)
            self.x = cx + (np.sin(self.orientation) * radius)
            self.y = cy - (np.cos(self.orientation) * radius)

    def __repr__(self):
        return '[x=%.5f y=%.5f orient=%.5f]' % (self.x, self.y, self.orientation)

############## ADD / MODIFY CODE BELOW ####################
# ------------------------------------------------------------------------
#
# run - does a single control run

def initialize_robot():
    """
    Resets the robot back to the initial position and drift.
    You'll want to call this after you call `run`.
    """
    robot = Robot()
    robot.set(0., 1., 0.)
    robot.set_steering_drift(10. / 180. * np.pi)
    return robot


# NOTE: We use params instead of tau_p, tau_d, tau_i
def run(robot, params, n=100, speed=1.0):
    x_trajectory = []
    y_trajectory = []
    err = 0
    prev_cte = robot.y
    int_cte = 0
    for i in range(2 * n):
        cte = robot.y
        # diff_cte = (cte - prev_cte) / speed
        diff_cte = (cte - prev_cte)
        int_cte += cte
        prev_cte = cte
        steerAngle = -params[0] * cte - params[1] * diff_cte - params[2] * int_cte
        robot.move(steerAngle, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
        if i >= n:
            err += cte ** 2
    return x_trajectory, y_trajectory, (err / float(n))


# Make this tolerance bigger if you are timing out!
#return params vector of tau_p, tau_d, tau_i
def twiddle(tol=0.2):
     # Don't forget to call `initialize_robot` before you call `run`!
    #params vector of tau_p, tau_d, tau_i
    pVector = [0., 0., 0.]
    difParmsVector = [1., 1., 0.]
    robot = initialize_robot()
    x_trajectory, y_trajectory, best_err = run(robot, pVector)

    it = 0
    while sum(difParmsVector) > tol:
        print("Iteration {}, best error = {}".format(it, best_err))
        for i in range(len(pVector)):
            pVector[i] += difParmsVector[i]
            robot = initialize_robot()
            x_trajectory, y_trajectory, err = run(robot, pVector)

            if err < best_err:
                best_err = err
                difParmsVector[i] *= 1.1
            else:
                pVector[i] -= 2 * difParmsVector[i]
                robot = initialize_robot()
                x_trajectory, y_trajectory, err = run(robot, pVector)

                if err < best_err:
                    best_err = err
                    difParmsVector[i] *= 1.1
                else:
                    pVector[i] += difParmsVector[i]
                    difParmsVector[i] *= 0.9
        it += 1
        print("Iteration {}, params {}, best error = {}".format(it, pVector, best_err))
    return pVector


params = twiddle()
robot = initialize_robot()
x_trajectory, y_trajectory, err = run(robot, params)
n = len(x_trajectory)
print("\n Final params {}, best error = {}".format(params, err))


plt.plot(x_trajectory, y_trajectory, 'g', label='PID controller')
plt.plot(x_trajectory, np.zeros(n), 'r', label='reference')
plt.legend()
plt.show()