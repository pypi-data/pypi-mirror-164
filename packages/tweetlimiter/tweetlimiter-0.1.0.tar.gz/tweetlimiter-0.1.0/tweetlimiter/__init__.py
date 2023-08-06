
# Copyright (C) 2022 Frank Sauerburger

"""
Package to estimate the rate of a message stream and to limit the number of
message.
"""

__version__ = "0.1.0"  # Also change in setup.py

import math
from simple_pid import PID

class Limiter:
    """
    Adaptive tweet rate limiter accepting tweets from authors with most
    followers.

    Internally, a threshold is continuously adapted, accepting only tweets
    having more follows then the threshold.
    """
    def __init__(self,
                 target,
                 damp_rate=None,
                 pid_kp=1, pid_ki=0.3):


        def fill(value, default):
            return default if value is None else value

        self.target = target
        self.damp_rate = fill(damp_rate, target / 2)

        self.pid = PID(pid_kp, pid_ki, 0,
                       setpoint=-target,
                       output_limits=(0, 20))
        self.pid._integral = math.log(20 / target)

        self.rate = 0
        self.threshold = 0
        self.last = None

    def filter(self, time, follower):
        """
        Process the event and return decision object.

        Return a decision object whether the number of followers exceeds
        the threshold.
        """
        if self.last is None:
            delta = 1
        else:
            delta = time - self.last
        self.last = time

        if delta <= 0:
            # Wrong order of events, ignore
            return Decision(self.rate, 0, self.threshold)

        self.rate = math.exp(-delta * self.damp_rate) * self.rate  # damp

        decision = Decision(self.rate, follower, self.threshold)
        if decision:
            self.rate += self.damp_rate

        self.threshold = math.exp(self.pid(-self.rate, dt=delta))

        return decision

    def state(self):
        """Return current limiter values"""
        return {
            "rate": self.rate,
            "threshold": self.threshold,
        }

class Decision:
    """
    Objects represent decisions by the rate limiter which evaluate to bool
    """

    def __init__(self, rate, follower, threshold):
        """Evals to True if follower > threshold, otherwise False"""
        self.rate = rate
        self.follower = follower
        self.threshold = threshold

    def __bool__(self):
        """Return weather follower exceeds the threshold"""
        return self.follower > self.threshold

    def to_object(self):
        """Return contained metadata as a dictionary"""
        return {
            "accepted": bool(self),
            "rate": self.rate,
            "follower": self.follower,
            "threshold": self.threshold,
        }
