def divide(self, dividend, divisor):
    is_positive= (dividend >0) == (divisor >0)

    dividend,divisor=abs(dividend),abs(divisor)

    inner_count=0
    count=0

    while dividend>=divisor:
        temp=divisor
        count+=inner_count
        dividend-=(inner_count*divisor)

        while dividend>=temp:
            
            inner_count=temp//divisor
            temp<<=1

    if not is_positive:
        count*=-1

    return  min(max(-2**31,count),2**31-1)