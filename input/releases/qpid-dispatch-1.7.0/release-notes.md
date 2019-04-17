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

# Qpid Dispatch 1.7.0 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1313](https://issues.apache.org/jira/browse/DISPATCH-1313) - Allow configuration of optional policy-vhost in listeners so different listeners can enforce different policies

## Bugs fixed

 - [DISPATCH-1270](https://issues.apache.org/jira/browse/DISPATCH-1270) - Inapropriate use of CLOCK_REALTIME for periodic timer
 - [DISPATCH-1302](https://issues.apache.org/jira/browse/DISPATCH-1302) - Large messages sent pre-settled may arrive unsettled and never get settled by the sender 
 - [DISPATCH-1304](https://issues.apache.org/jira/browse/DISPATCH-1304) - Authz self test fails with python 3
 - [DISPATCH-1305](https://issues.apache.org/jira/browse/DISPATCH-1305) - Fix flake8 warnings in system_tests_policy
 - [DISPATCH-1306](https://issues.apache.org/jira/browse/DISPATCH-1306) - [tools] Scraper does not account for changes to log format
 - [DISPATCH-1309](https://issues.apache.org/jira/browse/DISPATCH-1309) - Various crashes in 1.6 release
 - [DISPATCH-1314](https://issues.apache.org/jira/browse/DISPATCH-1314) - spurious error in log when using healthz or metrics
 - [DISPATCH-1315](https://issues.apache.org/jira/browse/DISPATCH-1315) - attempt to wake a deleted http connection
 - [DISPATCH-1316](https://issues.apache.org/jira/browse/DISPATCH-1316) - race in remote_sasl can cause use after free
 - [DISPATCH-1319](https://issues.apache.org/jira/browse/DISPATCH-1319) - Coverity issues on master branch