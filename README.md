# revcode-backend
backend for RevCode project
<br>
    <b>RevCode</b>   คือสิ่งที่จะมาปฏิวัติวิธีการเขียนโปรแกรมของทุกคนตลอดไป เพราะเราจะเปลี่ยนอิริยาบถของคุณให้เป็นสุดยอดโค้ด นั่นหมายความว่า ไม่ว่าคุณจะทำอะไรอยู่ กินข้าว เดินทางไปทำงาน หรือแม้แต่กำลังละเมอ คุณก็สามารถโค้ดด้วยคำพูดของคุณได้

#### โครงงานนี้เป้นส่วนหนึ่งของรายวิชา Software Engineering (01204341) ภาคต้น ปีการศึกษา 2562 
## Department of Computer Engineering - Kasetsart University

### Our Team
ลำดับที่ | ชื่อ-นามสกุล |  รหัสนิสิต 
:---:|---|:------:
1|นาย วรรธนัย สาธุพันธ์|6010500117
2|นาย ธันยา ตันศรีประภาศิริ|6010500389
3|นาย อัฐพงศ์ สมบูรณ์วรากร|6010500401
4|นาย ธนากร ปรางค์ศรีอรุณ|6010502578
5|นาย ฌานณโชตน์ บุญเขียว|6010504694

## RevCode API docs

* GET user data
 	* /userdata?uid=cidCuqVCQ5OKf26IAGjKRr8mLA82
	
* POST new user
	* /adduser
```json
{
	"name": "Wattanai s.",
	"uid": "test_uid",
	"email": "testemail@mailserver.com"
}
```

* GET file data
	* /loadfile?file_id=-LqbdD_0LnDR7QH7OeWy&uid=cidCuqVCQ5OKf26IAGjKRr8mLA82

* POST new file
	* /newfile
```json
{
	"uid": "cidCuqVCQ5OKf26IAGjKRr8mLA82",
	"filename": "bra.py", 
	"extension": "py"
}
```

* POST saved file
	* /savefile
```json
{
	"uid": "cidCuqVCQ5OKf26IAGjKRr8mLA82",
	"file_id": "-LqbdD_0LnDR7QH7OeWy",
	"code": "brabra", 
	"filename": "bra.py", 
	"extension": "py"
}
```

* POST remove file
	* /removefile
```json
{
	"uid": "cidCuqVCQ5OKf26IAGjKRr8mLA82",
	"file_id": "-LqbdD_0LnDR7QH7OeWy"
}
```

* POST remove user
	* /removeuser
```json
{
	"uid": "cidCuqVCQ5OKf26IAGjKRr8mLA82",
}
```
