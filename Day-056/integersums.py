def add_it_up(n):
    try:
      result=sum(range(n+1))
    except TypeError:
        return 0
    return result

print(add_it_up(int(input())))
