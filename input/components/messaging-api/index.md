;;
;; Licensed to the Apache Software Foundation (ASF) under one
;; or more contributor license agreements.  See the NOTICE file
;; distributed with this work for additional information
;; regarding copyright ownership.  The ASF licenses this file
;; to you under the Apache License, Version 2.0 (the
;; "License"); you may not use this file except in compliance
;; with the License.  You may obtain a copy of the License at
;; 
;;   http://www.apache.org/licenses/LICENSE-2.0
;; 
;; Unless required by applicable law or agreed to in writing,
;; software distributed under the License is distributed on an
;; "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
;; KIND, either express or implied.  See the License for the
;; specific language governing permissions and limitations
;; under the License.
;;

# Qpid Messaging API

A connection-oriented messaging API that supports many languages and
platforms.

  - *Languages* - C++, Python 2
  - *Platforms* - Linux, Windows
  - *AMQP versions* - C++: 1.0, 0-10, Python: 0-10
  - *Downloads* - C++, bindings: [qpid-cpp-{{current_cpp_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz) \[[ASC](https://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.asc), [MD5](https://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.md5), [SHA512](https://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.sha512)],<br/>Python: [qpid-python-{{current_python_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz) \[[ASC](https://www.apache.org/dist/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz.asc), [MD5](https://www.apache.org/dist/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz.md5), [SHA512](https://www.apache.org/dist/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz.sha512)]
  - *Source location* -  <https://gitbox.apache.org/repos/asf/qpid-cpp.git>,<br/> <https://gitbox.apache.org/repos/asf/qpid-python.git>

**NOTE**: For Python, look instead to [Qpid Proton](http://qpid.apache.org/proton) for Python 3 and AMQP 1.0 support.

## Documentation

This is the documentation for the current released version.  You can
find previous versions with our
[past releases]({{site_url}}/releases/index.html#past-releases).

<div class="two-column" markdown="1">

 - [Using the Qpid Messaging API]({{current_cpp_release_url}}/messaging-api/book/using-the-qpid-messaging-api.html) ([PDF]({{current_cpp_release_url}}/messaging-api/qpid-messaging-api-book.pdf))
 - [C++ API reference]({{current_cpp_release_url}}/messaging-api/cpp/api/annotated.html)
 - [C++ examples]({{current_cpp_release_url}}/messaging-api/cpp/examples/index.html)
 - [Python API reference]({{current_python_release_url}}/messaging-api/api/index.html)
 - [Python examples]({{current_python_release_url}}/messaging-api/examples/index.html)
 - [Installing Qpid C++](https://raw.githubusercontent.com/apache/qpid-cpp/master/INSTALL.txt)
 - [Installing Qpid Python](https://raw.githubusercontent.com/apache/qpid-python/master/README.md)

</div>

### Examples

  | Language | Hello World | Client | Server | Spout | Drain |
  | - | - | - | - | - | - |
  | *C++* | [hello_world.cpp]({{current_cpp_release_url}}/messaging-api/cpp/examples/hello_world.cpp.html) | [client.cpp]({{current_cpp_release_url}}/messaging-api/cpp/examples/client.cpp.html) | [server.cpp]({{current_cpp_release_url}}/messaging-api/cpp/examples/server.cpp.html) | [spout.cpp]({{current_cpp_release_url}}/messaging-api/cpp/examples/spout.cpp.html) | [drain.cpp]({{current_cpp_release_url}}/messaging-api/cpp/examples/drain.cpp.html) |
  | *Python* | [hello]({{current_python_release_url}}/messaging-api/examples/hello.html) |  | [server]({{current_python_release_url}}/messaging-api/examples/server.html) | [spout]({{current_python_release_url}}/messaging-api/examples/spout.html) | [drain]({{current_python_release_url}}/messaging-api/examples/drain.html) |

For Python, look instead to [Qpid Proton](http://qpid.apache.org/proton) for Python 3 and AMQP 1.0 support.
## Issues

For more information about finding and reporting bugs, see
[Qpid issues]({{site_url}}/issues.html).

<form id="jira-search-form">
  <input type="hidden" name="jql" value="project = QPID and component in ('C++ Client', 'Dot Net Client', 'Perl Client', 'Python Client', 'Ruby Client') and text ~ '{}' order by updatedDate desc"/>
  <input type="text" name="text"/>
  <button type="submit">Search</button>
</form>

<div class="two-column" markdown="1">

 - [Open bugs](https://issues.apache.org/jira/issues/?jql=resolution%20%3D%20EMPTY%20and%20issuetype%20%3D%20%22Bug%22%20and%20component%20in%20\(%22C%2B%2B%20Client%22%2C%20%22Dot%20Net%20Client%22%2C%20%22Perl%20Client%22%2C%20%22Python%20Client%22%2C%20%22Ruby%20Client%22\)%20and%20project%20%3D%20%22QPID%22)
 - [Fixed bugs](https://issues.apache.org/jira/issues/?jql=resolution%20%3D%20Fixed%20and%20issuetype%20%3D%20%22Bug%22%20and%20component%20in%20\(%22C%2B%2B%20Client%22%2C%20%22Dot%20Net%20Client%22%2C%20%22Perl%20Client%22%2C%20%22Python%20Client%22%2C%20%22Ruby%20Client%22\)%20and%20project%20%3D%20%22QPID%22)
 - [Requested enhancements](https://issues.apache.org/jira/issues/?jql=resolution%20%3D%20EMPTY%20and%20issuetype%20in%20\(%22New%20Feature%22%2C%20%22Improvement%22\)%20and%20component%20in%20\(%22C%2B%2B%20Client%22%2C%20%22Dot%20Net%20Client%22%2C%20%22Perl%20Client%22%2C%20%22Python%20Client%22%2C%20%22Ruby%20Client%22\)%20and%20project%20%3D%20%22QPID%22)
 - [Completed enhancements](https://issues.apache.org/jira/issues/?jql=resolution%20%3D%20Fixed%20and%20issuetype%20in%20\(%22New%20Feature%22%2C%20%22Improvement%22\)%20and%20component%20in%20\(%22C%2B%2B%20Client%22%2C%20%22Dot%20Net%20Client%22%2C%20%22Perl%20Client%22%2C%20%22Python%20Client%22%2C%20%22Ruby%20Client%22\)%20and%20project%20%3D%20%22QPID%22)
 - [Report a bug](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=1&priority=3&summary=[Enter%20a%20brief%20description]&components=12311396)
 - [Request an enhancement](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=4&priority=3&summary=[Enter%20a%20brief%20description]&components=12311396)
 - [Jira summary page](http://issues.apache.org/jira/browse/QPID/component/12311396)

</div>
