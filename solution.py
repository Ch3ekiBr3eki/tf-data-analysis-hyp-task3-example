import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import scipy.stats as st

chat_id = 323297403  # Ваш chat ID, не меняйте название переменной

def solution(control: np.ndarray, test: np.ndarray) -> bool:
    alpha = 0.04 

    control_mean = np.mean(control)
    test_mean = np.mean(test)

    t_statistic, p_value = st.ttest_ind(control, test, equal_var=False)

    if p_value < alpha:
        return True
    else:
        return False
