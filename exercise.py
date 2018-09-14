temperatures = [10, -20, -289, 100]
myfile = open("test.txt","w")
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c* 9/5 + 32
        return f
for t in temperatures:
    print(c_to_f(t))
    myfile.write(Str(c_to_f)
myfile.close()
