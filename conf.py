## conf.py

version = '3.0'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# Add custom css overrides
def setup(app):
  app.add_stylesheet( "custom.css" )

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
# html_css_files = [
#    'css/custom.css',
# ]

# html_js_files = [
#    'js/custom.js',
# ]

master_doc = 'index'
