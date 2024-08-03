import threading
import time

def write_to_file(filename, data):
	with open(filename, 'w') as f:
		f.write(data)
		time.sleep(1) # Simulate a time-consuming operation

def process_data(data_chunks):
	threads = []
	for i, chunk in enumerate(data_chunks):
		filename = f"output_{i}.txt"
		thread= threading.Thread(target=write_to_file, args=(filename, chunk))
		threads.append (thread)
		thread.start( )
	for thread in threads:
		thread.join()

data_chunks = ["This is chunk 1", "Nore data in chunk 2", "Final chunk 3"]
process_data(data_chunks)