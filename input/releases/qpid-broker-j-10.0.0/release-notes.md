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

# Qpid Broker-J 10.0.0 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8664](https://issues.apache.org/jira/browse/QPID-8664) - [Broker-J] Remove guava dependency
 - [QPID-8687](https://issues.apache.org/jira/browse/QPID-8687) - [Broker-J] Migrate build process to JDK 17
 - [QPID-8688](https://issues.apache.org/jira/browse/QPID-8688) - [Broker-J] Remove unneeded jaxb dependencies
 - [QPID-8689](https://issues.apache.org/jira/browse/QPID-8689) - [Broker-J] Remove switch for ignoring SNI host errors
 - [QPID-8690](https://issues.apache.org/jira/browse/QPID-8690) - [Broker-J] Remove deprecated AESKeyFileEncrypter
 - [QPID-8694](https://issues.apache.org/jira/browse/QPID-8694) - [Broker-J] BrokerLoggerStatusListener produces repeated stacktraces
 - [QPID-8701](https://issues.apache.org/jira/browse/QPID-8701) - [Broker-J] Remove deprecated authentication providers
 - [QPID-8702](https://issues.apache.org/jira/browse/QPID-8702) - [Broker-J] Log all broker connection attempts
 - [QPID-8703](https://issues.apache.org/jira/browse/QPID-8703) - [Broker-J] Use same javacc plugin for broker-core and query-engine modules
 - [QPID-8707](https://issues.apache.org/jira/browse/QPID-8707) - [Broker-J] Replace deprecated APIs

## Bugs fixed

 - [QPID-8691](https://issues.apache.org/jira/browse/QPID-8691) - [Broker-J] Increased CPU usage during query evaluation
 - [QPID-8700](https://issues.apache.org/jira/browse/QPID-8700) - [Broker-J] NonBlockingConnection#shutdownFinalWrite() may loop infinitely
 - [QPID-8704](https://issues.apache.org/jira/browse/QPID-8704) - [Broker-J] Optimize TaskExecutorImpl subject handling and execution
 - [QPID-8708](https://issues.apache.org/jira/browse/QPID-8708) - [Broker-J] Docker entrypoint script copies links instead of files
 - [QPID-8709](https://issues.apache.org/jira/browse/QPID-8709) - [Broker-J] Docker image 9.2.1-alpine does not contain entrypoint.sh
 - [QPID-8712](https://issues.apache.org/jira/browse/QPID-8712) - [Broker-J] Operation not permitted when building docker image

# Dependency updates

 - [QPID-8684](https://issues.apache.org/jira/browse/QPID-8684) - [Broker-J] Maven plugins and test dependencies updates for version 10.0.0
 - [QPID-8685](https://issues.apache.org/jira/browse/QPID-8685) - [Broker-J] Update to Jetty 12 (12.1.1)
 - [QPID-8686](https://issues.apache.org/jira/browse/QPID-8686) - [Broker-J] Update Apache httpclient to version 5.5
 - [QPID-8693](https://issues.apache.org/jira/browse/QPID-8693) - [Broker-J] Update Apache Derby to version 10.16.1.1
 - [QPID-8696](https://issues.apache.org/jira/browse/QPID-8696) - [Broker-J] Bump caffeine dependency version to 3.2.2
 - [QPID-8697](https://issues.apache.org/jira/browse/QPID-8697) - [Broker-J] Bump fasterxml jackson dependencies versions to 2.20.0
 - [QPID-8698](https://issues.apache.org/jira/browse/QPID-8698) - [Broker-J] Bump bouncycastle dependencies versions to 1.82
 - [QPID-8699](https://issues.apache.org/jira/browse/QPID-8699) - [Broker-J] Bump slf4j / logback dependencies to the versions 2.0.17 / 1.5.18
 - [QPID-8705](https://issues.apache.org/jira/browse/QPID-8705) - [Broker-J] Bump hikaricp dependency to the version 7.0.2
 - [QPID-8710](https://issues.apache.org/jira/browse/QPID-8710) - [Broker-J] Bump asm dependency to the version 9.8
 - [QPID-8711](https://issues.apache.org/jira/browse/QPID-8711) - [Broker-J] Bump commons-cli dependency to the version 1.10.0

