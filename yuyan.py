import time 
import fanfou

#987654321
consumer = {'key':'', 'secret':''}


# client = fanfou.XAuth(consumer, 'username', 'password')

client = fanfou.XAuth(consumer, '', '')
fanfou.bound(client);
resp = client.users.show()
resp = resp.json()



def getFilemsg(fromMsg):
	outMsg=''
	try:
		with open('story.txt',encoding='utf8') as fi:
			contents = fi.readlines()
		fi.close()
		fileLen = len(contents)
		content=fromMsg
	except Exception as e:
		print(e)

	pos = 0
	try:
		for line in contents:
			if content in line:
				break
			else:
				pos += 1
		
		if pos!=1 and pos!=fileLen:
			outMsg = contents[pos+2]
	except Exception as e:
		print(e)
	return outMsg

def sendMsg(lastMsg):
	sendMsg1 = ''
	outMsg = ''
	outMsg = getFilemsg(lastMsg)
	if len(outMsg)==0:
		print('send failed')
	else:
		sendMsg1={'status':outMsg}
		client.statuses.update(sendMsg1)


# #时间戳 'Thu Nov 02 15:20:38 +0000 2017'  '%a %b %d %H:%M:%S +0000 %Y'
create_time = resp['status']['created_at']
last_msg = resp['status']['text']
ti_stamp = time.strptime(create_time, '%a %b %d %H:%M:%S +0000 %Y')
t_now = time.localtime()
if t_now.tm_year > ti_stamp.tm_year:
	sendMsg(last_msg)
elif t_now.tm_mon > ti_stamp.tm_mon:
	sendMsg(last_msg)
elif t_now.tm_mday > ti_stamp.tm_mday:
	sendMsg(last_msg)
else:
	print('the same day')



exit()



#发送消息
# msg={'status':'my msg'}
# client.statuses.update(msg)

#删除消息
# get1=resp['status']['id']
# msg={'id':get1}
# client.statuses.destroy(msg)

#打开文件
	# try:
	# 	with open('story.txt',encoding='utf8') as fi:
	# 		contents = fi.readlines()
	# 	fi.close()
	# 	fileLen = len(contents)
	# 	content=fromMsg
	# except Exception as e:
	# 	print(e)

# #时间戳 'Thu Nov 02 15:20:38 +0000 2017'  '%a %b %d %H:%M:%S +0000 %Y'
# create_time = resp['status']['created_at']
# last_msg = resp['status']['text']
# ti_stamp = time.strptime(create_time, '%a %b %d %H:%M:%S +0000 %Y')
# t_now = time.localtime()
# if t_now.tm_year > ti_stamp.tm_year: