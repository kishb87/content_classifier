import pandas as pd

df_xls = pd.read_excel('content_cards_v1.xls', index_col='Number', na_values='')

def convert_and_count(str1, str2, category_name):
	if type(str1) == float: 
		return 'float in str1: ' + str(str1)
	if type(str2) == float:
		return 'float in ' + category_name + ': ' + str(str2)
	try:
		str1_converted = str1.encode('ascii', 'ignore')
	except:
		print ('Error in str1: ' + str(str1))
		return -1
	try:
		str2_converted = str2.encode('ascii', 'ignore')
	except:
		print ('Error in str2: ' + str(str2))
		return -1
	return str.count(str1_converted, str2_converted)

df_xls['category1_count'] = df_xls.apply(lambda row:convert_and_count(row['Article Content'], row['Category 1'], 'Category 1'), axis=1)
df_xls['category2_count'] = df_xls.apply(lambda row:convert_and_count(row['Article Content'], row['Category 2'], 'Category 2'), axis=1)
df_xls['category3_count'] = df_xls.apply(lambda row:convert_and_count(row['Article Content'], row['Category 3'], 'Category 3'), axis=1)

df_xls.to_excel('counted_content.xls', 'Counted Content')