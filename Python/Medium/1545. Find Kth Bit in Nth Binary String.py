class Solution:
  def __init__(self):
    self.sn = ["0", "011", "0111001", "011100110110001"]

  def findKthBit(self, n: int, k: int) -> str:
    return self.binary_string(n)[k - 1]

  def binary_string(self, value):
    if value < 5:
        return self.sn[value - 1]

    s_value = self.binary_string(value - 1)

    return s_value + "1" + self.reverse(self.invert(s_value))

  def invert(self, value):
    rev = ""
    for i in value:
        if i == "0":
            rev += "1"
        else:
            rev += "0"
    return rev

  def reverse(self, value):
    return value[::-1]
