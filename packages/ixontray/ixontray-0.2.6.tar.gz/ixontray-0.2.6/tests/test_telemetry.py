# ------------------------------------------------------------------
# Copyright (C) Smart Robotics - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly
# prohibited. All information contained herein is, and remains
# the property of Smart Robotics.
# ------------------------------------------------------------------
import numpy
from functools import reduce

from ixontray.telemetry import FunctionCall


def sum_it(a, b):
    return a + b


def test_function_call_addition() -> None:
    """Test adding two Function call objects"""

    durations = [2.1, 3.1, 5.1, 2.1, 5.1, 7.1]
    calls = [FunctionCall(name=f"fun_{i}", duration=d) for i, d in enumerate(durations) ]

    result = reduce(sum_it, calls)

    assert result.duration == numpy.average(durations), "Averages should match"
    assert result.min_duration == min(durations), "Min should match"
    assert result.max_duration == max(durations), "Max should match"

def test_function_call():
    fc = FunctionCall(name=f"fun_1", duration=10)

    assert fc.duration == 10
    assert fc.min_duration == 10
    assert fc.max_duration == 10
    print(fc)