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

# Qpid Dispatch 0.6.1 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-367](https://issues.apache.org/jira/browse/DISPATCH-367) - balanced distribution needs to be more... balanced.

## Bugs fixed

 - [DISPATCH-341](https://issues.apache.org/jira/browse/DISPATCH-341) - router did not respond to request to drain a message-routed consumers link credit
 - [DISPATCH-364](https://issues.apache.org/jira/browse/DISPATCH-364) - Inter-router listeners should not permit normal endpoint traffic
 - [DISPATCH-365](https://issues.apache.org/jira/browse/DISPATCH-365) - Standalone router crashes if an interior router attempts to connect to it
 - [DISPATCH-366](https://issues.apache.org/jira/browse/DISPATCH-366) - When delivery fails the router sends the RELEASED disposition, not MODIFIED
 - [DISPATCH-387](https://issues.apache.org/jira/browse/DISPATCH-387) - Router core dumps with misbehaving client
 - [DISPATCH-443](https://issues.apache.org/jira/browse/DISPATCH-443) - Reverse name lookup on listener connections can hang the entire router
 - [DISPATCH-460](https://issues.apache.org/jira/browse/DISPATCH-460) - Regression: Link-routed dynamic sources don't work

## Tasks

 - [DISPATCH-410](https://issues.apache.org/jira/browse/DISPATCH-410) - console build fixups