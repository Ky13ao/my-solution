# python3

class JobQueue:
  def read_data(self):
    # self.num_workers, m = map(int, input().split())
    # self.jobs = list(map(int, input().split()))
    self.num_workers, m, self.jobs = 2, 5, [1, 2, 3, 4, 5] #test case 1
    # self.num_workers, m, self.jobs = 4, 20, [1 for _ in range(20)] #test case 2
    assert m == len(self.jobs)

  def write_response(self):
    for i in range(len(self.jobs)):
      print(self.assigned_workers[i], self.start_times[i]) 

  def assign_jobs0(self):
    # TODO: replace this code with a faster algorithm.
    self.assigned_workers = [None] * len(self.jobs)
    self.start_times = [None] * len(self.jobs)
    next_free_time = [0] * self.num_workers
    for i in range(len(self.jobs)):
      next_worker = 0
      for j in range(self.num_workers):
        if next_free_time[j] < next_free_time[next_worker]:
          next_worker = j
      self.assigned_workers[i] = next_worker
      self.start_times[i] = next_free_time[next_worker]
      next_free_time[next_worker] += self.jobs[i]

  def assign_jobs(self):
    # use heapq module throughout the operation
    import heapq
    self.assigned_workers = [None] * len(self.jobs)
    self.start_times = [None] * len(self.jobs)
    # update min-heap to store tuples (times, workers)
    next_free_time = [(0, i) for i in range(self.num_workers)]
    heapq.heapify(next_free_time)

    #reduce O(jw) to O(j)
    for i in range(len(self.jobs)):
      next_worker = heapq.heappop(next_free_time)
      self.assigned_workers[i] = next_worker[1]
      self.start_times[i] = next_worker[0]
      heapq.heappush(next_free_time, (next_worker[0] + self.jobs[i], next_worker[1]))


  def solve(self):
    self.read_data()
    self.assign_jobs()
    self.write_response()

if __name__ == '__main__':
  job_queue = JobQueue()
  job_queue.solve()