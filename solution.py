import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import scipy.stats as st

chat_id = 323297403  # Your chat ID, do not change the variable name

def solution(control: np.ndarray, test: np.ndarray) -> bool:
    alpha = 0.04

    control_mean = np.mean(control)
    test_mean = np.mean(test)
    control_std = np.std(control, ddof=1)
    test_std = np.std(test, ddof=1)

    dof = len(control) + len(test) - 2
    pooled_std = np.sqrt(((len(control)-1) * control_std ** 2 + (len(test)-1) * test_std ** 2) / dof)
    effect_size = abs(test_mean - control_mean) / pooled_std
    
    t_statistic, p_value = st.ttest_ind(control, test, equal_var=False)

    if p_value < alpha and effect_size > 0.2:
        return True
    else:
        return False
