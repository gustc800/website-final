from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, World!'

@app.route('/about')
def about():
	return 'about page'

@app.route('/bokeh')
def bokeh():
	fig=figure(plot_width=600, plot_height=600)
	fig.vbar(
		y=[1,2,3,4],
		width=0.5,
		bottom= 0,
		top=[1.7, 2.2, 4.6, 3.9],
		color= 'navy'
	)

	js_resources = INLINE.render_js()
	css_resources = INLINE.redner_css()

	script, diy = components(fig)
	html = render_template(
		'index.html',
		plot_script =script,
		plot_div = div,
		js_resources = js_resources,
		css_resources = css_resources
		)



if __name__ == '__main__':
	app.run(debug=True)

