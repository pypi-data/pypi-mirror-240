print('Internal test')

import pandas as pd
import re

from Validity import is_date_in_dataset



import pandas as pd

df = pd.DataFrame({'text_column': ['abcdefgh', '123456789', 'short', None, 'toolongtext']})

def limit_max_length(location, column_name, start_length, length):
    location['limit_max_length'] = location[column_name].str.slice(start_length, start_length + length) 
    return df 


print(limit_max_length(df,'text_column',0,5))