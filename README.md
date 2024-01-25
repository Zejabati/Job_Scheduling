# Job Scheduling Project

This project solves the job scheduling problem based on rules such as predecessor relationships, eligible resources, and priority considerations using Python and Object-Oriented Programming.

## Problem Description

The problem involves assigning jobs to resources while considering predecessor relationships, eligible resources for each job, and priorities. Each job has a duration, a set of eligible resources, and predecessor jobs. 
The project generates a Gantt chart visualizing the schedule of jobs on resources over time. The chart is created using matplotlib.

## Files

- `main.py`: Contains the main logic for solving the job scheduling problem.
- `Job.csv`: Input data file containing information about jobs, their durations, eligible resources, and predecessors.
- `README.md`: This file providing information about the project.

## Project Structure

- `main.py`: The main script that reads input data, schedules jobs, and generates a Gantt chart.
- `Job.csv`: CSV file containing job information.
- `Job` class: Represents a job with attributes such as job_id, duration, resource, predecessor, assigned status, start time, end time, and assigned resource.
- `Resource` class: Represents a resource with attributes such as r_id, start time, and end time. Includes a method to assign a job to the resource.
- `str_to_tuple`: A utility function to convert string representations of tuples in the CSV to actual tuples.
- `check_predecessor`: Verifies if all predecessors of a given job are assigned and returns a tuple indicating the check result and the maximum end time among the predecessors.


## Example Dataset

Consider the following example dataset representing jobs with their respective attributes:

<div align="center">

| Id | Duration | Resource | Predecessor |
|:-:|:--------:|:--------:|:-----------:|
| 1  | 5        | 1,2      |             |
| 2  | 4        | 1,2      | 1           |
| 3  | 3        | 1        | 2           |
| 4  | 2        | 2        |             |
| 5  | 2        | 2        | 2           |
| 6  | 3        | 1,2      | 3,5         |
| 7  | 2        | 2        | 6,9         |
| 8  | 3        | 1        | 4           |
| 9  | 5        | 1,2      | 5           |

</div>


## Predecessor Relations Graph

The graph below illustrates the predecessor relationships among the jobs:

<div align="center">
<img width="400" alt="Graph" src="https://github.com/Zejabati/Job_Scheduling/assets/65095428/34542f7a-90cf-4cbb-a9c8-addf9254bc1c">
</div>

## Solution Visualization using Gantt chart

The Gantt chart below illustrates the schedule of jobs on resources over time.
<div align="center">
<img width="500" alt="Gaunt" src="https://github.com/Zejabati/Job_Scheduling/assets/65095428/e7678b89-5f3f-4a0f-a670-547a811325f2">

</div>
