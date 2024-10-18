class Solution:
  def maximumSwap(self, num: int) -> int:
    num_str = str(num)
    temp = num_str

    max_value = max(temp)

    while max_value == temp[0]:
      # remove the first value
      temp = temp[1:]

      # when temp is empty return num since no swap can be done
      if not temp:
        return num

      # update max_value
      max_value = max(temp)

    first = temp[0]
    swap = num_str.index(first)
    max_index = num_str.rindex(max_value)  # get the index of the max value if it occurs more than once.

    num_list = list(num_str)
    num_list[swap], num_list[max_index] = max_value, first

    return int(''.join(num_list))
