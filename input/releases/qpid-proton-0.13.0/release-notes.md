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

# Qpid Proton 0.13.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).

**Note:** Qpid C++ 0.34 builds will fail against this version of
Proton unless you set `-DCMAKE_CXX_FLAGS=-Wno-error=switch`. A new
release of Qpid C++ will resolve this problem.

**Note:** Users are advised to avoid any use of
`pn_connection_set_hostname()` to set the transport address on Proton
reactor connections.  A new reactor method has been introduced to deal
with this: `pn_reactor_connection_to_host(<reactor>, <host>, <port>,
<handler>)`.  The `pn_reactor_connection(<reactor>, <handler>)`
function has been deprecated in favor of this new interface.

**Note:** If the reactor connection's hostname is used to configure
the transport address (see above), then the C reactor may fail to
connect if the hostname does not include a ":<port>" suffix.  Using
the connection's hostname as the transport address is discouraged. Use
the new reactor connection factory method
`pn_reactor_connection_to_host()` instead.

**Note:** The python `Container.connect()` method now takes an
optional parameter with the keyword `virtual_host`. This can be used
to set the `hostname` attribute in the open frame sent by the client.

## New features and improvements

 - [PROTON-250](https://issues.apache.org/jira/browse/PROTON-250) - Add -fvisibility option when building shared libraries 
 - [PROTON-1046](https://issues.apache.org/jira/browse/PROTON-1046) - C++ multi-threaded broker example
 - [PROTON-1094](https://issues.apache.org/jira/browse/PROTON-1094) - c++:  refactor and documentation of type conversions
 - [PROTON-1111](https://issues.apache.org/jira/browse/PROTON-1111) - Fix warnings during make doc
 - [PROTON-1117](https://issues.apache.org/jira/browse/PROTON-1117) - Add link.detach method to C++ binding
 - [PROTON-1119](https://issues.apache.org/jira/browse/PROTON-1119) - C++ ssl_domain tracking uses unnecessary heap allocations
 - [PROTON-1138](https://issues.apache.org/jira/browse/PROTON-1138) - Assorted C++ API cleanups
 - [PROTON-1141](https://issues.apache.org/jira/browse/PROTON-1141) - Update JUnit Dependency and fix some warnings in the tests.
 - [PROTON-1142](https://issues.apache.org/jira/browse/PROTON-1142) - Remove proton-dump executable
 - [PROTON-1143](https://issues.apache.org/jira/browse/PROTON-1143) - Bump Minimum version of CMake to 2.8.7
 - [PROTON-1145](https://issues.apache.org/jira/browse/PROTON-1145) - Move the python shim code to the test module where it is used.
 - [PROTON-1147](https://issues.apache.org/jira/browse/PROTON-1147) - Add OSGi bundle metadata to the proton-j jar manifest 
 - [PROTON-1151](https://issues.apache.org/jira/browse/PROTON-1151) - [C++ binding] Move exposed implementation details into proton::internal namespace
 - [PROTON-1152](https://issues.apache.org/jira/browse/PROTON-1152) - [C++ binding] Make sure non API details in classes are private
 - [PROTON-1153](https://issues.apache.org/jira/browse/PROTON-1153) - [C++ binding] Tidy up various details
 - [PROTON-1161](https://issues.apache.org/jira/browse/PROTON-1161) - c++: better interface to connection_engine.
 - [PROTON-1178](https://issues.apache.org/jira/browse/PROTON-1178) - [C++ binding] Rearrange delivery class
 - [PROTON-1180](https://issues.apache.org/jira/browse/PROTON-1180) - [C++ binding] Change endpoint API
 - [PROTON-1182](https://issues.apache.org/jira/browse/PROTON-1182) - C++ binding: replace use of link with use of sender and receiver
 - [PROTON-1183](https://issues.apache.org/jira/browse/PROTON-1183) - C++ binding: deemphasize proton::terminus
 - [PROTON-1184](https://issues.apache.org/jira/browse/PROTON-1184) - c++: Merge the controller and container interfaces.
 - [PROTON-1186](https://issues.apache.org/jira/browse/PROTON-1186) - [C++ binding] Remove proton::url from core API
 - [PROTON-1187](https://issues.apache.org/jira/browse/PROTON-1187) - consistent options for endpoints
 - [PROTON-1191](https://issues.apache.org/jira/browse/PROTON-1191) - [C++ binding] Tidy up some exposed enum details
 - [PROTON-1194](https://issues.apache.org/jira/browse/PROTON-1194) - C++ flow control
 - [PROTON-1195](https://issues.apache.org/jira/browse/PROTON-1195) - [C++ binding] Don't use default parameters in ABI relevant places
 - [PROTON-1196](https://issues.apache.org/jira/browse/PROTON-1196) - Move connection options accessors from transport object to connection object
 - [PROTON-1197](https://issues.apache.org/jira/browse/PROTON-1197) - Ensure that private members don't have exported symbols
 - [PROTON-1198](https://issues.apache.org/jira/browse/PROTON-1198) - Add senders/receivers range constructors to connection
 - [PROTON-1200](https://issues.apache.org/jira/browse/PROTON-1200) - Improve the C++ binding documentation, round two
 - [PROTON-1203](https://issues.apache.org/jira/browse/PROTON-1203) - Improve header file usage consistency

## Bugs fixed

 - [PROTON-405](https://issues.apache.org/jira/browse/PROTON-405) - [proton-c] Windows install fails to find proton-api.jar file
 - [PROTON-629](https://issues.apache.org/jira/browse/PROTON-629) - Can't include proton-c header files in c-only applications in visual studio
 - [PROTON-988](https://issues.apache.org/jira/browse/PROTON-988) - pn_messenger_set_flags does not support new SASL flag correctly
 - [PROTON-992](https://issues.apache.org/jira/browse/PROTON-992) - Proton's use of Cyrus SASL is not thread-safe - short term fix
 - [PROTON-1041](https://issues.apache.org/jira/browse/PROTON-1041) - Add recurring timer example to the reactive C++ documentation
 - [PROTON-1115](https://issues.apache.org/jira/browse/PROTON-1115) - c++: memory leak in ssl examples
 - [PROTON-1122](https://issues.apache.org/jira/browse/PROTON-1122) - c++ fix issues raised by coverity
 - [PROTON-1124](https://issues.apache.org/jira/browse/PROTON-1124) - Small problems detected by Coverity scanner
 - [PROTON-1126](https://issues.apache.org/jira/browse/PROTON-1126) - Allow setting connection properties in BlockingConnection
 - [PROTON-1128](https://issues.apache.org/jira/browse/PROTON-1128) - [C++ binding] Symbol exports use wrong directive for proton::condition
 - [PROTON-1129](https://issues.apache.org/jira/browse/PROTON-1129) - C++ binding test failure with older python
 - [PROTON-1133](https://issues.apache.org/jira/browse/PROTON-1133) - Proton C includes port number in AMQP Open hostname
 - [PROTON-1135](https://issues.apache.org/jira/browse/PROTON-1135) - [proton-c] dont pipeline SASL and OPEN frames for ANONYMOUS logins by default
 - [PROTON-1144](https://issues.apache.org/jira/browse/PROTON-1144) - IPv6 addresses could be truncated by the accept code
 - [PROTON-1146](https://issues.apache.org/jira/browse/PROTON-1146) - [proton-j] fixes for issues identified by Coverity
 - [PROTON-1150](https://issues.apache.org/jira/browse/PROTON-1150) - Python setup.py fails to use environment settings
 - [PROTON-1171](https://issues.apache.org/jira/browse/PROTON-1171) - [proton-j] transport SSL wrapper does not flush all decoded bytes to the underlying input
 - [PROTON-1190](https://issues.apache.org/jira/browse/PROTON-1190) - [proton-j] Transport can emit erroneous Attach frames before session Begin and after session End frames
 - [PROTON-1193](https://issues.apache.org/jira/browse/PROTON-1193) - Proton-c uses getaddrinfo/socket calls incorrectly
 - [PROTON-1202](https://issues.apache.org/jira/browse/PROTON-1202) - The python setup script should only extract the C sources from the dist tar
 - [PROTON-1208](https://issues.apache.org/jira/browse/PROTON-1208) - CMake install target doesn't install correct files
 - [PROTON-1211](https://issues.apache.org/jira/browse/PROTON-1211) - C++ binding exception in message::correlation_id()
 - [PROTON-1212](https://issues.apache.org/jira/browse/PROTON-1212) - pn_unique_ptr operator ! returns the opposite result
 - [PROTON-1216](https://issues.apache.org/jira/browse/PROTON-1216) - c++: proton::coerce&lt;std::string&gt;() should allow conversion from binary.
 - [PROTON-1217](https://issues.apache.org/jira/browse/PROTON-1217) - Sporadic memory leak in C++ container_test
 - [PROTON-1218](https://issues.apache.org/jira/browse/PROTON-1218) - Fix errors in vhost handling
 - [PROTON-1219](https://issues.apache.org/jira/browse/PROTON-1219) - C Reactor sender/receiver examples leak like a sieve and fails to build on windows
 - [PROTON-1225](https://issues.apache.org/jira/browse/PROTON-1225) - c++: taking address of element 0 of an empty string or vector
 - [PROTON-1226](https://issues.apache.org/jira/browse/PROTON-1226) - Handler not set on inbound connection

## Tasks

 - [PROTON-1188](https://issues.apache.org/jira/browse/PROTON-1188) - remove the 'contrib/proton-jms' module
 - [PROTON-1189](https://issues.apache.org/jira/browse/PROTON-1189) - remove the 'contrib/proton-hawtdispatch' module
