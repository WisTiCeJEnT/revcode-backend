# revcode-backend
backend for RevCode project

## RevCode API docs

* GET user data
 	* /userdata?uid=cidCuqVCQ5OKf26IAGjKRr8mLA82
	
* POST new user
	* /adduser
```json
{
	"name": "Wattanai s.",
	"uid": "test_uid"
}
```

* GET file data
	* /loadfile?file_id=-LqbdD_0LnDR7QH7OeWy&uid=cidCuqVCQ5OKf26IAGjKRr8mLA82

* POST new file
	* /newfile
```json
{
	"uid": "cidCuqVCQ5OKf26IAGjKRr8mLA82",
	"file_id": "-LqbdD_0LnDR7QH7OeWy",
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
	* /remove file
```json
{
	"uid": "cidCuqVCQ5OKf26IAGjKRr8mLA82",
	"file_id": "-LqbdD_0LnDR7QH7OeWy"
}
```
