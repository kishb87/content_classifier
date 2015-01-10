# -*- coding: utf-8 -*-

#Need an array called keys to access dictionary

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

		# Title from Excel sheet column B becomes key and value containts content body and permalinks stored as strings in a list
		# for row in csv_f2:
		# 	contentData[row[0]] = [row[1], row[2], row[4]]

		# Take contentData and store it in list of dictionaries where each dict holds one title as key and contnt/permalink as value
		# for k, v in contentData.items():
		# 	data = {}
		# 	data[k] = v
		# 	contentList.append(data)

		f2.close()

		return contentData

class Classifier():

	def list_creator(self, content_data):

		keyword_list = []
		value_list = []

		#for key, value in content_data.iteritems():
			#keyword_list.append(key)
			#value_list.append(value)

		return keyword_list, value_list

	def match(self, keyword_list, article_list, title_list, number_list):

		#{title:[[content][link][{keyword:number_of_keywords_found}]]}

		#{title:[[content][link][results_for_article]]}

		result_list = []
		
		for article, link, title, number in map(article_list, link_list, title_list, number_list):
			results_for_article = []

			for keyword in keyword_list:
				keywords_found = re.findall(keyword, article)
				number_of_keywords_found = len(keywords_found)
				keyword_and_number_found = {keyword: number_of_keywords_found}
				results_for_article.append(keyword_and_number_found)

			result = [number, title, article, link, results_for_article]

			result_list.append(result)

		return result_list

#class Writer():



open_file = Open()
compile_content = open_file.compile_content()

#classify_file = Classifier()
#result = classify_file.list_creator(compile_content)
#print result

print compile_content[0]['643'][1]



# Data output looks like: {'title':['content', 'link', [{'subsub': numlinks}]]}


# Begin CSV output code
#with open('sorted_content', 'wb') as csvfile:
#	fieldnames = ['number', 'title', 'content', 'permalink', 'keyword', 'number found']
#	writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect=csv.excel, delimiter='|')

#	writer.writeheader()
#	for key, value in result_list.items():
#		writer.writerow([key, value])

