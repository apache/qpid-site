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

# Qpid Proton 0.32.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-335](https://issues.apache.org/jira/browse/PROTON-335) - Need a means of specifying and reading link properties
 - [PROTON-2077](https://issues.apache.org/jira/browse/PROTON-2077) - Change Minimum supported Visual Studio compiler to 2015
 - [PROTON-2208](https://issues.apache.org/jira/browse/PROTON-2208) - Change base C language/compiler requirements to C99 or equivalent
 - [PROTON-2246](https://issues.apache.org/jira/browse/PROTON-2246) - Restructure pn_netaddr_* implementation
 - [PROTON-2247](https://issues.apache.org/jira/browse/PROTON-2247) - [c] Proactor API to support 'raw' TCP connections using the proactor event loop
 - [PROTON-2250](https://issues.apache.org/jira/browse/PROTON-2250) - Simplify the locking inside the proactor epoll implementation
 - [PROTON-2258](https://issues.apache.org/jira/browse/PROTON-2258) - Mark the Proton work list as deprecated

## Bugs fixed

 - [PROTON-2080](https://issues.apache.org/jira/browse/PROTON-2080) - cc1plus: warning: -Wformat-security ignored without -Wformat [-Wformat-security]
 - [PROTON-2199](https://issues.apache.org/jira/browse/PROTON-2199) - memory leak in c++ object inspect
 - [PROTON-2215](https://issues.apache.org/jira/browse/PROTON-2215) - Windows build fails if CMAKE_MODULE_PATH is not empty
 - [PROTON-2222](https://issues.apache.org/jira/browse/PROTON-2222) - Undefined variable `x` in scripts/env.py
 - [PROTON-2226](https://issues.apache.org/jira/browse/PROTON-2226) - [proton-c] Assert in pni_add_work during pn_proactor_done
 - [PROTON-2228](https://issues.apache.org/jira/browse/PROTON-2228) - Epoll proactor listener leaks file descriptors on close
 - [PROTON-2244](https://issues.apache.org/jira/browse/PROTON-2244) - [Proton-c] Encoder error for array of lists where first list in array is empty
 - [PROTON-2252](https://issues.apache.org/jira/browse/PROTON-2252) - Coverity warning of buffer overrun in pn_proactor_addr
 - [PROTON-2265](https://issues.apache.org/jira/browse/PROTON-2265) - Build fails with older CMake version 2.8.12