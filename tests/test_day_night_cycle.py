import pytest
import math
from gameplay import day_night_cycle as mod

CASES = [
    ("time", 'm.time_of_day(25, 24) == 1'),
    ("sun", 'm.sun_intensity(0.5) == 0.5'),
    ("shadow", 'm.shadow_direction(-1) == -1'),
    ("ambient", 'm.ambient_for("night") == "night"'),
    ("moon", 'm.moon_intensity(0.5) == 0.5'),
    ("weather", 'm.weather_dim(1, 0.5) == approx(0.75)'),
    ("tz", 'm.timezone(8) == 8'),
    ("trans", 'm.transition(0.5) == 0.5'),
    ("rebake", 'm.rebake(0.6) is True'),
    ("sync", 'm.sync(10, 5) == 10'),
    ("night", 'm.is_night(-1) is True'),
    ("clamp", 'm.clamp01(1.2) == 1.0'),
    ("key", 'm.key("cst") == "tz:cst"'),
    ("frac", 'm.day_fraction(12, 24) == approx(0.5)'),
    ("lerp", 'm.lerp(0, 10, 0.5) == 5')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
