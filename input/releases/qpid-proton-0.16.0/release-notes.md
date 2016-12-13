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

# Qpid Proton 0.16.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-721](https://issues.apache.org/jira/browse/PROTON-721) - [proton-j] expose ability to operate on Link capabilities
 - [PROTON-722](https://issues.apache.org/jira/browse/PROTON-722) - [proton-j] expose ability to operate on Session capabilities and properties
 - [PROTON-1309](https://issues.apache.org/jira/browse/PROTON-1309) - Add the ability to set the outgoing message window to electron interface
 - [PROTON-1314](https://issues.apache.org/jira/browse/PROTON-1314) - Fixing SIGPIPE ignore on Solaris OS
 - [PROTON-1315](https://issues.apache.org/jira/browse/PROTON-1315) - Force compilation in multi-threading mode for Solaris SunStudio
 - [PROTON-1316](https://issues.apache.org/jira/browse/PROTON-1316) - Add a way to set visibility of exportable symbols on Solaris
 - [PROTON-1317](https://issues.apache.org/jira/browse/PROTON-1317) - Add template parameter because SunStudio 12.1 doesn't handle templated method signature detection when using an "extern c" parameter
 - [PROTON-1318](https://issues.apache.org/jira/browse/PROTON-1318) - Replace variadic constructror of "sfinae::wildcard" with template for SunStudio
 - [PROTON-1319](https://issues.apache.org/jira/browse/PROTON-1319) - [SunStudio] Move internal header files of cpp bindings from src to their own directory
 - [PROTON-1320](https://issues.apache.org/jira/browse/PROTON-1320) - Add namespace prefix to srand and rand
 - [PROTON-1322](https://issues.apache.org/jira/browse/PROTON-1322) - Fix Sunstudio unable to find templated method when parameter can be constructed by an intermediate class (proton::scalar --&gt; proton::value)
 - [PROTON-1327](https://issues.apache.org/jira/browse/PROTON-1327) - Go binding should not use any proton-c handlers
 - [PROTON-1337](https://issues.apache.org/jira/browse/PROTON-1337) - [proton-j] Add methods and Sender and Receiver that allow for alternate buffer types
 - [PROTON-1338](https://issues.apache.org/jira/browse/PROTON-1338) - Go: make binding compatible with older C libraries, update `go get` 
 - [PROTON-1344](https://issues.apache.org/jira/browse/PROTON-1344) - Provide C "proactor" API for multi-threaded proton applications
 - [PROTON-1351](https://issues.apache.org/jira/browse/PROTON-1351) - Introduce proton core library
 - [PROTON-1352](https://issues.apache.org/jira/browse/PROTON-1352) - Trivial casting from UnsignedByte to ReceiverSettleMode and SenderSettleMode
 - [PROTON-1353](https://issues.apache.org/jira/browse/PROTON-1353) - Adding message annotations on toString for Message implementation class
 - [PROTON-1355](https://issues.apache.org/jira/browse/PROTON-1355) - Allow controlling peer_hostname independently of connection url
 - [PROTON-1363](https://issues.apache.org/jira/browse/PROTON-1363) - Remove unecessary and unused stuff from the C++ binding
 - [PROTON-1373](https://issues.apache.org/jira/browse/PROTON-1373) - Clean up C++ API docs

## Bugs fixed

 - [PROTON-241](https://issues.apache.org/jira/browse/PROTON-241) - proton-c: mark old transport interfaces 'deprecated'
 - [PROTON-623](https://issues.apache.org/jira/browse/PROTON-623) - Add missing error check to pn_string_inspect
 - [PROTON-1012](https://issues.apache.org/jira/browse/PROTON-1012) - Unable to build python-qpid-proton when behind a proxy server
 - [PROTON-1292](https://issues.apache.org/jira/browse/PROTON-1292) - errno not thread-safe on Solaris
 - [PROTON-1311](https://issues.apache.org/jira/browse/PROTON-1311) - [proton-c] Accessors for max-message-size on link
 - [PROTON-1324](https://issues.apache.org/jira/browse/PROTON-1324) - Interpretation of "int8_t" on Solaris using SunStudio is different from GCC one
 - [PROTON-1325](https://issues.apache.org/jira/browse/PROTON-1325) - Python "buffer" type in Message body should map to a known encoding type
 - [PROTON-1330](https://issues.apache.org/jira/browse/PROTON-1330) - Include the C sources in the python source distribution
 - [PROTON-1331](https://issues.apache.org/jira/browse/PROTON-1331) - go: electron.Container.Dial returning (nil, nil)
 - [PROTON-1332](https://issues.apache.org/jira/browse/PROTON-1332) - go: electron client leaking links/sessions in long lived connection
 - [PROTON-1333](https://issues.apache.org/jira/browse/PROTON-1333) - CMake error if no C++ compiler avaliable.
 - [PROTON-1336](https://issues.apache.org/jira/browse/PROTON-1336) - [Proton-c 0.14.0][Visual Studio 2013] Failing ssl unit test only in Debug mode
 - [PROTON-1346](https://issues.apache.org/jira/browse/PROTON-1346) - [proton-j] reactor exit when UnresolvedAddressException is thrown during connect
 - [PROTON-1366](https://issues.apache.org/jira/browse/PROTON-1366) - Reactor Python - segfault when out of file descriptors
 - [PROTON-1371](https://issues.apache.org/jira/browse/PROTON-1371) - proton::container::schedule crashes when mixing different language versions
 - [PROTON-1372](https://issues.apache.org/jira/browse/PROTON-1372) - Use PIMPL, not an interface, for event_loop

## Tasks

 - [PROTON-1329](https://issues.apache.org/jira/browse/PROTON-1329) - [proton-j] remove the TestDecoder class
 - [PROTON-1361](https://issues.apache.org/jira/browse/PROTON-1361) - [proton-j] mark Messenger as deprecated