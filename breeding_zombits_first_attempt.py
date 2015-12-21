def answer(str_S):
  num_rabits = int(str_S)
  if num_rabits > 10**16:
    return None
  elif num_rabits < 3:
    return str_S
  memo = [1,1,2]
  last = 2
  instance = 3
  while last != num_rabits:
    if num_rabits < memo[-1] and num_rabits < memo[-2]:
      return None
    if instance % 2 == 0:
      last = memo[1] + memo[2] + instance/2
    else:
      last = memo[0] + memo[1] + 1
      memo.pop(0)
    memo.append(last)
    instance += 1
  if instance % 2 == 0:
    last = memo[1] + memo[2] + instance/2
    memo.append(last)
    instance +=1
    last = memo[0] + memo[1] + 1
    instance +=1
  else:
    last = memo[0] + memo[1] + 1
    instance +=1
    memo.append(last)
    last = memo[1] + memo[2] + instance/2
    instance +=1
    memo.pop(0)
  new_instance = instance
  # print last
  while last != num_rabits:
    if num_rabits < memo[-1] and num_rabits < memo[-2]:
      return str(instance-3)
    if new_instance % 2 == 0:
      last = memo[1] + memo[2] + new_instance/2
    else:
      last = memo[0] + memo[1] + 1
      memo.pop(0)
    memo.append(last)
    new_instance +=1

  # print memo
  return str(new_instance-1)

############### someone else's solution ##############

# r = {0: 1, 1: 1, 2: 2}  # Store R(n) values


# def R(count):
#     """Work backwards to compute R(n)."""
#     if count not in r:
#         n = count // 2
#         if count == 2 * n:
#             r[count] = R(n) + R(n + 1) + n
#         else:
#             r[count] = R(n - 1) + R(n) + 1
#     return r[count]


# def binary_search(space, zombits):
#     start, end = 0, zombits
#     while start <= end:
#         mid = (start + end) // 2
#         probe = R(space(mid))
#         if probe == zombits:
#             return mid
#         if probe < zombits:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return -1


# def answer(zombits):
#     zombits = int(zombits, 10)
#     bs_even = binary_search(lambda n: n * 2, zombits) * 2
#     bs_odd = binary_search(lambda n: n * 2 + 1, zombits) * 2 + 1
#     if bs_even < 0:
#         answer = None if bs_odd < 0 else bs_odd
#     elif bs_odd < 0:
#         answer = bs_even
#     else:
#         answer = max(bs_even, bs_odd)
#     return '{}'.format(answer)


# if __name__ == '__main__':
#     print answer(str(10**25))

for _ in xrange(10000):
  answer("133")
print answer("1")
print answer("7")
print answer("72") == "41"
print answer("100")
print answer("133")
print answer("1083")
print answer(str(10**25)) #== "22686405"
