import math

def time_of_day(time, day):
    """真实时间。"""
    raise NotImplementedError("TODO: time_of_day")

def sun_intensity(sin_alt):
    """光照曲线。"""
    raise NotImplementedError("TODO: sun_intensity")

def shadow_direction(alt):
    """阴影翻转。"""
    raise NotImplementedError("TODO: shadow_direction")

def ambient_for(phase):
    """环境光随时段。"""
    raise NotImplementedError("TODO: ambient_for")

def moon_intensity(sin_alt):
    """月亮光源。"""
    raise NotImplementedError("TODO: moon_intensity")

def weather_dim(intensity, rain):
    """天气影响。"""
    raise NotImplementedError("TODO: weather_dim")

def timezone(hours):
    """服务器时区。"""
    raise NotImplementedError("TODO: timezone")

def transition(alpha):
    """平滑过渡。"""
    raise NotImplementedError("TODO: transition")

def rebake(delta):
    """按时段重烘焙。"""
    raise NotImplementedError("TODO: rebake")

def sync(server, client):
    """网络同步时间。"""
    raise NotImplementedError("TODO: sync")

def is_night(alt):
    """夜晚判定。"""
    raise NotImplementedError("TODO: is_night")

def clamp01(value):
    """归一钳制。"""
    raise NotImplementedError("TODO: clamp01")

def key(zone):
    """时区键。"""
    raise NotImplementedError("TODO: key")

def day_fraction(time, day):
    """日照比例。"""
    raise NotImplementedError("TODO: day_fraction")

def lerp(a, b, t):
    """插值。"""
    raise NotImplementedError("TODO: lerp")
