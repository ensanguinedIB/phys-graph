# Physics Graph Plotter
A tool for plotting graphs without the need to open Excel

## Features
Uses matplotlib to plot points and lines of best and worst fit.
Includes major and minor gridlines and error bars.

## Requirements
A Python runtime, available at [python.org](https://www.python.org/).
numpy and matplotlib modules.  See how to install modules using pip [here](https://packaging.python.org/en/latest/tutorials/installing-packages/).

## Usage
Edit the Graph() constructor in the main() method and run by double clicking the file or running it from the command line.
There is some example data provided.  See the init method for optional constructor arguments.

## Planned improvements
- A command line interface to allow users to input data without editing the source code.
- Update algorithm for calculating line of worst fit, at the moment the uncertainty is returned from numpy.
- Maybe package this for easy importing.
