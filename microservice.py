import multiprocessing
import random
import sys

def request(conn, min, max): 
	""" 
	function to send range to other end of pipe 
	"""
	range = "{} {}".format(min, max)
	conn.send(range) 
	print("Sent the message: {}".format(range)) 
	conn.close() 

def generate(conn): 
	""" 
	function to print the random number based on
	the range received from other end of pipe 
	"""
	while 1: 
		msg = conn.recv()
		range = msg.split(' ')
		random_num = random.randrange(int(range[0]), int(range[1]))
		file = open('Z:/CS361/assignment_8/random_num.txt', 'w')
		file.write(str(random_num))
		file.close()
		print("Wrote random number {} to \'random_num.txt\'".format(random_num))
		break
		
def main():
	# messages to be sent 
	min = sys.argv[1]
	max = sys.argv[2]

	# creating a pipe 
	parent_conn, child_conn = multiprocessing.Pipe() 

	# creating new processes 
	p1 = multiprocessing.Process(target=request, args=(parent_conn,min,max)) 
	p2 = multiprocessing.Process(target=generate, args=(child_conn,))

	# running processes 
	p1.start() 
	p2.start() 

	# wait until processes finish 
	p1.join() 
	p2.join()

if __name__ == "__main__":
	main()