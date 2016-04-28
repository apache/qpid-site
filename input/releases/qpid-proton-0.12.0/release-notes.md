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

# Qpid Proton 0.12.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).

**Note**: This release contains a new C++ binding of the Proton API.
The documented API is substantially settled, but there are some areas
that will change in the next release and should be considered unstable
API:

 - The `proton::connection_engine` and the `proton::io` interfaces
 - The `find_sessions` and `find_links` methods on `connection` and
   `session`

**Note**: Qpid C++ 0.34 builds will fail against this version of Proton
unless you set `-DCMAKE_CXX_FLAGS=-Wno-error=switch`.  A new release
of Qpid C++ will resolve this problem.

## New features and improvements

 - [PROTON-1037](https://issues.apache.org/jira/browse/PROTON-1037) - Add support for setting/getting message properties
 - [PROTON-1039](https://issues.apache.org/jira/browse/PROTON-1039) - Add support for setting/getting transport headers
 - [PROTON-1047](https://issues.apache.org/jira/browse/PROTON-1047) - go: improved ack handling in electron API, add to  broker example
 - [PROTON-1048](https://issues.apache.org/jira/browse/PROTON-1048) - Proton-C ssl tests on Windows with SChannel
 - [PROTON-1052](https://issues.apache.org/jira/browse/PROTON-1052) - SSL support in C++ reactor client
 - [PROTON-1053](https://issues.apache.org/jira/browse/PROTON-1053) - SASL support in C++ reactor client
 - [PROTON-1054](https://issues.apache.org/jira/browse/PROTON-1054) - Add acceptor context to incoming reactor connections.
 - [PROTON-1062](https://issues.apache.org/jira/browse/PROTON-1062) - proton::engine as a client example
 - [PROTON-1066](https://issues.apache.org/jira/browse/PROTON-1066) - Connection options for C++ binding
 - [PROTON-1068](https://issues.apache.org/jira/browse/PROTON-1068) - c++ remove counted_ptr and context types from public API
 - [PROTON-1076](https://issues.apache.org/jira/browse/PROTON-1076) - C++ binding acceptor context
 - [PROTON-1082](https://issues.apache.org/jira/browse/PROTON-1082) - add ability to specify and inspect properties for link attach frames
 - [PROTON-1083](https://issues.apache.org/jira/browse/PROTON-1083) - [C++] Simplify the messaging events
 - [PROTON-1085](https://issues.apache.org/jira/browse/PROTON-1085) - c++ improve message interface and dynamic value handling
 - [PROTON-1088](https://issues.apache.org/jira/browse/PROTON-1088) - Add convenience functions to obtain the client certificate fingerprint, subject subfields
 - [PROTON-1089](https://issues.apache.org/jira/browse/PROTON-1089) - C++ binding link options
 - [PROTON-1092](https://issues.apache.org/jira/browse/PROTON-1092) - c++: improve proton::message API
 - [PROTON-1095](https://issues.apache.org/jira/browse/PROTON-1095) - Error handling
 - [PROTON-1096](https://issues.apache.org/jira/browse/PROTON-1096) - [proton-j] enable set/get of MessageFormat on the Delivery being sent/received 
 - [PROTON-1102](https://issues.apache.org/jira/browse/PROTON-1102) - C++ binding remove _t suffix for types
 - [PROTON-1103](https://issues.apache.org/jira/browse/PROTON-1103) - C++ binding rename xxx_domain to ssl_xxx_options
 - [PROTON-1108](https://issues.apache.org/jira/browse/PROTON-1108) - Change DISCONNECT event to be called TRANSPORT_CLOSE, introduce TRANSPORT_ERROR event
 - [PROTON-1109](https://issues.apache.org/jira/browse/PROTON-1109) - Improve the C++ binding documentation

## Bugs fixed

 - [PROTON-713](https://issues.apache.org/jira/browse/PROTON-713) - TransportImpl#setChannelMax does not enforce legal value range, may cause unexpected results
 - [PROTON-829](https://issues.apache.org/jira/browse/PROTON-829) - Possible reference counting bug in pn_clear_tpwork
 - [PROTON-949](https://issues.apache.org/jira/browse/PROTON-949) - proton doesn't build with ccache swig
 - [PROTON-995](https://issues.apache.org/jira/browse/PROTON-995) - Url fails to parse URL
 - [PROTON-1000](https://issues.apache.org/jira/browse/PROTON-1000) - Connection leak on heartbeat-timeouted connections
 - [PROTON-1020](https://issues.apache.org/jira/browse/PROTON-1020) - Typos in the error messages
 - [PROTON-1026](https://issues.apache.org/jira/browse/PROTON-1026) - Invalid queue/destination causes a segmentation fault
 - [PROTON-1027](https://issues.apache.org/jira/browse/PROTON-1027) - Incorrectly handling of invalid addresses
 - [PROTON-1031](https://issues.apache.org/jira/browse/PROTON-1031) - [python] Bump the module version to 0.11.0
 - [PROTON-1035](https://issues.apache.org/jira/browse/PROTON-1035) - [proton-c] Python binding mishandles connection close event
 - [PROTON-1040](https://issues.apache.org/jira/browse/PROTON-1040) - BlockingConnection fails to send heartbeats if timeout is None and no local idle time is specified
 - [PROTON-1044](https://issues.apache.org/jira/browse/PROTON-1044) - Create/Delete of BlockingConnection leaks file descriptors
 - [PROTON-1045](https://issues.apache.org/jira/browse/PROTON-1045) - Use of callbacks to handle accepted endpoints violates design goals.
 - [PROTON-1049](https://issues.apache.org/jira/browse/PROTON-1049) - Reactor needs an alternative to using the URL to pass user authentication information.
 - [PROTON-1055](https://issues.apache.org/jira/browse/PROTON-1055) - Username sent twice during SASL AUTH
 - [PROTON-1056](https://issues.apache.org/jira/browse/PROTON-1056) - Attempting to print an ApplicationEvent raises a NameError
 - [PROTON-1059](https://issues.apache.org/jira/browse/PROTON-1059) - ruby: ruby binding broken in 0.11 release and on master
 - [PROTON-1060](https://issues.apache.org/jira/browse/PROTON-1060) - [Python Binding] API call types for some message properties do not match AMQP specification
 - [PROTON-1065](https://issues.apache.org/jira/browse/PROTON-1065) - dbgheap.c assertion when adding types to message body (through proton::value)
 - [PROTON-1067](https://issues.apache.org/jira/browse/PROTON-1067) - python messenger: cannot acknowledge messages, messenger forces auto-ack or pre-settled.
 - [PROTON-1069](https://issues.apache.org/jira/browse/PROTON-1069) - Windows schannel ssl hang in shutdown sequence
 - [PROTON-1074](https://issues.apache.org/jira/browse/PROTON-1074) - C++ cbinding SSL core dump
 - [PROTON-1075](https://issues.apache.org/jira/browse/PROTON-1075) - Data races detected in go_test_electron
 - [PROTON-1077](https://issues.apache.org/jira/browse/PROTON-1077) - receiver link and transport view of credit can become disjoint when sending link sends flow frames
 - [PROTON-1080](https://issues.apache.org/jira/browse/PROTON-1080) - have container attribute on any relevant event
 - [PROTON-1090](https://issues.apache.org/jira/browse/PROTON-1090) - BlockingConnection client spins at 100% cpu on reconnect
 - [PROTON-1093](https://issues.apache.org/jira/browse/PROTON-1093) - [proton-c++] pragma to hide a warning in GCC introduces a warning in Windows
 - [PROTON-1100](https://issues.apache.org/jira/browse/PROTON-1100) - [proton-j] the transport should not emit other frames before the Open frame has been sent
 - [PROTON-1101](https://issues.apache.org/jira/browse/PROTON-1101) - Proton build broken on Visual Studio 10
 - [PROTON-1104](https://issues.apache.org/jira/browse/PROTON-1104) - reactor hangs on reconnect
 - [PROTON-1105](https://issues.apache.org/jira/browse/PROTON-1105) - enable EventImpl#getTransport() to succeed in more situations
 - [PROTON-1107](https://issues.apache.org/jira/browse/PROTON-1107) - [proton-j] only create the attachments Record on a Delivery if it actually gets used
 - [PROTON-1110](https://issues.apache.org/jira/browse/PROTON-1110) - [proton-j] allow suppressing the synthentic flow event when sending transfers
 - [PROTON-1114](https://issues.apache.org/jira/browse/PROTON-1114) - [proton-j] the transport should not emit other frames after the Close frame has been sent
 - [PROTON-1116](https://issues.apache.org/jira/browse/PROTON-1116) - Potential infinite recursion detected by VC++14 compiler
 - [PROTON-1118](https://issues.apache.org/jira/browse/PROTON-1118) - python setup.py build fails if run from git repo
 - [PROTON-1120](https://issues.apache.org/jira/browse/PROTON-1120) - Memory leak using proton.utils
 - [PROTON-1121](https://issues.apache.org/jira/browse/PROTON-1121) - Zero pointer derefence in pn_sasl_allowed_mechs()
 - [PROTON-1123](https://issues.apache.org/jira/browse/PROTON-1123) - cmake fails under python3 when -DSYSINSTALL_BINDINGS=ON
 - [PROTON-1125](https://issues.apache.org/jira/browse/PROTON-1125) - c++: core dump on empty address in link options
 - [PROTON-1127](https://issues.apache.org/jira/browse/PROTON-1127) - [Windows] qpid-proton-cpp.dll not installed by "make install" target

## Tasks

 - [PROTON-973](https://issues.apache.org/jira/browse/PROTON-973) - various javadoc errors when building with Java 8
 - [PROTON-1084](https://issues.apache.org/jira/browse/PROTON-1084) - [cpp binding] Add message annotation support
 - [PROTON-1113](https://issues.apache.org/jira/browse/PROTON-1113) - tidy up some descriptive detail around running the python tests
