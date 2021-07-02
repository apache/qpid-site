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

# Qpid Proton 0.35.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2323](https://issues.apache.org/jira/browse/PROTON-2323) - [python] Remove support for python 2.7
 - [PROTON-2324](https://issues.apache.org/jira/browse/PROTON-2324) - Support Python 3.9
 - [PROTON-2370](https://issues.apache.org/jira/browse/PROTON-2370) - [cpp] An accessor for the delivery tag
 - [PROTON-2375](https://issues.apache.org/jira/browse/PROTON-2375) - Make connection driver more efficient when finishing writes
 - [PROTON-2387](https://issues.apache.org/jira/browse/PROTON-2387) - [C++] Remove support for compiler prior to C++ 11
 - [PROTON-2397](https://issues.apache.org/jira/browse/PROTON-2397) - Update default client TLS defaults for verifying outbound connections to AMQP servers.

## Bugs fixed

 - [PROTON-2377](https://issues.apache.org/jira/browse/PROTON-2377) - [cpp] tag_counter is not used in a thread safe way in sender.cpp