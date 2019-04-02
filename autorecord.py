import os
name = "forward"
for i in range(0,2):
	os.system("arecord -d 2 "+name +str(i)+".wav")