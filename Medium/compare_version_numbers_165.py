#Accepted: 03.05.24, 35ms, 16.61 MB
def compareVersion(version1, version2):
    def stripLeadingZeros(version_list):
        corr_list = version_list
        for i in range(len(corr_list)):
            if len(corr_list[i]) > 1:
                corr_list[i] = corr_list[i].lstrip("0")
                if corr_list[i] == "":
                    corr_list[i] = "0"
        return [int(val) for val in corr_list if val]
    
    version1_curr = version1.split(".")
    version2_curr = version2.split(".")
    version1_curr = stripLeadingZeros(version1_curr)
    version2_curr = stripLeadingZeros(version2_curr)
    if len(version1_curr) != len(version2_curr):
        diff = abs(len(version1_curr) - len(version2_curr))

        for j in range(diff):
            min(version1_curr, version2_curr, key=len).append(0)
        print(diff)
    i = 0
    while i < len(version1_curr):
        if version1_curr[i] > version2_curr[i]:
            return 1
        elif version1_curr[i] < version2_curr[i]:
            return -1
        else:
            i+=1
    return 0

def main():
    print(compareVersion("1.00.1", "1.0.2"))

main()