def maxArea(self, height):
    left,right=0,len(height)-1
    max_area=0

    while left < right:

        l= min(height[left],height[right])
        w=right -left
        max_area=max(max_area,(l*w))

        if height[left] > height[right]:
            right-=1
        else:
            left+=1

    return max_area 