class _Release(object):
    def __init__(self, component_name, component_key, number):
        self.component_name = component_name
        self.component_key = component_key
        self.number = number

    @property
    def name(self):
        return "{} {}".format(self.component_name, self.number)

    @property
    def url(self):
        args = site_url, self.component_key, self.number
        return "{}/releases/{}-{}".format(*args)

    @property
    def link(self):
        return "<a href=\"{}\">{}</a>".format(self.url, self.name)

qpid_release = _Release("Qpid", "qpid", "0.32")

cpp_release = _Release("Qpid C++", "qpid-cpp", "0.34")
dispatch_release = _Release("Qpid Dispatch", "qpid-dispatch", "0.6.0")
java_release = _Release("Qpid Java", "qpid-java", "6.0.4")
jms_release = _Release("Qpid JMS", "qpid-jms", "0.9.0")
proton_release = _Release("Qpid Proton", "qpid-proton", "0.13.0")

_svn_base = "http://svn.apache.org/repos/asf/qpid"

current_release = qpid_release.number
current_release_url = qpid_release.url
current_release_link = qpid_release.link
current_release_tag = "{}/tags/{}".format(_svn_base, qpid_release.number)

current_cpp_release = cpp_release.number
current_cpp_release_url = cpp_release.url
current_cpp_release_link = cpp_release.link

current_java_release = java_release.number
current_java_release_url = java_release.url
current_java_release_link = java_release.link

current_jms_release = jms_release.number
current_jms_release_url = jms_release.url
current_jms_release_link = jms_release.link

current_dispatch_release = dispatch_release.number
current_dispatch_release_url = dispatch_release.url
current_dispatch_release_link = dispatch_release.link

current_proton_release = proton_release.number
current_proton_release_url = proton_release.url
current_proton_release_link = proton_release.link
