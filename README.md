# Smart Parking Management System

## Project Overview

The Smart Parking Management System is a Python-based desktop application developed using Tkinter and Matplotlib. It provides a simple, user-friendly dashboard to manage parking slots and vehicle information.

The application allows users to park vehicles, remove vehicles, search for vehicle numbers, update vehicle information, and view parking statistics through a graphical chart. The interface uses a modern dashboard layout with parking-slot cards and status indicators.

## Objectives

- To develop a parking management application using Python.
- To understand classes, objects, lists, loops, conditions, and functions.
- To create a graphical user interface using Tkinter.
- To visualize parking statistics using Matplotlib.
- To simplify vehicle and parking-slot management.

## Technologies Used

- **Python:** Main programming language.
- **Tkinter:** Graphical user interface (GUI).
- **Matplotlib:** Graphical representation of parking statistics.

## Features

1. **Dashboard:** Displays total, occupied, and available parking slots.
2. **Park Vehicle:** Assigns a vehicle to an available slot.
3. **Remove Vehicle:** Removes a vehicle and makes its slot available.
4. **Search Vehicle:** Finds a vehicle and displays its parking slot.
5. **Update Vehicle:** Updates an existing vehicle number.
6. **Parking Slot Status:** Displays available slots in green and occupied slots in red.
7. **Parking Statistics:** Generates a bar chart showing occupied and available slots.
8. **Vehicle List:** Displays the vehicles currently parked.

## Python Concepts Used

- Classes and objects
- Variables and data types
- Lists
- Conditional statements (`if-else`)
- Loops (`for`)
- Functions and methods
- List operations
- Tkinter widgets and event handling
- Geometry managers: `pack()` and `grid()`
- Matplotlib bar charts

## Project Structure

```text
Smart-Parking-Management-System/
│
├── smart_parking_gui.py
└── README.md
```

## Installation and Setup

### Step 1: Install Python

Download and install Python from https://www.python.org/downloads/ if it is not already installed.

### Step 2: Install Matplotlib

Open the terminal in VS Code and execute:

```bash
python -m pip install matplotlib
```

Tkinter is generally included with standard Python installations.

### Step 3: Run the Project

Navigate to the folder containing the Python file and run:

```bash
python smart_parking_gui.py
```

The Smart Parking Management System dashboard will open.

## How to Use

1. Launch the application.
2. View the total number of parking slots on the dashboard.
3. Click **Park Vehicle** and enter the vehicle number.
4. Click **Remove Vehicle** to release an occupied slot.
5. Click **Search Vehicle** to locate a parked vehicle.
6. Click **Update Vehicle** to change a vehicle number.
7. Click **Parking Statistics** to view the bar chart.
8. Click **Dashboard** to refresh the dashboard and view the latest parking status.

## Expected Output

The application displays a dashboard containing parking-slot cards, vehicle information, and summary counts. Available slots appear in green, while occupied slots appear in red. The statistics option displays a bar chart comparing occupied and available slots.

## Learning Outcomes

- Learned to develop a GUI application using Python Tkinter.
- Applied classes, objects, lists, loops, conditions, and functions.
- Practiced using Tkinter geometry managers to arrange widgets.
- Learned to create and interpret bar charts using Matplotlib.

## Limitations

- The system supports a fixed capacity of 10 parking slots.
- Vehicle records are stored in memory and are lost when the application closes.
- The project does not use a database or online vehicle tracking.

## Future Enhancements

- Add permanent data storage.
- Allow the user to choose the total number of parking slots.
- Add vehicle entry and exit time tracking.
- Generate parking fee reports.

## Conclusion

The Smart Parking Management System demonstrates how Python programming concepts can be applied to a practical parking management problem. It combines a Tkinter graphical interface with Matplotlib data visualization to provide a simple and organized way to monitor parking availability and manage vehicles.
