check = (_ for _ in range(100))

# len(check) fails
# check[0] fails

print(check)
print(list(check))
print(list(check), "Exhaustive")

check = (_ for _ in range(100))


# another important note
def checking():
    for _ in check:
        print(_)
        break


checking()
checking()
