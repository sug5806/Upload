# 데이터를 읽어오는 delegate
# read, delegate, make_sum

def read_data(filename):
    f = open(filename, 'rt')
    line = f.readlines()
    return line
    

def delegate(filename):
    func_data = read_data(filename)
    make_sum(data) = yield from func_data # list

    print("sending data")
    



def make_sum(data):
    sum = 0
    print("sum data")
    for i in data:
        sum += i 
    
if __name__ == "__main__":
    li = ["data1.txt","data2.txt","data3.txt"]
    for filename in range(len(li)):
        g = delegate(filename)

