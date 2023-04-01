import matplotlib.pyplot as plt
from typing import List, Dict


def create_param_optimization_plot(param_values: List[Dict[str, float]], performance_metrics: List[float]) -> None:
    """
    Creates a visualization plot of the parameter optimization process.

    :param param_values: A list of parameter values for each iteration of the optimization process.
    :type param_values: List[Dict[str, float]]
    :param performance_metrics: A list of performance metrics for each iteration of the optimization process.
    :type performance_metrics: List[float]
    """
    # Get the parameter names from the first set of parameter values
    param_names = list(param_values[0].keys())

    # Create a sub-plot for each parameter
    fig, axs = plt.subplots(len(param_names), 1, figsize=(8, 8))
    
    # Set the title and axis labels for the sub-plots
    for i, param_name in enumerate(param_names):
        axs[i].set_title(param_name)
        axs[i].set_xlabel('Iteration')
        axs[i].set_ylabel(param_name)

    # Add the parameter values to each sub-plot
    for i, param_name in enumerate(param_names):
        axs[i].plot(range(len(param_values)), [params[param_name] for params in param_values])
    
    # Create a plot for the performance metric
    fig, ax = plt.subplots(1, 1, figsize=(8, 4))
    ax.set_title('Performance Metric')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')
    ax.plot(range(len(performance_metrics)), performance_metrics)

    plt.show()
