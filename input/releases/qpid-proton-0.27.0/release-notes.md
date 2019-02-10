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

# Qpid Proton 0.27.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-985](https://issues.apache.org/jira/browse/PROTON-985) - Modify pn_transport_tick to explicitly use a monotonic clock, not wall clock time
 - [PROTON-1887](https://issues.apache.org/jira/browse/PROTON-1887) - [c] Introduce external C test harness for C tests
 - [PROTON-1959](https://issues.apache.org/jira/browse/PROTON-1959) - [c,cpp] API additions to simplify reconnect
 - [PROTON-1973](https://issues.apache.org/jira/browse/PROTON-1973) - Allow proton-test to be run as a python module ("python -m proton_tests")
 - [PROTON-1983](https://issues.apache.org/jira/browse/PROTON-1983) - [c] Fuzz regression testing: Use reponse files instead of long command line

## Bugs fixed

 - [PROTON-1805](https://issues.apache.org/jira/browse/PROTON-1805) - [MacOS] Fuzzer issues in fuzz-connection-driver &amp; fuzz-message-decode
 - [PROTON-1910](https://issues.apache.org/jira/browse/PROTON-1910) - Profiling indicates that cgo becomes a bottleneck during scale testing of electron
 - [PROTON-1933](https://issues.apache.org/jira/browse/PROTON-1933) - [go] error from ill-formed message is not reported
 - [PROTON-1951](https://issues.apache.org/jira/browse/PROTON-1951) - [go] Server connection fails to authenticate if Server() is not first
 - [PROTON-1953](https://issues.apache.org/jira/browse/PROTON-1953) - [go] occasional client/server hang with high volume of messages
 - [PROTON-1954](https://issues.apache.org/jira/browse/PROTON-1954) - [go] Container should default to random container-id
 - [PROTON-1955](https://issues.apache.org/jira/browse/PROTON-1955) - [go] incorrect conversion between Go time and AMQP time
 - [PROTON-1960](https://issues.apache.org/jira/browse/PROTON-1960) - [Go Electron] Unable to send a message larger than 16k in size
 - [PROTON-1968](https://issues.apache.org/jira/browse/PROTON-1968) - SSL stub will not link if compiled as C++
 - [PROTON-1969](https://issues.apache.org/jira/browse/PROTON-1969) - Tox fails to run proton-test on Windows as invocation relies on #!
 - [PROTON-1970](https://issues.apache.org/jira/browse/PROTON-1970) - Need to compile proton-core with VS2008 (msvc9) to make python2.7 extension
 - [PROTON-1974](https://issues.apache.org/jira/browse/PROTON-1974) - Libraries are not being correctly detected in CMake build scripts when old CMake is used
 - [PROTON-1978](https://issues.apache.org/jira/browse/PROTON-1978) - Disposition frames can take a *very* long time to complete
 - [PROTON-1979](https://issues.apache.org/jira/browse/PROTON-1979) - Decoding a bad message can overflow the stack
 - [PROTON-1982](https://issues.apache.org/jira/browse/PROTON-1982) - Proton C tests fail to build if C++ compiler is not available
 - [PROTON-1984](https://issues.apache.org/jira/browse/PROTON-1984) - [c] pn_data_inspect has order n^2 running time
 - [PROTON-1985](https://issues.apache.org/jira/browse/PROTON-1985) - [Python] db_recv example throws away messages by default!
 - [PROTON-1986](https://issues.apache.org/jira/browse/PROTON-1986) - [Python] Example broker does not allow example client and server to work together
 - [PROTON-1990](https://issues.apache.org/jira/browse/PROTON-1990) - drain gets stuck on
 - [PROTON-1991](https://issues.apache.org/jira/browse/PROTON-1991) - [Python] Tornado examples no longer work