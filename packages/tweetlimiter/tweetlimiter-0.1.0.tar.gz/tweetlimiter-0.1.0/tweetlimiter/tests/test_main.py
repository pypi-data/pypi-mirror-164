
# Copyright (C) 2022 Frank Sauerburger

import unittest
import tweetlimiter as tl

class LimiterTest(unittest.TestCase):
    """Test the Limiter class"""

    def test_initial_state(self):
        """Check the initial state"""
        limiter = tl.Limiter(target=1, damp_rate=0.1)
        state = limiter.state()
        self.assertEqual(state["rate"], 0)

    def test_rate_estimate(self):
        """Check the rate estimate"""
        limiter = tl.Limiter(target=1, damp_rate=0.1)
        state = limiter.state()

        limiter.filter(0, state["threshold"] + 1)
        state = limiter.state()
        self.assertAlmostEqual(state["rate"], 0.1)

        limiter.filter(1, state["threshold"] * 2)
        state = limiter.state()
        self.assertAlmostEqual(state["rate"], 0.19048374180359595)

    def test_threshold_surge(self):
        """Check that the threshold is adjusted"""
        limiter = tl.Limiter(target=1, damp_rate=0.1)

        # bring to eqiv
        for i in range(100):
            state = limiter.state()
            limiter.filter(i, state["threshold"] + 1)

        pre = limiter.state()

        # Simulate surge
        for i in range(100):
            state = limiter.state()
            limiter.filter(100 + i / 10, state["threshold"] + 1)

        post = limiter.state()
        self.assertGreater(post["threshold"], pre["threshold"])

    def test_threshold_quite(self):
        """Check that the threshold is adjusted"""
        limiter = tl.Limiter(target=1, damp_rate=0.1)

        # bring to eqiv
        for i in range(100):
            state = limiter.state()
            limiter.filter(i, state["threshold"] + 1)

        pre = limiter.state()

        # Simulate silence
        limiter.filter(200, 0)

        post = limiter.state()
        self.assertLess(post["threshold"], pre["threshold"])


class DecisionTest(unittest.TestCase):
    """Test the Decision class"""

    def test_true(self):
        """Check that the object evaulates to true"""
        decision = tl.Decision(0.1, 1000, 999)
        self.assertTrue(decision)

        decision = tl.Decision(100000, 1000, 999)
        self.assertTrue(decision)

    def test_false(self):
        """Check that the object evaulates to false"""
        decision = tl.Decision(0.1, 999, 1000)
        self.assertFalse(decision)

        decision = tl.Decision(100000, 999, 1000)
        self.assertFalse(decision)
