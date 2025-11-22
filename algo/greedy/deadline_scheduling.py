"""
P: Given assignments with deadlines and the amount of time required for their completion,
   schedule them to minimize the maximum lateness.
Sol: Prioritize the assignment with the earliest deadline.
"""

class Assignment:
    def __init__(self, id, deadline, execution_time):
        self.id = id
        self.deadline = deadline
        self.execution_time = execution_time
    
    def __str__(self):
        unit = "time unit" if self.execution_time == 1 else "time units"
        return "Assignment %d (%d %s) with deadline at t=%d" % (self.id, self.execution_time, unit, self.deadline)

class Scheduler:
    def __init__(self, assignments):
        self.sorted_assignments = self.sort(assignments)
    
    def sort(self, assignments):
        # sort assignments: earliest-deadline first
        return sorted(assignments, key = lambda a: a.deadline)
    
    def print_schedule(self):
        t = 0
        max_lateness = 0
        for a in self.sorted_assignments:
            end_assignment = t+a.execution_time
            delay = max(0, end_assignment - a.deadline)
            max_lateness = max(max_lateness, delay)
            print("Start assignment %d at t=%d. Completed at t=%d (delay=%d)" % (a.id, t, end_assignment, delay))
            t = end_assignment
        print("Maximum lateness: %d" % max_lateness)

if __name__ == "__main__":
    assignments = [
        Assignment(0, 2, 4),
        Assignment(1, 1, 2),
        Assignment(2, 3, 1),
    ]
    
    scheduler = Scheduler(assignments)
    scheduler.print_schedule()
