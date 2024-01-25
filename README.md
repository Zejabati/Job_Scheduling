# Job Scheduling Project

This project solves the job scheduling problem based on various rules such as predecessor relationships, eligible resources, and priority considerations using Python and Object-Oriented Programming.

## Problem Description

The problem involves assigning jobs to resources while considering predecessor relationships, eligible resources for each job, and priorities. Each job has a duration, a set of eligible resources, and predecessor jobs. 

## Files

- `Job Scheduling.py`: Contains the main logic for solving the job scheduling problem.
- `Job.csv`: Input data file containing information about jobs, their durations, eligible resources, and predecessors.
- `README.md`: This file providing information about the project.

## Project Structure

- `Job Scheduling.py`: The main script that reads input data, schedules jobs, and generates a Gantt chart.
- `Job.csv`: CSV file containing job information.
- `str_to_tuple`: A utility function to convert string representations of tuples in the CSV to actual tuples.
- `Job` class: Represents a job with attributes such as job_id, duration, resource, predecessor, assigned status, start time, end time, and assigned resource.
- `Resource` class: Represents a resource with attributes such as r_id, start time, and end time. Includes a method to assign a job to the resource.

## Gantt Chart

The project generates a Gantt chart visualizing the schedule of jobs on resources over time. The chart is created using matplotlib.
The Gantt chart below illustrates the schedule of jobs on resources over time.
![Gaunt](https://github.com/Zejabati/Job_Scheduling/assets/65095428/d1699166-22d1-4a49-80fe-4150949a2058) 

