import tornado.web

class NavbarModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('components/navbar.html')


class AsideModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('components/aside.html')


class FixedPluginModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('components/fixed-plugin.html')

