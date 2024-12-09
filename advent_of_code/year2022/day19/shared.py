import re
from math import ceil
from operator import add, sub
from typing import NamedTuple


# Tuple class with element-wise comparison and arithmetic
# One can simply use numpy arrays but this solution uses native python
class Resources(NamedTuple):
    ore: int
    clay: int
    obs: int
    geode: int

    def __le__(self, other):
        return all(x <= y for x, y in zip(self, other))

    def __ge__(self, other):
        return all(x >= y for x, y in zip(self, other))

    def __lt__(self, other):
        return all(x < y for x, y in zip(self, other))

    def __gt__(self, other):
        return all(x > y for x, y in zip(self, other))

    def __add__(self, other):
        return Resources(*map(add, self, other))

    def __sub__(self, other):
        return Resources(*map(sub, self, other))


opt = {t: t * (t - 1) // 2 for t in range(50)}


class Blueprint:
    def __init__(self, n: int, blueprint):
        self.id: int = n
        self.blueprint = blueprint
        self.max_ore: int = max(r.ore for r, _ in blueprint)
        self.max_clay: int = max(r.clay for r, _ in blueprint)
        self.max_obs: int = max(r.obs for r, _ in blueprint)
        self.min_obs: int = self.max_obs
        self.best: int = 0
        self.memo: dict = dict()

    def dfs(self, robots: Resources, resources: Resources, avail: set, t: int) -> int:
        """Depth first search to find the maximum number of geodes that can be made in t minutes"""
        # If this state has already been calculated then return it
        if (robots, resources, t) in self.memo:
            return self.memo[(robots, resources, t)]

        # If time remaining is 1 then there isn't enough time to make more robots and max geodes is
        # the number of geodes we have plus the number of geode robots
        if t == 1:
            return resources.geode + robots.geode

        # If the most optimistic number of geodes we can get with time t remaining
        # is less than the best score seen so far then stop
        if resources.geode + robots.geode * t + opt[t] <= self.best:
            return 0

        # If enough obs cannot be made to make more geode robots then
        # number of geodes can already be calculated with time t remaining
        if resources.obs + robots.obs * t + opt[t] <= self.max_obs:
            return resources.geode + robots.geode * t

        # Max number of robots needed is the max amount of that resource needed in a minute
        if robots.ore > self.max_ore or robots.clay > self.max_clay or robots.obs > self.max_obs:
            return 0

        # If robots are maxed out and resources are more than max set resource to max
        # This reduces the number of states that need to be calculated and helps memoization
        if resources.ore > self.max_ore and robots.ore == self.max_ore:
            resources = Resources(self.max_ore, resources.clay, resources.obs, resources.geode)
        if resources.clay > self.max_clay and robots.clay == self.max_clay:
            resources = Resources(resources.ore, self.max_clay, resources.obs, resources.geode)

        # Try to make each type of robot starting from the geode, then obs, then clay, then ore
        for cost, prod in self.blueprint:
            # If this robot could have been made in the past then skip this branch
            if prod in avail:
                continue
            # If there are enough resources to make this robot then start a new branch and make it
            if cost <= resources:
                score = self.dfs(robots + prod, resources - cost + robots, set(), t - 1)
                self.best = max(score, self.best)
                # Add this robot to the set of robots that could have been made
                avail.add(prod)

        # Do not make any robots and just wait a minute
        # Resources generated are equal to the number of robots already existing and
        # the number of available robots are robots that could have been made but were not
        score = self.dfs(robots, resources + robots, avail, t - 1)
        self.best = max(score, self.best)

        # Store the state in memo
        self.memo[(robots, resources, t)] = self.best

        return self.best

    def max_geodes(self, t: int) -> int:
        score = self.dfs(Resources(1, 0, 0, 0), Resources(0, 0, 0, 0), set(), t)
        return score


def parse_input(text: str) -> list[Blueprint]:
    pattern = re.compile(r'\d+')

    blueprints = []
    for line in text.splitlines():
        match = pattern.findall(line)
        b, o, c, ob_o, ob_c, g_o, g_ob = map(int, match)
        # Blueprint is a list of tuples where the first element is the cost of a robot
        # and the second element is the resources produced by that robot
        # Robot order is: geode, obs, clay, ore
        # Resource order is: ore, clay, obs, geode
        blueprint = (
            (Resources(g_o, 0, g_ob, 0), Resources(0, 0, 0, 1)),
            (Resources(ob_o, ob_c, 0, 0), Resources(0, 0, 1, 0)),
            (Resources(c, 0, 0, 0), Resources(0, 1, 0, 0)),
            (Resources(o, 0, 0, 0), Resources(1, 0, 0, 0)),
        )

        blueprints.append(Blueprint(b, blueprint))
    return blueprints
