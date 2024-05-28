import subprocess

def request_random_num(min, max):
    subprocess.run(["python", "Z:/CS361/assignment_8/microservice.py", str(min), str(max)])

def main():
    """ Main entry point of the app """
    
    request_random_num(1, 10)

    file = open('Z:/CS361/assignment_8/random_num.txt', 'r+')
    random_number = file.read()
    file.close

    print("Random number: {}".format(random_number))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()