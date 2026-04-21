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

<div class="retired-component" markdown="1">
**WARNING**: Qpid C++ and Qpid Python have been retired and are no longer maintained. This page is for historic
reference and may be stale. No new features, bug fixes, or security updates will be provided.
</div>

# Qpid Messaging API

A connection-oriented messaging API that supports many languages and
platforms.

  - *Languages* - C++, Python 2
  - *Platforms* - Linux, Windows
  - *AMQP versions* - C++: 1.0, 0-10, Python: 0-10
  - *Archived Downloads* - C++: [qpid-cpp](https://archive.apache.org/dist/qpid/cpp/),<br/>Python: [qpid-python](https://archive.apache.org/dist/qpid/python/)
  - *Source location* -  C++: [qpid-cpp](https://gitbox.apache.org/repos/asf/qpid-cpp.git),<br/> Python: [qpid-python](https://gitbox.apache.org/repos/asf/qpid-python.git)

**NOTE**: For Python and C++, look instead to [Qpid Proton](https://qpid.apache.org/proton) for Python 3, C++, and AMQP 1.0 support.

## Documentation

This is the documentation for the final released version.

<div class="two-column" markdown="1">

 - [Using the Qpid Messaging API]({{final_cpp_release_url}}/messaging-api/book/using-the-qpid-messaging-api.html) ([PDF]({{final_cpp_release_url}}/messaging-api/qpid-messaging-api-book.pdf))
 - [C++ API reference]({{final_cpp_release_url}}/messaging-api/cpp/api/annotated.html)
 - [C++ examples]({{final_cpp_release_url}}/messaging-api/cpp/examples/index.html)
 - [Python API reference]({{final_python_release_url}}/messaging-api/api/index.html)
 - [Python examples]({{final_python_release_url}}/messaging-api/examples/index.html)
 - [Installing Qpid C++](https://raw.githubusercontent.com/apache/qpid-cpp/{{final_cpp_release}}/INSTALL.txt)
 - [Installing Qpid Python](https://raw.githubusercontent.com/apache/qpid-python/{{final_python_release}}/README.md)

</div>

### Examples

  | Language | Hello World | Client | Server | Spout | Drain |
  | - | - | - | - | - | - |
  | *C++* | [hello_world.cpp]({{final_cpp_release_url}}/messaging-api/cpp/examples/hello_world.cpp.html) | [client.cpp]({{final_cpp_release_url}}/messaging-api/cpp/examples/client.cpp.html) | [server.cpp]({{final_cpp_release_url}}/messaging-api/cpp/examples/server.cpp.html) | [spout.cpp]({{final_cpp_release_url}}/messaging-api/cpp/examples/spout.cpp.html) | [drain.cpp]({{final_cpp_release_url}}/messaging-api/cpp/examples/drain.cpp.html) |
  | *Python* | [hello]({{final_python_release_url}}/messaging-api/examples/hello.html) |  | [server]({{final_python_release_url}}/messaging-api/examples/server.html) | [spout]({{final_python_release_url}}/messaging-api/examples/spout.html) | [drain]({{final_python_release_url}}/messaging-api/examples/drain.html) |

**NOTE**: For Python and C++, look instead to [Qpid Proton](https://qpid.apache.org/proton) for Python 3, C++, and AMQP 1.0 support.

