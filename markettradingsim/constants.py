BASE_URL = 'http://api.marketstack.com/v1'

TEXTONLY = {
	"REGEX": "^[A-Za-z]*$",
	"ERROR": "Error! Only text can be entered!"
}

MENU_CONSTANTS = {
	"WELCOME": "Please enter select action (enter 'help' for options): ",
	"INVALID": "Invalid action entered. Type 'help' to see available actions.",
	"OPTIONS": [
		{
			"key":"help",
			"message":"Show available actions"
		},
		{
			"key":"add-ticker",
			"message":"Collect data on a company"
		},
		{
			"key":"exchanges",
			"message":"Print list of available exchanges"
		},
		{
			"key":"close",
			"message":"Close program"
		}
	],
	"FIELDS":[
		"Stock Code",
		"Exchange"
	]
}