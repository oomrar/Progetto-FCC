
def square_root_bisection(num, toll = 0.01, max_iterations=100):
    if num < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if not num or num == 1:
        print(f"The square root of {num} is {num}")
        return num
    
    low = 0
    high = max(1, num)
    
    
    for _ in range(max_iterations):
        mid = (low + high)/2
        square = mid * mid
        
        if abs(high-low) <= toll:
            print(f"The square root of {num} is approximately {mid}")
            return mid

        if square > num:
            high = mid
        else:
            low = mid
        
    print(f"Failed to converge within {max_iterations} iterations")
    return None

    