import pandas as pd

data = {
    "name": ["oi", "tchau", "cu"],
    "idade": [10,12,15]
}

df = pd.DataFrame(data)
for i in df['name']:
    print(i)