
def convert_seconds(seconds):
    parts = []
    hours = seconds // 3600
    if hours > 0:
        parts.append("{} hour{}".format(hours, "s" if hours != 1 else ""))
    seconds %= 3600
    minutes = seconds // 60
    if minutes > 0:
        parts.append("{} minute{}".format(minutes, "s" if minutes != 1 else ""))
    seconds %= 60
    if seconds > 0:
        parts.append("{} second{}".format(seconds, "s" if seconds != 1 else ""))
    return " ".join(parts)