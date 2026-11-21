import numpy as np
from services.mode import findMode

def calculate_statistics(data: list) -> dict:
    if not data:
        return {
            "mean": None,
            "median": None,
            "std": None,
            "variance": None,
            "mode": None
        }

    np_data = np.array(data)
    mean_val = np.mean(np_data)
    median_val = np.median(np_data)
    # TODO 1A: Calculate population variance from np_data.
    # Keep the population definition used in the original example (ddof=0).
    var_val = np.var(np_data, ddof=0)

    # TODO 1B: Calculate population standard deviation from np_data.
    std_val = np.std(np_data, ddof=0)

    mode_val = findMode(data)

    return {
        "mean": float(mean_val),
        "median": float(median_val),
        "std": float(std_val) if std_val is not None else None,
        "variance": float(var_val) if var_val is not None else None,
        "mode": mode_val
    }