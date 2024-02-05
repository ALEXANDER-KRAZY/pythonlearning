def outerFunc():
    outerFunction = 10
    def innerFunc():
            innerFunction = 20
            print("Outer Function is - ", outerFunction)
            print("Inner Function is - ", innerFunction)
    innerFunc()
    print("Outer Function is - ", outerFunction)
    print("Inner Function is - ", innerFunction)
outerFunc()