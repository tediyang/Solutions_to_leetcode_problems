class Solution:
  def findComplement(self, num: int) -> int:
    binary = str(bin(num)[2:])
    reverse = ""
    for i in binary:
      if i == "0":
        reverse += "1"
      else:
        reverse += "0"

    return int(reverse, 2)
