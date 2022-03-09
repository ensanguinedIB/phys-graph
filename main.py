"""A tool to plot graphs for AQA A-level physics required practicals."""

from math import ceil, log10

import matplotlib.pyplot as plt
import numpy as np


def round_sig(x, figures):
    if x == 0:
        return 0
    
    # sign = True if x < 0 else False

    magnitude_diff = ceil(log10(abs(x)))
    power = figures - magnitude_diff

    magnitude = 10 ** power
    shifted = round(x * magnitude)

    rounded = shifted / magnitude
    rounded = str(rounded)

    while len(rounded.replace("-", "").replace(".", "")) < figures:
        rounded = rounded + "0"

    return rounded


class Graph:
    def __init__(self, x, y, x_err=None, y_err=None, accuracy=3,
                 title="Graph", x_label="Independent variable", y_label="Dependent variable",
                 force_origin=True):
        # Get graph from matplotlib
        self.fig, self.ax = plt.subplots()

        # Data variables
        self.x = np.array(x)
        self.y = np.array(y)
        self.x_err = x_err
        self.y_err = y_err

        # TODO: Infer accuracy from data
        self.accuracy = accuracy

        # Textual variables
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

        # Flags
        self.force_origin = force_origin
    
    def __add_gridlines(self):
        # Ticks must be shown on axes to show minor gridlines
        plt.minorticks_on()

        # Adjust gridlines
        self.ax.grid(which="major", color="gray", linewidth=0.6)
        self.ax.grid(which="minor", color="lightgray", linewidth=0.6)

    def __add_text(self):
        # Add self.axis and graph labels
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)

        # Display line names
        self.ax.legend()
    
    def __show_origin(self):
        # Find the mself.aximum points on the graph
        if self.x_err:
            x_max = max(self.x + self.x_err)
        else:
            x_max = max(self.x)
        
        if self.y_err:
            y_max = max(self.y + self.y_err)
        else:
            y_max = max(self.y)
        
        # Adjust the view to include the origin and mself.ax points
        self.ax.set_xlim(left=0, right=x_max * 1.1)
        self.ax.set_ylim(bottom=0, top=y_max * 1.1)
    
    def __plot_points(self):
        # Add data points
        self.ax.scatter(self.x, self.y, color="black", s=30, marker="x", linewidths=0.6)

        # Add error bars
        self.ax.errorbar(self.x, self.y, xerr=self.x_err, yerr=self.y_err,
                         color="black", linewidth=0.6, fmt="none", capsize=4, capthick=0.6)
    
    def __plot_lines(self):
        # Use numpy's polyfit to perform a linear regression on the data
        (m_b, c_b), cov = np.polyfit(self.x, self.y, 1, cov=True)
        
        # Interpret worst gradient and intercept
        (m_err, c_err) = np.sqrt(np.diag(cov))
        m_w = m_b + m_err
        c_w = c_b - c_err

        # Two points to draw line through
        endpoints = np.array([0, max(self.x) * 1.1])

        # Labels for the legend
        best_label = f"Best fit line: m = {round_sig(m_b, self.accuracy)}"
        worst_label = f"Worst fit line: m = {round_sig(m_w, self.accuracy)}"

        # Plot lines
        self.ax.plot(endpoints, (m_b * endpoints) + c_b, color="black", linewidth=0.6, label=best_label)
        self.ax.plot(endpoints, (m_w * endpoints) + c_w, color="red", linewidth=0.6, label=worst_label)

    def show(self):
        if self.force_origin:
            self.__show_origin()
        
        self.__add_gridlines()

        self.__plot_points()
        self.__plot_lines()

        self.__add_text()

        plt.show()


def main():
    Graph([1, 0.9, 0.8, 0.7, 0.6, 0.5], [3.0, 2.5, 2.5, 2.3, 1.8, 1.5], y_err=0.3,
          title="Young's double slit data", x_label="Displacement / m", y_label="Fringe spacing / mm").show()


if __name__ == "__main__":
    main()
