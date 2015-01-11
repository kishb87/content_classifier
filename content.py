# -*- coding: utf-8 -*-


import re, csv


class Open():

	def compile_content(self):
	
		# Vida content cards
		f = open('content_cards_v1.csv', 'rU')

		csv_f = csv.reader(f, dialect=csv.excel)

		contentData = {}
		numberList = []

		for row in csv_f:
			numberList.append(row[0])

		f.close()

		return contentData

class Classifier():

	def match(self):

		row_list = [[1711,"How to find a new fitness fitness fitness fitness gym that will work for you","<p>In general, I like fitness and new things.</p>","https://www.vida.com/content/how-to-find-a-gym-that-will-work-for-you","fitness","new","gym"],[1711,"How to find a gym that will work for you","<p>Finding a gym is a fun and an exciting part of your health journey. When looking for a gym consider what is important to you. There are many gyms out there from the bare bones gym to the full service athletic club. For example you may want access to a pool and jacuzzi, classes that are included in your membership, specific exercise equipment or child care services.</p>","https://www.vida.com/content/how-to-find-a-gym-that-will-work-for-you","General fitness","new","gym"]]	
	
		keywords_per_article = []
		for row in row_list:
			content = [row[1],row[2],row[3]]
			keywords = [row[4],row[5],row[6]]
			result_list = []
			for keyword in keywords:
				keyword_list = []
				for content_item in content:
					keywords_found = re.findall(keyword, content_item)
					keyword_number = len(keywords_found)
					keyword_list.append(keyword_number)
					keyword_total = sum(keyword_list)
				result_list.append(keyword_total)
			keywords_per_article.append(result_list)

		print keywords_per_article

		
#class Writer():



open_file = Open()
compile_content = open_file.compile_content()


classify_file = Classifier()
result = classify_file.match()
#print result

#print compile_content[0]['643'][1]



# Data output looks like: {'title':['content', 'link', [{'subsub': numlinks}]]}


# Begin CSV output code
#with open('sorted_content', 'wb') as csvfile:
#	fieldnames = ['number', 'title', 'content', 'permalink', 'keyword', 'number found']
#	writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect=csv.excel, delimiter='|')

#	writer.writeheader()
#	for key, value in result_list.items():
#		writer.writerow([key, value])

