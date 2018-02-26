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

# Qpid Dispatch 1.0.1 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [DISPATCH-874](https://issues.apache.org/jira/browse/DISPATCH-874) - unable to load .json or .woff2 files from local file system from http port
 - [DISPATCH-881](https://issues.apache.org/jira/browse/DISPATCH-881) - Inbound pre-settled messages causes memory leak of deliveries
 - [DISPATCH-882](https://issues.apache.org/jira/browse/DISPATCH-882) - router buffers messages for slow presettled receiver
 - [DISPATCH-883](https://issues.apache.org/jira/browse/DISPATCH-883) - Router crashes when it processes management request for connections
 - [DISPATCH-887](https://issues.apache.org/jira/browse/DISPATCH-887) - Dispatch reestablishes connection inspite of deleting the connector
 - [DISPATCH-889](https://issues.apache.org/jira/browse/DISPATCH-889) - linkRoute patterns beginning with #/string match substrings after the / 
 - [DISPATCH-895](https://issues.apache.org/jira/browse/DISPATCH-895) - qpid-dispatch crashes with a SEGFAULT in libqpid-proton
 - [DISPATCH-900](https://issues.apache.org/jira/browse/DISPATCH-900) - Memory leak when repeatedly opening and closing connections
 - [DISPATCH-908](https://issues.apache.org/jira/browse/DISPATCH-908) - Router loses dispositions over receive link on qpid-interop-test 2-node test
 - [DISPATCH-914](https://issues.apache.org/jira/browse/DISPATCH-914) - qd_connector_t leaks mutexes
 - [DISPATCH-920](https://issues.apache.org/jira/browse/DISPATCH-920) - Enabled policy blocks inter-router links