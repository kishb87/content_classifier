import csv

# Livestrong content categories
f1 = open('livestrong_content_structure.csv', 'rU')

csv_f1 = csv.reader(f1, dialect=csv.excel)

# Split out each level of content tags into individual variables
category = []
subCategory = []
subSubCategory = []

# Make sure no duplicate entries get appended to lists
for row in csv_f1:
	if row[0] not in category:
		category.append(row[0])
	else:
		pass
	
	if row[1] not in subCategory:
		subCategory.append(row[1])
	else:
		pass

	if row[2] not in subSubCategory:
		subSubCategory.append(row[2])
	else:
		pass

f1.close()


# Vida content cards
f2 = open('vida_content_cards_12_03_2014.csv', 'rU')

csv_f2 = csv.reader(f2, dialect=csv.excel)

contentData = {}
contentList = []

# Title from Excel sheet column B becomes key and value containts content body and permalinks stored as strings in a list
for row in csv_f2:
	contentData[row[1]] = [row[2],row[4]]

# Take contentData and store it in list of dictionaries where each dict holds one title as key and contnt/permalink as value
for k, v in contentData.items():
	data = {}
	data[k] = v
	contentList.append(data)

f2.close()


# Begin CSV output code
with open('sorted_content.csv', 'wb') as csvfile:
	writer = csv.DictWriter(csvfile, contentData.keys(), dialect=csv.excel)

	writer.writeheader()
	for key, value in contentData.items():
		writer.writerow([key, value])
