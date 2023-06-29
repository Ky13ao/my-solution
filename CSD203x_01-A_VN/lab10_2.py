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
    """
    Dùng heap để theo dõi lần rãnh rỗi tiếp theo của từng worker
    Cải tiến việc giao việc bằng cách tối thiếu thời gian hoàn thành tổng quát
    Độ phức tạp thời gian của thuật toán này là O(j log w)
    So với thuật toán gốc thời gian là O(j*w)
    """
    import heapq
    self.assigned_workers = [None] * len(self.jobs)
    self.start_times = [None] * len(self.jobs)
    # khởi tạo tuple (số việc, số worker) list theo thứ tự tăng dần theo số worker
    next_free_time = [(0, i) for i in range(self.num_workers)]
    print(list(next_free_time))
    # đưa min-heap vừa tạo vào heapq
    heapq.heapify(next_free_time)
    print(list(next_free_time))

    # giảm O(jw) --> O(j)
    for i in range(len(self.jobs)):
      # công nhân được chọn để giao nhiệm vụ là công nhân có số nhiệm vụ ít nhất
      # hàm heappop sẽ làm điều đó
      next_worker = heapq.heappop(next_free_time)
      # công nhân làm việc i sẽ là công nhân vừa được chọn
      self.assigned_workers[i] = next_worker[1]
      # việc bắt đầu ở vị trí i sẽ là số việc người được chọn đang làm
      self.start_times[i] = next_worker[0]
      # thêm 1 node vào cây heap 
      # (số việc = số việc người được đang làm + số việc của công việc, số công nhân = số công nhân đó)
      heapq.heappush(next_free_time, (next_worker[0] + self.jobs[i], next_worker[1]))
      print(list(next_free_time))


  def solve(self):
    self.read_data()
    self.assign_jobs()
    self.write_response()

if __name__ == '__main__':
  job_queue = JobQueue()
  job_queue.solve()