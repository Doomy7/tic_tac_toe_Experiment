'''mapper.py'''
import pandas as pd
from hdfs import InsecureClient
def mapper():
    print("MAPPER READS...")
    web_hdfs_interface = InsecureClient('http://localhost:9870', user='')
    with web_hdfs_interface.read('/tic_tac_toe/ml-project/tic-tac-toe.data') as reader:
        data = pd.read_csv(reader)
    to_reduce = []
    for index, row in data.iterrows():
        #for every column except class
        for square in data.columns[:-1]:
            #instead of 1 or 0 we have W and L
            if row.loc[square] == 'x' and row.loc['Class'] == 'positive':
                print(square, 'W')
                to_reduce.append('%s\t%s'% (square, 'W'))
            elif row.loc[square] == 'x' and row.loc['Class'] == 'negative':
                print(square, 'L')
                to_reduce.append('%s\t%s'% (square, 'L'))
    to_reduce.sort()
    with open('x_mapped.csv', 'w') as csvfile:
        for line in to_reduce:
            csvfile.write(line+'\n')

mapper()