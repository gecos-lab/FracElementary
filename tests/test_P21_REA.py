from src.P21_REA import (
    sum
)
import os
import pytest


# @pytest.mark.skip(reason="Skipping this test for now because ...")
@pytest.mark.slow
def test_sum():
    assert sum(1, 2) == 3
    assert sum(2, 2) == 4