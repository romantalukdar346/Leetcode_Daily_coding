def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i,j=0,0
    l1=len(nums1)
    l2=len(nums2)
    common=[]
    while l1 >i and l2 > j:
        if nums1[i]==nums2[j]:
            common.append(nums1[i])
            i+=1
            j+=1
        elif nums1[i]>nums2[j]:
            j+=1
        else:
            i+=1
    return common
    
    # 2nd
    # return list((Counter(nums1) & Counter(nums2)).elements())