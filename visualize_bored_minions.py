def answer(rolls, blocks):
  games = []
  roll = 0
  position = 0

  winnables =0
  if 3** rolls > 12345:
    return
  for i in xrange(3**rolls):
    games.append(Game(rolls, blocks))
  for i in range(1, rolls+1):
    for j,game in enumerate(games):
      iterater = j / 3**(rolls-i)
      if iterater % 3 == 0:

        game.move("left")

      elif iterater %3 == 1:
        game.move("right")
      else:
        game.move("stay")

      if i == rolls and game.valid and game.token.position == blocks -1:
        winnables += 1
  return winnables %123454321



moves = ["left", "right", "stay"]
movements = {"left": -1, "right": 1, "stay": 0}



class Token:

  def __init__(self):
    self.position =  0

class Game:
  def __init__(self, rolls, blocks):
    self.rolls = rolls
    self.blocks = blocks -1
    self.token = Token()
    self.valid = True

  def move(self, direction):

    if self.token.position == self.blocks and direction != "stay":
      self.valid = False
    self.token.position += movements[direction]
    # # self.rolls -= 1
    if self.token.position < 1 and direction == "left":
      self.valid = False
    # else:
    #   self.token.position += movements[direction]
    #   return True
      # elif self.token.position == self.blocks and
    # if self.rolls == 0 and self.token.position == self.blocks:
    #   return True
print answer(3,2)
print answer(2,1)
# print answer(3,2)
print answer(5,4)
