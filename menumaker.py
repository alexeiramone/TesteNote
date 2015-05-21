# -*- coding: utf-8 -*-
bootstrap = """
<!DOCTYPE html>
<html>
  <head>
    <title>Bootstrap 101 Template</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link href="https://maxcdn.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet" media="screen">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>

    <div class="navbar">
      <div class="navbar-inner">
        <div class="container">
     
          <!-- .btn-navbar is used as the toggle for collapsed navbar content -->
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
     
          <!-- Be sure to leave the brand out there if you want it shown -->
          <a class="brand" href="#">Project name</a>
     
          <!-- Everything you want hidden at 940px or less, place within here -->
          <div class="nav-collapse collapse">
            <!-- .nav, .navbar-search, .navbar-form, etc -->
            {}
          </div>
     
        </div>
      </div>
    </div>


  </body>
</html>
"""

class MenuItem(object):
    """docstring for MenuItem"""
    def __init__(self, href, texto, active=False):
        super(MenuItem, self).__init__()
        self.href = href
        self.texto = texto
        self.active = ' class="active"' if active else ''

    def __str__(self):
        return u'<li{0.active}><a href="{0.href}">{0.texto}</a></li>'.format(self)


class MenuSearch(object):
    """docstring for MenuItem"""
    def __init__(self, action="", klass="pull-left", placeholder="Search"):
        super(MenuSearch, self).__init__()
        self.placeholder = placeholder
        self.klass = klass
        self.action = action

    def __str__(self):
        return u'<form class="navbar-search {0.klass}" action="{0.action}"><input type="text" class="search-query" placeholder="{0.placeholder}"></form>'.format(self)



items = [
    MenuItem('/bunda','Primeiro'), MenuItem('/bunda','Segundo Ativo', active=True),
    ('Dropdown', [MenuItem('/bunda','Drop 01'), MenuItem('/bunda','Drop 02')]),
    MenuSearch(),
]

html = ""

def explode(node, klass="nav"):
    html = ""
    if type(node) == list:
        for i in node:
            html += explode(i)
        return '<ul class="{}">{}</ul>'.format(klass,html)
    if type(node) == tuple:
        drop_name, items = node
        html += explode(items,'dropdown-menu')
        return '<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">{} <b class="caret"></b></a>{}</li>'.format(drop_name,html)
    elif isinstance(node, MenuItem) or isinstance(node, MenuSearch):
        return str(node)


output = bootstrap.format(explode(items))
print output
with file('menumaker.html','w') as arq:
    arq.write(output)
    arq.close()