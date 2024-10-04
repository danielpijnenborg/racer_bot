from typing import Tuple

from pygame import Vector2

from ...bot import Bot
from ...linear_math import Transform


class Racinator(Bot):
    @property
    def name(self):
        return "Racinator"

    @property
    def contributor(self):
        return "Daniel"

    def compute_commands(self, next_waypoint: int, position: Transform, velocity: Vector2) -> Tuple:
        target = self.track.lines[next_waypoint]
        next_point = next_waypoint +1
        if next_point >= len(self.track.lines):
            next_point = 0
        next_target = self.track.lines[next_point]
        # calculate the target in the frame of the robot
        target = position.inverse() * target
        next_target = position.inverse() * next_target
        # calculate the angle to the target
        angle = target.as_polar()[1]
        dist = target.as_polar()[0]
        next_dist = (next_target-target).length()
        # calculate the throttle
        
        target_velocity = 60+min(1.8*dist,2.8*next_dist)
        throttle = 2*( target_velocity-velocity.length())


        # calculate the steering
        if angle > 0:
            return throttle, 1
        else:
            return throttle, -1
