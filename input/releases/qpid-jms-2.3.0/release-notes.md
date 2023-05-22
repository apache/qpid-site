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

# Qpid JMS 2.3.0 Release Notes

Qpid JMS is a complete [Jakarta Messaging](https://jakarta.ee/specifications/messaging/) 3.1
client built using the [Qpid Proton]({{site_url}}/proton/index.html) protocol engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [QPIDJMS-584](https://issues.apache.org/jira/browse/QPIDJMS-584) - JMSProducer#send(...body) will NPE when given null Map or byte[] body values
 - [QPIDJMS-588](https://issues.apache.org/jira/browse/QPIDJMS-588) - failover URI with invalid/unused user-info in component URI not rejected, can be logged

## Tasks

 - [QPIDJMS-583](https://issues.apache.org/jira/browse/QPIDJMS-583) - Update to Netty 4.1.92
 - [QPIDJMS-585](https://issues.apache.org/jira/browse/QPIDJMS-585) - update to proton-j 0.34.1