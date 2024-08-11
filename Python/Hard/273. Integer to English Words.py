class Solution:
  def numberToWords(self, num: int) -> str:
    value = self.convert(num)

    split_value = value.split()
    if len(split_value) == 1 or split_value[-1] != "Zero":
      return value

    split_value.pop()
    return " ".join(split_value)

  def convert(self, num: int) -> str:
    if (num < 20):
      return self.mappedNum(num)

    if (num < 100):
      return f"{self.mappedNum((num // 10) * 10)} {self.mappedNum(num % 10)}"

    for div in [1000000000, 1000000, 1000, 100]:
      if (num // div) > 0 :
        return f"{self.numberToWords(num // div)} {self.mappedNum(div)} {self.numberToWords(num % div)}"

  def mappedNum(self, num: int) -> str:
    mapped = {
      0: "Zero",
      1: "One",
      2: "Two",
      3: "Three",
      4: "Four",
      5: "Five",
      6: "Six",
      7: "Seven",
      8: "Eight",
      9: "Nine",
      10: "Ten",
      11: "Eleven",
      12: "Twelve",
      13: "Thirteen",
      14: "Fourteen",
      15: "Fifteen",
      16: "Sixteen",
      17: "Seventeen",
      18: "Eighteen",
      19: "Nineteen",
      20: "Twenty",
      30: "Thirty",
      40: "Forty",
      50: "Fifty",
      60: "Sixty",
      70: "Seventy",
      80: "Eighty",
      90: "Ninety",
      100: "Hundred",
      1000: "Thousand",
      1000000: "Million",
      1000000000: "Billion"
    }

    return mapped[num]
