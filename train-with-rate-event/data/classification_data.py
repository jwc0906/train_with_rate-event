import predictionio
import random
import xlrd

wb = xlrd.open_workbook("classification.xlsx")
ws = wb.sheet_by_index(0)

client = predictionio.EventClient(
  access_key="iEdtm1nxM2cieX08GHlQ9KBeJbVr3k3hRKyxPWqNZchnrGDizuxTUNG_Ix8esCMm",
  url="http://localhost:7070",
  threads=5,
  qsize=500
)


# def user
def ucreating(user_id):
    client.create_event(
        event="$set",
        entity_type="user",
        entity_id=user_id
    )

# def item
def icreating(item_id):
    client.create_event(
        event="$set",
        entity_type="item",
        entity_id=item_id
    )

# def a new rating
def rating(user, item, rate):
    client.create_event(
	event="rate",
	entity_type="user",
	entity_id=user,
	target_entity_type="item",
	target_entity_id=item,
	properties={"rating" : float(rate)}
	)


# create a new item
for i in range(0,53):
	icreating("o001_"+str(i))
for i in range(0,82):
	icreating("o100_"+str(i))
for i in range(0,22):
	icreating("o010_"+str(i))
for i in range(0,7):
	icreating("o110_"+str(i))
for i in range(0,1):
	icreating("o111_"+str(i))

for i in range(0,9):
	icreating("s001_"+str(i))
for i in range(0,97):
	icreating("s100_"+str(i))
for i in range(0,50):
	icreating("s010_"+str(i))
for i in range(0,20):
	icreating("s110_"+str(i))
for i in range(0,14):
	icreating("s111_"+str(i))

# create a new user
for i in range(0,500):
	ucreating("u"+str(i))

for i in range(0,100):
	taste=random.randint(1,500)
	sum=0
	for j in range(2, 245):
		sum=sum+ws.row_values(j)[10]
		if sum>=taste:
			taste_row=j
			print "u"+str(i)+" taste_row : "+ str(taste_row)
			break
	for k in range(0, 10):
		ritem=random.randint(0,189)
		if ritem<9:
			inum=ritem
			rating("u"+str(i), "s001_"+str(inum), ws.row_values(taste_row)[2])
		elif ritem<106:
			inum=ritem-9
			rating("u"+str(i), "s100_"+str(inum), ws.row_values(taste_row)[3])
		elif ritem<156:
			inum=ritem-106
			rating("u"+str(i), "s010_"+str(inum), ws.row_values(taste_row)[4])
		elif ritem<176:
			inum=ritem-156
			rating("u"+str(i), "s110_"+str(inum), ws.row_values(taste_row)[5])
		else:
			inum=ritem-176
			rating("u"+str(i), "s111_"+str(inum), ws.row_values(taste_row)[6])


for i in range(100,350):
	taste=random.randint(1,500)
	sum=0
	for j in range(2, 245):
		sum=sum+ws.row_values(j)[10]
		if sum>=taste:
			taste_row=j
			print "u"+str(i)+" taste_row : "+ str(taste_row)
			break
	for k in range(0, 30):
		ritem=random.randint(0,189)
		if ritem<9:
			inum=ritem
			rating("u"+str(i), "s001_"+str(inum), ws.row_values(taste_row)[2])
		elif ritem<106:
			inum=ritem-9
			rating("u"+str(i), "s100_"+str(inum), ws.row_values(taste_row)[3])
		elif ritem<156:
			inum=ritem-106
			rating("u"+str(i), "s010_"+str(inum), ws.row_values(taste_row)[4])
		elif ritem<176:
			inum=ritem-156
			rating("u"+str(i), "s110_"+str(inum), ws.row_values(taste_row)[5])
		else:
			inum=ritem-176
			rating("u"+str(i), "s111_"+str(inum), ws.row_values(taste_row)[6])

for i in range(350,450):
	taste=random.randint(1,500)
	sum=0
	for j in range(2, 245):
		sum=sum+ws.row_values(j)[10]
		if sum>=taste:
			taste_row=j
			print "u"+str(i)+" taste_row : "+ str(taste_row)
			break
	for k in range(0, 60):
		ritem=random.randint(0,189)
		if ritem<9:
			inum=ritem
			rating("u"+str(i), "s001_"+str(inum), ws.row_values(taste_row)[2])
		elif ritem<106:
			inum=ritem-9
			rating("u"+str(i), "s100_"+str(inum), ws.row_values(taste_row)[3])
		elif ritem<156:
			inum=ritem-106
			rating("u"+str(i), "s010_"+str(inum), ws.row_values(taste_row)[4])
		elif ritem<176:
			inum=ritem-156
			rating("u"+str(i), "s110_"+str(inum), ws.row_values(taste_row)[5])
		else:
			inum=ritem-176
			rating("u"+str(i), "s111_"+str(inum), ws.row_values(taste_row)[6])

for i in range(450,500):
	taste=random.randint(1,500)
	sum=0
	for j in range(2, 245):
		sum=sum+ws.row_values(j)[10]
		if sum>=taste:
			taste_row=j
			print "u"+str(i)+" taste_row : "+ str(taste_row)
			break
	for k in range(0, 100):
		ritem=random.randint(0,189)
		if ritem<9:
			inum=ritem
			rating("u"+str(i), "s001_"+str(inum), ws.row_values(taste_row)[2])
		elif ritem<106:
			inum=ritem-9
			rating("u"+str(i), "s100_"+str(inum), ws.row_values(taste_row)[3])
		elif ritem<156:
			inum=ritem-106
			rating("u"+str(i), "s010_"+str(inum), ws.row_values(taste_row)[4])
		elif ritem<176:
			inum=ritem-156
			rating("u"+str(i), "s110_"+str(inum), ws.row_values(taste_row)[5])
		else:
			inum=ritem-176
			rating("u"+str(i), "s111_"+str(inum), ws.row_values(taste_row)[6])


