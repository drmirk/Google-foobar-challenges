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

for _ in xrange(10000):
  answer("133")
print answer("1")
print answer("7")
print answer("72") == "41"
print answer("100")
print answer("133")
print answer("1083")
print answer(str(10**25)) #== "22686405"
