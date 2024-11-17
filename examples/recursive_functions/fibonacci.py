def fibo(num: int):
    if num == 0: return 0
    elif num == 1: return 1
    else:  return fibo(num-2) + fibo(num-1)