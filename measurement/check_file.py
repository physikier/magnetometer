def find_current_measurement_number():
    import glob
    import os
    import re
    cell_id = find_recent_cell_id()
    try:
        newest_folder = max(glob.iglob(os.path.join('N:\\data\\2016\\magnetometer\\cell{}\\remote'.format(cell_id), '*/')), key=os.path.getctime)
        regex = re.compile(r'\d+')
        regex.findall(newest_folder)
        nums=[int(x) for x in regex.findall(newest_folder)]
        recent_measure_num=nums[-1]
        measurement_number = recent_measure_num + 1
        print(newest_folder)
        print(nums)
        print(measurement_number, type(measurement_number))
        return measurement_number
    
    except ValueError:
        print('no existing measurement in directory: start now with measurement number = 0')
        return 0

def find_recent_cell_id():
    import glob
    import os
    import re

    try:
        newest_folder = max(glob.iglob(os.path.join('N:\\data\\2016\\magnetometer', '*/')), key=os.path.getctime)
        regex = re.compile(r'\d+')
        regex.findall(newest_folder)
        nums=[int(x) for x in regex.findall(newest_folder)]
        recent_cell_id=nums[-1]
        print(newest_folder)
        print(nums)
        print(recent_cell_id)
        return(recent_cell_id)
    except ValueError:
        print('no recent cell id found: set cell id = 0')
        return 0


mn=find_current_measurement_number()
print(mn)
# cid = find_recent_cell_id()
# print(cid)