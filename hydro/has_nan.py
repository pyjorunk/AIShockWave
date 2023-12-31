import numpy as np
import os
import sys
import time

def has_nan(array):
    '''
    checks if given array has a NaN inside
    returns: True if given array has at least one NaN, False otherwise
    '''
    return np.isnan(array).any()


def main(batchn):
    directory = '/scratch/project_2003154/MachineLearning/FirstImages5TeV/'
    directory += batchn + '/'
    howmanyNaNs = 0
    file_list = os.listdir(directory)
    n_files = len(file_list)
    i = 0
    start = time.time()
    for filename in file_list:
        filepath = os.path.join(directory, filename)
        if not os.path.isfile(filepath): continue
        i += 1
        compressed = np.load(filepath, allow_pickle=False)
        flowdata = compressed['flow_data']
        if has_nan(flowdata):
            howmanyNaNs += 1
        #if(i%100 == 0):
           # sys.stdout.write("\r{0}".format((float(i)/n_files)*100))
           # sys.stdout.flush()
           # print('files containing NaNs: ', howmanyNaNs, ' /', i)
    #print('checked', i, ' / ', n_files)
    print('files containing NaNs: ', howmanyNaNs, ' /', i)
    end = time.time()
    #print(end-start)


if __name__ == '__main__':
    batchn = sys.argv[1]
    main(batchn)
