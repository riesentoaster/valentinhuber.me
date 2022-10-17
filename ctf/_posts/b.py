a = '{{2*3}}'
s = '''a{a}a'''.format(a=a)
print(s)