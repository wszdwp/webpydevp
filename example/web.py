import web
#render = web.templates.render('templates/')
#import view, config
#from view import render

urls = (
    '/', 'index'
)

class index:
    def GET(self):
    	#name = 'Bob'
    	return "Hello world"
        #return render.index(name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    #app.internalerror = web.debugerror
    app.run()