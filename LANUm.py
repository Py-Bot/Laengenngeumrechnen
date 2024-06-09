def mtod(m):
    return m / 1000

def ktom(km):
    return km * 1000

def ctomm(cm):
    return cm * 10

def mmtoc(mm):
    return mm / 10

def dtom(dm):
    return dm / 10

def mtod(m):
    return m * 10

def ctom(cm):
    return cm * 100

def main():
    length = float(input("Gib die Länge ein: "))
    unit = input("Gib die Einheit ein (m, km, cm, mm, dm): ")

    if unit == "m":
        result_km = mtod(length)
        result_cm = mtod(length) * 100
        result_mm = mtod(length) * 1000
        print(length, "m entsprechen", result_km, "km,", result_cm, "cm und", result_mm, "mm")
    elif unit == "km":
        result_m = ktom(length)
        result_cm = mtod(result_m) * 100
        result_mm = mtod(result_m) * 1000
        print(length, "km entsprechen", result_m, "m,", result_cm, "cm und", result_mm, "mm")
    elif unit == "cm":
        result_mm = ctomm(length)
        result_m = ctom(length)
        result_km = mtod(result_m)
        print(length, "cm entsprechen", result_km, "km,", result_m, "m und", result_mm, "mm")
    elif unit == "mm":
        result_cm = mmtoc(length)
        result_m = ctom(result_cm)
        result_km = mtod(result_m)
        print(length, "mm entsprechen", result_km, "km,", result_m, "m und", result_cm, "cm")
    elif unit == "dm":
        result_m = dtom(length)
        result_cm = mtod(result_m) * 100
        result_mm = mtod(result_m) * 1000
        print(length, "dm entsprechen", result_m, "m,", result_cm, "cm und", result_mm, "mm")
    else:
        print("Ungültige Einheit.")

if __name__ == "__main__":
    main()