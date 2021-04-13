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

# Qpid Proton 0.34.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2314](https://issues.apache.org/jira/browse/PROTON-2314) - [python] reconnect/failover is a bit of a mess
 - [PROTON-2315](https://issues.apache.org/jira/browse/PROTON-2315) - [python] BlockingConnection has no way to allow failover
 - [PROTON-2319](https://issues.apache.org/jira/browse/PROTON-2319) - [python] Remove support for python 2.6
 - [PROTON-2332](https://issues.apache.org/jira/browse/PROTON-2332) - Allow access to link properties in cpp binding 
 - [PROTON-2338](https://issues.apache.org/jira/browse/PROTON-2338) - Allow proactor raw connections to be half closed
 - [PROTON-2339](https://issues.apache.org/jira/browse/PROTON-2339) - Introduce 'Drain buffers' event to proactor raw connection
 - [PROTON-2343](https://issues.apache.org/jira/browse/PROTON-2343) - Simplify and clean up build flag selection for different compilers

## Bugs fixed

 - [PROTON-1914](https://issues.apache.org/jira/browse/PROTON-1914) - [c] receiver cannot settle an incomplete incoming message
 - [PROTON-2217](https://issues.apache.org/jira/browse/PROTON-2217) - Python detection logic prefers python2 over python3 when both are installed
 - [PROTON-2248](https://issues.apache.org/jira/browse/PROTON-2248) - [c] Codec pn_data_vfill() method doc has symbol and string types interchanged
 - [PROTON-2309](https://issues.apache.org/jira/browse/PROTON-2309) - [cpp] If reconnect is on client responds to a forced close from server by only closing the socket
 - [PROTON-2327](https://issues.apache.org/jira/browse/PROTON-2327) - Installed C example build fails using CMake 2.8.12
 - [PROTON-2328](https://issues.apache.org/jira/browse/PROTON-2328) - epoll proactor bug in tracking previous task used by a thread
 - [PROTON-2329](https://issues.apache.org/jira/browse/PROTON-2329) - Incorrect handling of commandline options in ssl.cpp example
 - [PROTON-2340](https://issues.apache.org/jira/browse/PROTON-2340) - Fix some proactor raw connection issues found with TSAN
 - [PROTON-2342](https://issues.apache.org/jira/browse/PROTON-2342) - Fails to build on Fedora rawhide
 - [PROTON-2344](https://issues.apache.org/jira/browse/PROTON-2344) - memory leak and close_waits in qpid-proton-c / python2-qpid-proton when dropping timeouted connection
 - [PROTON-2346](https://issues.apache.org/jira/browse/PROTON-2346) - Build failure on musl
 - [PROTON-2354](https://issues.apache.org/jira/browse/PROTON-2354) - C++ test failures on MacOS due to unexported symbols being  hidden
 - [PROTON-2355](https://issues.apache.org/jira/browse/PROTON-2355) - Build failure with -DPROACTOR=none

## Tasks

 - [PROTON-2320](https://issues.apache.org/jira/browse/PROTON-2320) - Apply autofixes to resolve some flake8 code formatting issues