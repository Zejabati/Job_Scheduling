# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 21:59:59 2024

@author: zahra
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time                


def str_to_tuple(value):
    if isinstance(value, str):
        return tuple(map(int, value.split(',')))
    else:
        return value


class Job:
    def __init__ (self,job_id , duration, resource, predecessor,assigned) :
        self.job_id = job_id
        self.duration = duration
        self.resource = str_to_tuple(resource)
        self.predecessor = str_to_tuple(predecessor)
        self.assigned = assigned
        self.s = None #starttime
        self.e = None #endtime
        self.assigned_resource = None

class Resource:
    def __init__ (self,r_id, starttime=0, endtime=0):
        self.r_id = r_id
        self.starttime = starttime
        self.endtime = endtime   

    def assign_job(self, job, max_endtime_pre):
        self.starttime = max(self.endtime, max_endtime_pre)
        self.endtime = self.starttime + job.duration   
        

def check_predecessor(jobs, job_id):
    selected_object = next((obj for obj in jobs if obj.job_id == job_id), None)
    P = selected_object.predecessor
    #print('P', P)

    if P == 0:
        return 1, 0

    assigned_statuses = [next((obj.assigned for obj in jobs if obj.job_id == i), None) for i in P]
    check = all(assigned_statuses)

    if check:
        max_endtime_pre = max(obj.e for obj in jobs if obj.job_id in P)
        return check, max_endtime_pre

    return 0


def plot_gantt_chart(sorted_jobs):
    fig, ax = plt.subplots(figsize=(10, 6))


    resources = sorted(set(job.assigned_resource for job in sorted_jobs),reverse=True)
    resource_mapping = {resource: i for i, resource in enumerate(resources)}

    for job in sorted_jobs:
        if job.s is not None and job.e is not None and job.assigned_resource is not None:
            ax.barh(y=resource_mapping[job.assigned_resource], width=job.e - job.s, left=job.s, height=0.5, align='center', label=f'Job {job.job_id}')
            ax.text(job.s + 0.5 * (job.e - job.s), resource_mapping[job.assigned_resource], f'Job {job.job_id}', ha='center', va='center', color='black',fontsize=10)

    ax.set_xlabel('Time')
    ax.set_xticks(np.arange(0, max(job.e for job in sorted_jobs) + 1, step=1))  # Set x-axis ticks every 1 unit
    ax.set_yticks(np.arange(len(resources)))
    ax.set_yticklabels(resources)
    ax.set_title('Gantt Chart')
    ax.grid(True)

    plt.show()

#%%
             
def main():
    data = pd.read_csv("C:/Users/zahra/Desktop/Scheduling/Job.csv")
    data['predecessor'] = data['predecessor'].fillna(0)

    #Create Jobs and Resources
    n = 9
    r = 2
    List_jobs= n*[0]
    List_R = [Resource(i + 1) for i in range(r)]

    for i in range(n):
        List_jobs[i]= Job(i+1,data['duration'][i],data['resourse'][i],data['predecessor'][i],0)
     
     
    sorted_jobs = sorted(List_jobs, key=lambda x: x.job_id)
    remained=sorted_jobs.copy()


    
    while len(remained)>0:
        for i in range(len(remained)):
            #Check Predecessor
            result = check_predecessor(sorted_jobs, remained[i].job_id)
            if isinstance(result, tuple):
                check, max_endtime_pre = result
                
                #Choose Resource
                resource = None
                if remained[i].resource == (1,):
                    resource = List_R[0]
                elif remained[i].resource == (2,):
                    resource = List_R[1]
                elif remained[i].resource == (1, 2):
                    # Choose the resource with the earliest endtime
                    resource = min(List_R, key=lambda r: (max(r.endtime,max_endtime_pre), r.r_id))
                
                #assign job to chosen resource
                index = remained[i].job_id
                resource.assign_job(sorted_jobs[index-1], max_endtime_pre)
                sorted_jobs[index-1].assigned = 1
                sorted_jobs[index-1].s = resource.starttime
                sorted_jobs[index-1].e = resource.endtime
                sorted_jobs[index-1].assigned_resource = resource.r_id
                

        remained = list(filter(lambda obj: obj.assigned == 0, sorted_jobs))   

    plot_gantt_chart(sorted_jobs)
                          
             
if __name__ == "__main__":
    s=time.time()
    main()
    duration = time.time()-s            
    #print(duration)            
    
    
    
    
    
    



          
    
    