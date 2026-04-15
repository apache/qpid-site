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

# Components

The Qpid project offers two kinds of components, *messaging APIs* for
building AMQP applications, and *messaging server* for deploying AMQP
networks.  You can use them together to build robust distributed
applications.

**Messaging APIs** give your application a tool for efficient,
high-level interprocess communication.

Qpid offers various messaging APIs.
[Qpid Proton]({{site_url}}/proton/index.html) is a reactive API with
full-spectrum AMQP control. In addition to being a messaging API, Qpid
Proton is used by other Qpid components to implement AMQP 1.0 protocol
support.  [Qpid JMS](jms/index.html) is an AMQP-fluent implementation
of the widely used
[Java Message Service](http://en.wikipedia.org/wiki/Java_Message_Service)
API.

The term "client" is often used to refer to messaging APIs, but some
messaging APIs, such as Qpid Proton, can be used to implement any kind
of messaging component, including clients, servers, bridges, and
proxies.

**Messaging servers** are message-transfer intermediaries that provide
additional behaviors such as store-and-forward for improved
reliability.

Qpid [Broker-J](broker-j/index.html) is a full-featured
[message-oriented middleware](http://en.wikipedia.org/wiki/Message-oriented_middleware)
broker, offering specialized queueing behaviors, message persistence, and manageability.

## Messaging APIs

 - [Qpid Proton]({{site_url}}/proton/index.html) - A toolkit allowing any application to speak AMQP
 - [Qpid JMS](jms/index.html) - An AMQP-fluent [Java Message Service](http://en.wikipedia.org/wiki/Java_Message_Service) implementation

## Messaging servers

 - [Broker-J](broker-j/index.html) - A pure-Java AMQP message broker

## Messaging tools

- [Qpid Interop Test](interop-test/index.html) - An AMQP 1.0 interoperability test suite

## Compatibility

<div class="scroll" markdown="1">

| Component | Languages | Platforms | AMQP versions |
| --------- | --------- | --------- | ------------- |
| [Broker-J]({{site_url}}/components/broker-j/index.html) | - | JVM | 1.0, 0-10, 0-9-1, 0-9, 0-8 |
| [Qpid JMS]({{site_url}}/components/jms/index.html) | Java | JVM | 1.0 |
| [Qpid Proton]({{site_url}}/proton/index.html) | C, C++, Java, Python, Ruby | JVM, Linux, Windows | 1.0 |
| [Qpid Interop Test](interop-test/index.html) | - | Linux | 1.0 |

Any Qpid components that share an AMQP version can interoperate.  For
instance, Broker-J is implemented in Java, but can communicate with
C++ clients for communication.

</div>

;;## Other components
;;
;; - [Qpid Interop Test](interop-test/index.html) - Tests for interoperability of AMQP components
