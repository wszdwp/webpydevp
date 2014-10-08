"""Postboard using webpy"""

import web

#Url mappings

urls = (
	'/', 'Index',
	'/post', 'Post',
)


### Templates
#t_globals = {
#	'datestr': web.datestr
#}
render = web.template.render('templates/')




class Index:

	def GET(self, name=None):
		"""Show Page"""	
		return render.index(name)


class Post:

	form = web.form.Form(
		web.form.Textbox('title', web.form.notnull, 
			size=30,
			description="Post title:"),
		web.form.Textarea('content', web.form.notnull, 
			rows=10, cols=60,
			description="Post content:"),
		web.form.Button('Post entry'),
	)

	def GET(self):
		"""form"""
		form = self.form()
		return render.post(form)

	def POST(self):
		form = self.form()
		if not form.validates():
				return render.post(form)
		raise web.seeother('/')



app = web.application(urls, globals())


if __name__ == "__main__":
	
	app.run()
