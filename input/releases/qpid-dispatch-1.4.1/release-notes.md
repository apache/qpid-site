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

# Qpid Dispatch 1.4.1 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [DISPATCH-1148](https://issues.apache.org/jira/browse/DISPATCH-1148) - auth plugin should indicate version in open properties
 - [DISPATCH-1149](https://issues.apache.org/jira/browse/DISPATCH-1149) - authz plugin can no longer override conf file policy
 - [DISPATCH-1151](https://issues.apache.org/jira/browse/DISPATCH-1151) - Revert to gulp version 3 for console build
 - [DISPATCH-1157](https://issues.apache.org/jira/browse/DISPATCH-1157) - auth plugin leaks memory