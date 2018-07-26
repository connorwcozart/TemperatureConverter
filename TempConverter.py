ConverterType = input("If you would like to convert from C to F, enter 0. If you would like to convert from F to C, enter 1.")

def CelsiusConverter():
    CelsTemp = input("Enter the temperature that you would like converted to fahrenheit.")
    FinalFarTemp = (float(CelsTemp) * 1.8) + float(32)
    print(CelsTemp, "is equivalent to ", FinalFarTemp, " degrees in fahrenheit.")

def FahrenheitConverter():
    FarTemp = input("Enter the temperature that you would like converted to celsius")
    FinalCelsTemp = (float(FarTemp) - float(32)) * 0.5556
    print(FarTemp, "is equivalent to ", FinalCelsTemp, " degrees in celsius.")

if ConverterType == 0:
    CelsiusConverter()
else:
    FahrenheitConverter()