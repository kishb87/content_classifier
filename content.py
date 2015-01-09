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



data = ["""<p>Finding a gym is a fun and an exciting part of your health journey. When looking for a gym consider what is important to you. There are many gyms out there from the bare bones gym to the full service athletic club. For example you may want access to a pool and jacuzzi, classes that are included in your membership, specific exercise equipment or child care services. </p>

<p>Each gym will vary in quality, amenities, membership benefits and customer service.  Make a list of what is important to you and go visit some local gyms. Many gyms will offer a tour or even a guest pass to try out the facility.  </p>

<p>Here are some other things to take into consideration: 
How clean is the gym? Do they provide cleaning spray for members to clean equipment after use?
Consider membership cost in relationship to amenities. Do you have to pay extra for classes? Will someone show you how to use the equipment? Do they offer towels?  
Is the staff friendly? Are the members social? 
Look around at the gym equipment.  Does it look new and modern or does it look like something from the1930’s?
Ask to see the locker rooms to make sure they are well kept and have everything you need. Do you need a shower for working before work? Do they have towels, shampoo and soap? 
Visit the gym at the time you would be using the facility. How crowded is it? Does it look like the classes fill up quickly? You want to make sure you don’t have to wait in line to use equipment. On the flip side if the gym is empty, has poor customer service, has low class attendance and serves alcohol, that might be a sign! </p>"""],["""<p>Sticking with a routine gets easier and easier as you keep doing it and will become a habit just like brushing your teeth! Be patient! It can take 4-6 weeks before you start to see or feel results, it is worth it! Consistency is key!  Just like practicing any skill, it yields the greatest results!  It is wise to start with something manageable so you don’t feel overwhelmed. When you feel ready, you can build on your routine. 
So how do you start a routine? 
Start with 2 days a week and exercise for 15, 20 or 30 minutes. 
On other the days add some mini sessions or non-structured physical activity to keep your mind, body and spirit in exercise mode. For example take a 10 minute walk during your lunch break or do an activity you enjoy such as gardening. 
After 4 weeks of sticking to this routine add another day of 30 to 60 minutes of exercise. 
At 6 weeks assess your progress. Do you feel stronger? Do you feel like you are overdoing it? Do you feel like you can do more or is that thought overwhelming?  </p>

<p>If you feel energized and you are recovering quickly from your workouts you can add another day or increase the time of your workout. The key is not to burn out and give up. If you are comfortable with your routine keep it going a only add more when you truly feel ready. 
Another great way to add more physical activity is to add something fun you can do with your friends or family. Before you know it, you will feel strong and fit ready to take on any new activity you choose to! </p>"""]


open_file = Open()
source = open_file.compile_category()
content = open_file.compile_content()

print content

#print source[1]

#feed = ''.join(data[0])

#result1 = re.findall(r'is', feed)
#print len(result1)
#result2 = re.findall(r'are', data1[1])
#print len(result1)
#print result2

#interate(data1)
#interate(data2)