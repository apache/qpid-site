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

# Qpid Proton 0.31.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2078](https://issues.apache.org/jira/browse/PROTON-2078) - Merge c/test/fuzz patches from oss-fuzz
 - [PROTON-2134](https://issues.apache.org/jira/browse/PROTON-2134) - Create suppression files for sanitizers and add tsan and asan to Travis CI
 - [PROTON-2195](https://issues.apache.org/jira/browse/PROTON-2195) - Tidy up/Finalise the API around proactor event batches
 - [PROTON-2196](https://issues.apache.org/jira/browse/PROTON-2196) - Tidying of proactor code

## Bugs fixed

 - [PROTON-1709](https://issues.apache.org/jira/browse/PROTON-1709) - [python] ApplicationEvent causing memory growth
 - [PROTON-2005](https://issues.apache.org/jira/browse/PROTON-2005) - [proton-c] AMQP error if delivery is aborted with session_outgoing bytes &gt; 0
 - [PROTON-2135](https://issues.apache.org/jira/browse/PROTON-2135) - C, cpp, and fuzz tests do not set TEST_ENV on Linux
 - [PROTON-2156](https://issues.apache.org/jira/browse/PROTON-2156) - [Python] Tornado integration broken by reconnect work
 - [PROTON-2159](https://issues.apache.org/jira/browse/PROTON-2159) - C++ example tests fail if SASLPASSWD env var is set.
 - [PROTON-2184](https://issues.apache.org/jira/browse/PROTON-2184) - pn_session_set_context() aborts if zero is passed as the context
 - [PROTON-2187](https://issues.apache.org/jira/browse/PROTON-2187) - Python client leak on early Connection.close
 - [PROTON-2194](https://issues.apache.org/jira/browse/PROTON-2194) - Incorrect memory deallocation
 - [PROTON-2200](https://issues.apache.org/jira/browse/PROTON-2200) - [Go] memory leak when in message unmarshal
 - [PROTON-2203](https://issues.apache.org/jira/browse/PROTON-2203) - Assertion error in new proactor code
 - [PROTON-2211](https://issues.apache.org/jira/browse/PROTON-2211) - Epoll proactor leaks file descriptors

## Tasks

 - [PROTON-2165](https://issues.apache.org/jira/browse/PROTON-2165) - Fix errors in the Python tutorial