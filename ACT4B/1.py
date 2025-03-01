import pandas as pd

mydataset = {
'cars': ["Toyota", "Mitsubishi", "Honda"],
'ratings': [1, 3, 5]
}

myvar = pd.DataFrame(mydataset)
print(myvar)
print(myvar.to_string())