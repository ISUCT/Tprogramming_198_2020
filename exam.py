class TemperatureConverter:
    def convertTemp(self, temperature, convertTO):
        if (convertTO == "F"):
            temperature = (temperature - 32) * (5/9)
        else:
             temperature = temperature * (9/5) + 32

        return temperature

if __name__ == "__main__":
    con = TemperatureConverter()
    res = con.convertTemp(7, 'C')
    print (f"7 * C -> {res} * F")
    res = con.convertTemp(43, 'C')
    print (f"43 * C -> {res} * F")
    res = con.convertTemp(64, 'F')
    print (res)
    res = con.convertTemp(300, 'F')
    print (res)
