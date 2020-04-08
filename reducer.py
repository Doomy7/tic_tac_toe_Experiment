'''reducer.py'''
from hdfs import InsecureClient

def reducer():
    web_hdfs_interface = InsecureClient('http://localhost:9870', user='')
    with web_hdfs_interface.read('/tic_tac_toe/ml-project/x_mapped.csv') as reader:
        to_reduce = open('x_mapped.csv', newline='\n')
    currentSquare = None
    currendResult = None
    reduced = {}
    print('REDUSING...')
    for line in to_reduce:
        #split the tuple
        square, result= line.strip().split('\t')
        #if dict key does not exist init
        if not reduced.get(square):  reduced[square] = {'W': 0, 'L': 0}
        #if square change
        if currentSquare != square:
        #if not first loop print reduced
            if currentSquare is not None:
                print(currentSquare, reduced.get(currentSquare), 'W/L Ratio',
                        float(reduced.get(currentSquare)['W']) / float(reduced.get(currentSquare)['L']))
            #change cur square
            currentSquare = square
            #if result also changed
            if currendResult != result:
                #change result
                currendResult = result
                reduced.get(square)[result] += 1
            else:
                reduced.get(square)[result] += 1
        else:
            if currendResult != result:
                currendResult = result
                reduced.get(square)[result] += 1
            else:
                reduced.get(square)[result] += 1
    #print last
    print(currentSquare, reduced.get(currentSquare), 'W/L Ratio',
            float(reduced.get(currentSquare)['W']) / float(reduced.get(currentSquare)['L']))

reducer()