import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 323297403  # Ваш chat ID, не меняйте название переменной

def solution(control: np.ndarray, test: np.ndarray) -> bool:
    _, p_value = ttest_ind(control, test, equal_var=False)
    significance_level = 0.04
    return p_value < significance_level
