"""A tool to plot graphs for AQA A-level physics required practicals"""

import matplotlib.pyplot as plt
import numpy


class Graph:
	def __init__(self, x, y, x_err=None, y_err=None, title="Graph",
		         x_label="Independent variable", y_label="Dependent variable"):
		self.fig, self.ax = plt.subplots()
		self.x = x
		self.y = y
		self.x_err = x_err
		self.y_err = y_err
		self.title = title
		self.x_label = x_label
		self.y_label = y_label

	def __plot(self):
		# Add labels
		self.ax.set_title(self.title)
		self.ax.set_xlabel(self.x_label)
		self.ax.set_ylabel(self.y_label)

		# Force graph to include origin
		self.ax.set_xlim(left=0, right=max(self.x) * 1.1)
		self.ax.set_ylim(bottom=0, top=max(self.y) * 1.1)

		# Add data points
		self.ax.scatter(self.x, self.y, color="black", s=30, marker="x",
						linewidths=0.6)

		# Add error bars
		self.ax.errorbar(self.x, self.y, xerr=self.x_err, yerr=self.y_err,
						 color="black", linewidth=0.6, fmt="none",
						 capsize=4, capthick=0.6)

		self.ax.grid(which="minor", color="lightgray", linewidth=0.6)
		self.ax.grid(which="major", color="gray", linewidth=0.6)

		plt.minorticks_on()

	def __gradients(self):
		# Get coefficients of line of best fit
		(m, c), cov = numpy.polyfit(self.x, self.y, 1, cov=True)

		# Interpret uncertainties in coefficients
		(m_err, c_err) = numpy.sqrt(numpy.diag(cov))
		m_worst = m + m_err
		c_worst = c - c_err

		# Plot lines of best and worst fit
		line_x = numpy.append(0, self.x.copy())
		self.ax.plot(line_x, (m * line_x) + c, color="black", linewidth=0.6,
					 label=f"Best m = {round(m, 3)}")
		self.ax.plot(line_x, (m_worst * line_x) + c_worst, color="red",
					 linewidth=0.6, label=f"Worst m = {round(m_worst, 3)}")

		self.ax.legend()

	def show(self):
		self.__plot()
		self.__gradients()
		plt.show()


def main():
	Graph([1, 0.9, 0.8, 0.7, 0.6, 0.5], [3.0, 2.5, 2.5, 2.3, 1.8, 1.5],
		  y_err=0.3, title="Young's double slit data",
		  x_label="Displacement / m", y_label="Fringe spacing / mm").show()

if __name__ == "__main__":
	main()
