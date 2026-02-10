try:
    a = int(input("Enter value of a "))
    b = int(input("Enter value of b "))
    print(a/b)
except ZeroDivisionError:
    print("Denominator cannot be zero")
except Exception:
    print(":Error")
except ValueError:
    print("Enter only integer value")
except Exception as e:
    print ("Error:", e)

print(a+b)
print(a-b)
