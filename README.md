# revcode-backend
backend for RevCode project

RevCode API docs
GET user data
/userdata?uid=cidCuqVCQ5OKf26IAGjKRr8mLA82

POST new user
/adduser
{
	"name": "Wattanai s.",
	"uid": "test_uid"
}

GET file data
/loadfile?file_id=-LqbdD_0LnDR7QH7OeWy&uid=cidCuqVCQ5OKf26IAGjKRr8mLA82

GET new file
/newfile?uid=cidCuqVCQ5OKf26IAGjKRr8mLA82

POST saved file
/savefile
{
	"uid": "cidCuqVCQ5OKf26IAGjKRr8mLA82",
	"file_id": "-LqbdD_0LnDR7QH7OeWy",
	"code": "brabra", 
	"filename": "bra.py", 
	"extension": "py"
}


POST remove file
/remove file
{
	"uid": "cidCuqVCQ5OKf26IAGjKRr8mLA82",
	"file_id": "-LqbdD_0LnDR7QH7OeWy"
}
