import math

# https://aonecode.com/amazon-online-assessment-utilization-checks

def finalInstances(instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """


    # Average utilization < 25%: An action is instantiated to reduce the number of instances by half if the number of instances is greater than 1 (take the ceiling if the number is not an integer). If the number of instances is 1, take no action.
    # 25% <= Average utilization <= 60%: Take no action.
    # Average utilization > 60%: An action is instantiated to double the number of instances if the doubled value does not exceed 2* 10^8. If the number of instances exceeds this limit upon doubling, perform no action.
    # Given an array of integers that represent the average utilization at each second, determine the number of instances at the end of the time frame.

    maxi = 2*10**8

    i = 0
    while i < len(averageUtil):

        print(int(averageUtil[i]), i, instances)
        if int(averageUtil[i]) < 25 and instances > 1:
            instances = math.ceil(instances / 2)
            i += 11
            continue
        elif int(averageUtil[i]) > 65:
            if instances*2 <= maxi:
                instances = instances*2
                i += 11
                continue
        i += 1

    return int(instances)

# instances = 2
# averageUtil = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]

# instances=5
# averageUtil=['30', '5', '4', '8', '19', '89']

instances=1
averageUtil=['30', '15', '18', '18', '19', '89', '15', '18', '18', '19', '89', '15', '18', '18', '19', '89', '15', '18', '18', '19', '89', '15', '18', '18', '19', '89']

print(finalInstances(instances, averageUtil))