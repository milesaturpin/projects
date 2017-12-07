import math

prompts = {
	"\nEnter one of the following functions to map":
		{
		"square": (lambda lst: list(map((lambda x: x*x),list(lst)))),
		"cos": (lambda lst: list(map((lambda x: math.cos(x)),list(lst)))),
		"negate": (lambda lst: list(map((lambda x: -1*x),list(lst))))
		},
	"Make fun of Haley":
		{
		"insult": (lambda x: "Haley is LAME"),
		"slander": (lambda x: "Haley is a lizard from Mars")
		}
	}
# fn_keys = map(lambda fn: fn.keys(),fns)


def query(prompt,fns):
	print(prompt + ':')
	for fn in list(fns.keys()): 
		print('- ' + fn)
	usr_rule = input('\n>>> ')
	bad_input = True
	while bad_input == True:
		if usr_rule in fns:
			bad_input = False
			continue
		usr_rule = input('Please enter a valid rule!\n>>> ')

	print('\nEnter input:')
	params = input('\n>>> ')
	return fns[usr_rule](params)

def init():
	for prompt,fns in prompts.items():
		print(query(prompt,fns))
	
init()

