import pandas as pd

def lambda_handler(event, context):
    data = data = {"Name" : ["Manoj", "Anu", "Harish", "krish"],
                "Age" :  [23, 24, 22, 18]}
    df = pd.DataFrame(data=data)
    print(df)
    print("Done")