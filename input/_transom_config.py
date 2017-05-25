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

broker_j_release = _Release("Qpid Broker-J", "qpid-broker-j", "6.2.0")
cpp_release = _Release("Qpid C++", "qpid-cpp", "1.36.0")
dispatch_release = _Release("Qpid Dispatch", "qpid-dispatch", "0.8.0")
interop_test_release = _Release("Qpid Interop Test", "qpid-interop", "0.1.0")
java_release = _Release("Qpid for Java", "qpid-java", "6.1.2")
jms_release = _Release("Qpid JMS", "qpid-jms", "0.23.0")
jms_amqp_0_x_release = _Release("Qpid JMS for AMQP 0-x", "qpid-jms-amqp-0-x", "6.2.0")
proton_release = _Release("Qpid Proton", "qpid-proton", "0.17.0")
proton_j_release = _Release("Qpid Proton-J", "qpid-proton-j", "0.19.0")
python_release = _Release("Qpid Python", "qpid-python", "1.36.0")

current_broker_j_release = broker_j_release.number
current_broker_j_release_url = broker_j_release.url
current_broker_j_release_link = broker_j_release.link

current_cpp_release = cpp_release.number
current_cpp_release_url = cpp_release.url
current_cpp_release_link = cpp_release.link

current_dispatch_release = dispatch_release.number
current_dispatch_release_url = dispatch_release.url
current_dispatch_release_link = dispatch_release.link

current_interop_test_release = interop_test_release.number
current_interop_test_release_url = interop_test_release.url
current_interop_test_release_link = interop_test_release.link

current_java_release = java_release.number
current_java_release_url = java_release.url
current_java_release_link = java_release.link

current_jms_release = jms_release.number
current_jms_release_url = jms_release.url
current_jms_release_link = jms_release.link

current_jms_amqp_0_x_release = jms_amqp_0_x_release.number
current_jms_amqp_0_x_release_url = jms_amqp_0_x_release.url
current_jms_amqp_0_x_release_link = jms_amqp_0_x_release.link

current_proton_release = proton_release.number
current_proton_release_url = proton_release.url
current_proton_release_link = proton_release.link

current_proton_j_release = proton_j_release.number
current_proton_j_release_url = proton_j_release.url
current_proton_j_release_link = proton_j_release.link

current_python_release = python_release.number
current_python_release_url = python_release.url
current_python_release_link = python_release.link
