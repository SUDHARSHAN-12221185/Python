def  func1(parm1):
    def func2(parm2):
        return parm1.upper()+parm2.lower()
    return func2
y=func1('computer')
print(y('SCIENCE'))
