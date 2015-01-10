# -*- coding: utf-8 -*-

import re, csv


class Open():
	def compile_category(self):
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

		return category, subCategory, subSubCategory

	def compile_content(self):
		#Vida content cards
		f2 = open('vida_content_cards_12_03_2014.csv', 'rU')

		csv_f2 = csv.reader(f2, dialect=csv.excel)

		contentData = {}

		# Title from Excel sheet column B becomes key and value containts content body and permalinks stored as strings in a list
		for row in csv_f2:
			contentData[row[1]] = [row[2],row[4]]

		f2.close()

		return contentData

class Classifier():
	def list_classifer(self,content_data, sub_sub_category):
		pass

	def match(self, keyword_list, article_list,title_list, number_list):

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

			result = {number:[[title],[article],[link],[results_for_article]]}

			result_list.append(result)

		return result_list


open_file = Open()
compile_content = open_file.compile_content()

print compile_content




