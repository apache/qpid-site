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

# Qpid JMS AMQP 0-x 6.4.0 Release Notes

Qpid JMS AMQP 0-x is JMS 1.1 compatible client which can speak AMQP 0-8,0-9,0-9-1 and 0-10.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPID-8440](https://issues.apache.org/jira/browse/QPID-8440) - [JMS AMQP 0-x] Add support for user defined extensions to override client settings
 - [QPID-8441](https://issues.apache.org/jira/browse/QPID-8441) - [JMS AMQP 0-x] Add connection options to override keystore and truststore types 
 - [QPID-8446](https://issues.apache.org/jira/browse/QPID-8446) - [JMS AMQP 0-x] Add ability to notify messaging application about the result of every connectivity attempt

## Tasks

 - [QPID-8443](https://issues.apache.org/jira/browse/QPID-8443) - [JMS AMQP 0-x] Upgrade slf4j dependency to the latest version
 - [QPID-8444](https://issues.apache.org/jira/browse/QPID-8444) - [JMS AMQP 0-x] Upgrade logback dependency to the latest version