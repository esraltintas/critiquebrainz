from publication import publication

def register_blueprints(app, prefix):
	app.register_blueprint(publication, url_prefix='%s/publication' % prefix)