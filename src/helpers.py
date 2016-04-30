import numpy as np

def get_baseline(data):
	return np.median(data)


def find_closest(A, target):
    #A must be sorted
    #A=np.sort(A)
    #idx = A.searchsorted(target)
    #idx = np.clip(idx, 1, len(A)-1)
    #left = A[idx-1]
    #right = A[idx]
    #idx -= target - left < right - target
    #return idx
   	try:
   		return (np.abs(A-target).argmin())
   	except:
   		return None

