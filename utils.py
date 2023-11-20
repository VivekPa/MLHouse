import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def plot_bars(x, y, ylabel, title=None):
    plt.figure(figsize=(12, 6))
    
    plt.bar(x, y)

    plt.xticks(rotation=90)
    plt.ylabel(ylabel)
    if title is None:
        plt.title(f"Bar Plot of {ylabel}")
    else:
        plt.title(title)

    plt.show()
