import usabilla as ub

if __name__ == '__main__':
	clientApi = ub.APIClient('CLIENT-API-KEY', 'CLIENT-SECRET-KEY')
	clientApi.setQueryParameters({'limit' : 1})
	buttons = clientApi.getButtons()
	print buttons