num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = [eval(num1) for num1 in input("Enter test numbers: ").split()]

average = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10) / 10
print("The mean is: ", average)

newNum1 = (num1 - average) ** 2
newNum2 = (num2 - average) ** 2
newNum3 = (num3 - average) ** 2
newNum4 = (num4 - average) ** 2
newNum5 = (num5 - average) ** 2
newNum6 = (num6 - average) ** 2
newNum7 = (num7 - average) ** 2
newNum8 = (num8 - average) ** 2
newNum9 = (num9 - average) ** 2
newNum10 = (num10 - average) ** 2

newAverage = (newNum1 + newNum2 + newNum3 + newNum4 + newNum5 + newNum6 + newNum7 + newNum8 + newNum9 + newNum10) / 10
standardDev = newAverage ** 0.5

print("The standard deviation is: ", standardDev)
