import pandas as pd

def handler(event, context):
    d = {'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    return 'Done x1.1'
