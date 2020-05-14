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

# Qpid Proton 0.30.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2030](https://issues.apache.org/jira/browse/PROTON-2030) - Use CLOCK_MONOTONIC in proactors for pn_transport_tick
 - [PROTON-2096](https://issues.apache.org/jira/browse/PROTON-2096) - Drop Python 3 &lt; 3.5
 - [PROTON-2105](https://issues.apache.org/jira/browse/PROTON-2105) - Support Go modules
 - [PROTON-2119](https://issues.apache.org/jira/browse/PROTON-2119) - [Python] Change API to better handle strings where symbols are required
 - [PROTON-2124](https://issues.apache.org/jira/browse/PROTON-2124) - Disable GS2-KRB5 and GS2-IAKERB SASL mechanisms if they are not explicitly enabled
 - [PROTON-2131](https://issues.apache.org/jira/browse/PROTON-2131) - Improved logging API
 - [PROTON-2140](https://issues.apache.org/jira/browse/PROTON-2140) - proton-c has very high memory footprint for links
 - [PROTON-2144](https://issues.apache.org/jira/browse/PROTON-2144) - [C] Memory usage tracking
 - [PROTON-2146](https://issues.apache.org/jira/browse/PROTON-2146) - Reduce memory per connection
 - [PROTON-2148](https://issues.apache.org/jira/browse/PROTON-2148) - Reduce size of shared object data segment
 - [PROTON-2150](https://issues.apache.org/jira/browse/PROTON-2150) - Small reorganisation of object system to allow finer grained memory tracking
 - [PROTON-2155](https://issues.apache.org/jira/browse/PROTON-2155) - Switch helloworld.py back to connect with args

## Bugs fixed

 - [PROTON-2091](https://issues.apache.org/jira/browse/PROTON-2091) - [python] example broker never removes empty queues
 - [PROTON-2092](https://issues.apache.org/jira/browse/PROTON-2092) - [C++] When we use proton::connection::connect() [no arguments] allow no connect.json to get purely default settings
 - [PROTON-2098](https://issues.apache.org/jira/browse/PROTON-2098) - [Python] client abruptly disconnects after receiving disconnect-close-half socket close sequence
 - [PROTON-2099](https://issues.apache.org/jira/browse/PROTON-2099) - [Python] example test runner script leaks file handles
 - [PROTON-2102](https://issues.apache.org/jira/browse/PROTON-2102) - [Python] Improve python build and packaging
 - [PROTON-2103](https://issues.apache.org/jira/browse/PROTON-2103) - [Python] abstract_server example has incorrect import
 - [PROTON-2109](https://issues.apache.org/jira/browse/PROTON-2109) - [Python] Correct default JSON schema to amqps
 - [PROTON-2110](https://issues.apache.org/jira/browse/PROTON-2110) - [Python] Expand tilde symbol as user's home directory when searching for connect.json file
 - [PROTON-2116](https://issues.apache.org/jira/browse/PROTON-2116) - Memory leak in python client
 - [PROTON-2126](https://issues.apache.org/jira/browse/PROTON-2126) - Appveyor: pip install --user setuptools tox: `exec code in run_globals` File "C:\Python27\Scripts\pip.exe\__main__.py", line 9, in &lt;module&gt; TypeError: 'module' object is not callable Command exited with code 1
 - [PROTON-2127](https://issues.apache.org/jira/browse/PROTON-2127) - Proton doesn't build on FreeBSD currently
 - [PROTON-2132](https://issues.apache.org/jira/browse/PROTON-2132) - proton-cpp fails to build with build on clang 9.0 when libc++ is used instead of libstdc++
 - [PROTON-2137](https://issues.apache.org/jira/browse/PROTON-2137) - [cpp] Performance regression found in 0.29.0
 - [PROTON-2138](https://issues.apache.org/jira/browse/PROTON-2138) - Capabilities not retrieved from transaction coordinator target
 - [PROTON-2143](https://issues.apache.org/jira/browse/PROTON-2143) - Linkage warnings build proton-c/python bindings
 - [PROTON-2145](https://issues.apache.org/jira/browse/PROTON-2145) - libqpid-proton-cpp-static.a not included in make install
 - [PROTON-2149](https://issues.apache.org/jira/browse/PROTON-2149) - Handler incorrectly uses session state a method call
 - [PROTON-2153](https://issues.apache.org/jira/browse/PROTON-2153) - Python Proton Reactor get_connection_address attempts to call non-existent connection.get_address method

## Tasks

 - [PROTON-1801](https://issues.apache.org/jira/browse/PROTON-1801) - Strip the version from the /usr/share/proton dir