"""
Your module description
"""
S={100,0,29,'jan',3.4}
print(type(S))
Fs=frozenset(S)
print(type(Fs))
S.add(29)
S.remove(100)
print(S)
print(Fs)