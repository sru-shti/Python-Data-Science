s1={2,435,5467,45,65,446}
s2={34,3,43,5,45,446}
print(s1.union(s2))  # all of them
print(s1.intersection(s2))   # only common once
print(s1.difference(s2))        # exclude common from s1 & s2 and print all from s1
print(s2.difference(s1))            # exclude common from s1 & s2 and print all from s2