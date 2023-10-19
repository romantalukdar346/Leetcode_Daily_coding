def summaryRanges(nums):
    if len(nums)==0:
        return []
    range_arr=[]
    start,end=nums[0],nums[0]
    for num in nums[1:]:
        if num==end+1:
            end=num
        else:
            if start==end:
                range_arr.append(f"{start}->{end}" if start!=end else str(start))
            else:
                range_arr.append(str(start)+"->"+str(end))
            start,end=num,num

    range_arr.append(f"{start}->{end}" if start!=end else str(start))
    return range_arr


nums=list(map(int,input().split(",")))
print(summaryRanges(nums))