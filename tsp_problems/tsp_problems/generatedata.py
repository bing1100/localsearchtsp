
# Parses a file into a list
def parsefile(num_city, file_num):
    file_name = str(num_city) + "/instance_" + str(file_num) + ".txt"
    f = open(file_name, 'r')

    raw_data = f.read().split('\n')
    raw_data = [ data.split(' ') for data in raw_data[1:-1]]
    parsed = [[data[0], [int(data[1]), int(data[2])]] for data in raw_data]

    f.close()
    return parsed

# Parse the 36 city example
def parsefile_p36():
    file_name = "36/instance_1.txt"
    f = open(file_name, 'r')

    raw_data = f.read().split('\n')
    raw_data = [ data.split(' ') for data in raw_data[1:-1]]
    parsed = [[data[0], [int(data[1]), int(data[2])]] for data in raw_data]

    return parsed

def parsefile_opt():
    file_name = "tsp_opt_solution.txt"
    f = open(file_name, 'r')

    raw_data = f.read().split('\n')
    parsed = [ float(data.split(' ')[1]) for data in raw_data[1::2]]
    
    return parsed

if __name__ == '__main__':
    print(parsefile(14, 5))
    print(parsefile_p36())

    print(parsefile_opt())
    print(len(parsefile_opt()))
    


    