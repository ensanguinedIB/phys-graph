"""A tool to plot graphs for AQA A-level physics required practicals."""

import matplotlib.pyplot as plt
import numpy as np


class Graph:
    """A class for easily creating and customising graphs using matplotlib."""
    def __init__(self, x, y, x_err=None, y_err=None,
                 title="Graph", x_label="Independent variable", y_label="Dependent variable"):
        """
        Create a new Graph object given ordered x and y data.

        Positional arguments:
        
        x -- the independent variable.  x can be a list, a numpy ndarray, or any similar data type
            capable of being interpreted by matplotlib.
        
        y -- the dependent variable.  Data types as above.

        Keyword arguments:

        x_err -- the uncertainty in x, allowing for horizontal error bars to be plotted.
            This type can be a list-like object, the same length as x,
            meaning individual uncertainties will be displayed, or a single number,
            in which case the uncertainties will be plotted uniformly.

        y_err -- the uncertainty in y, allowing for vertical error bars to be plotted.  Data types as above.
        
        title -- the title to be displayed at the top of the plot.
        
        x_label -- the label on the horizontal axis.
        
        y_label -- the label on the vertical axis.
        """
        self.x = x
        self.y = y
        self.x_err = x_err
        self.y_err = y_err

        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def plot(self):
        """
        Draw graph using matplotlib.

        - Plots data points as a scatter graph.
        - Draws lines of best and worst fit.
        - Adds error bars to show uncertainties, if provided.
        """
        # Get graph from matplotlib
        fig, ax = plt.subplots()
        
        # Add labels
        ax.set_title(self.title)
        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)

        # Force graph to include origin
        ax.set_xlim(left=0, right=max(self.x) * 1.2)
        ax.set_ylim(bottom=0, top=max(self.y) * 1.2)

        # Add data points
        ax.scatter(self.x, self.y, color="black", s=30, marker="x", linewidths=0.6)

        # Add error bars
        ax.errorbar(self.x, self.y, xerr=self.x_err, yerr=self.y_err,
                    color="black", linewidth=0.6, fmt="none", capsize=4, capthick=0.6)

        # Adjust gridlines
        ax.grid(which="minor", color="lightgray", linewidth=0.6)
        ax.grid(which="major", color="gray", linewidth=0.6)

        plt.minorticks_on()

        # Get coefficients of line of best fit
        (m, c), cov = np.polyfit(self.x, self.y, 1, cov=True)

        # Interpret uncertainties in coefficients
        (m_err, c_err) = np.sqrt(np.diag(cov))
        m_worst = m + m_err
        c_worst = c - c_err

        # Plot lines of best and worst fit
        line_x = np.append(0, self.x.copy())
        ax.plot(line_x, (m * line_x) + c, color="black", linewidth=0.6, label=f"Best m = {round(m, 3)}")
        ax.plot(line_x, (m_worst * line_x) + c_worst,
                color="red", linewidth=0.6, label=f"Worst m = {round(m_worst, 3)}")

        # Add legend
        ax.legend()

        plt.show()


def main():
    Graph([1, 0.9, 0.8, 0.7, 0.6, 0.5], [3.0, 2.5, 2.5, 2.3, 1.8, 1.5], y_err=0.3,
          title="Young's double slit data", x_label="Displacement / m", y_label="Fringe spacing / mm").plot()


if __name__ == "__main__":
    main()
