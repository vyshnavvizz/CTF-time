# this code contains the code to decode a list of base64 encrypted files and converting that decoded
# usernames into md5 hashes for checking php juggling
# so use after editing it in your own ways

#required headers
import base64
import md5
#spliting the lines
lines = file("users.dat").read().strip().split("\n")
line = [i.split(",")for i in lines]
#base64 decoding
usernames = [(base64.decodestring(i[0]), base64.decodestring(i[1])) for i in line]
print usernames
#md5 encoding
for i in usernames:
	hash = md5.md5(i[0]).hexdigest()
	print hash,i[0],
	#compairing for php juggling parts
	if hash.startswith("0e") :
		print "startwith 0e",i
	else :
		print ""