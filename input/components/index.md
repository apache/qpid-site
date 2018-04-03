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
building AMQP applications, and *messaging servers* for deploying AMQP
networks.  You can use them together to build robust distributed
applications.

**Messaging APIs** give your application a tool for efficient,
high-level interprocess communication.

Qpid offers three messaging APIs.
[Qpid Proton]({{site_url}}/proton/index.html) is a reactive API with
full-spectrum AMQP control. In addition to being a messaging API, Qpid
Proton is used by other Qpid components to implement AMQP 1.0 protocol
support.  [Qpid JMS](jms/index.html) is an AMQP-fluent implementation
of the widely used
[Java Message Service](http://en.wikipedia.org/wiki/Java_Message_Service)
API.  The [Qpid Messaging API](messaging-api/index.html) is a
connection-oriented API that supports many languages.

The term "client" is often used to refer to messaging APIs, but some
messaging APIs, such as Qpid Proton, can be used to implement any kind
of messaging component, including clients, servers, bridges, and
proxies.

**Messaging servers** are message-transfer intermediaries that provide
additional behaviors such as store-and-forward for improved
reliability.

The Qpid message brokers are full-featured
[message-oriented middleware](http://en.wikipedia.org/wiki/Message-oriented_middleware)
brokers.  They offer specialized queueing behaviors, message
persistence, and manageability.  Qpid offers pure-Java and native-code
implementations, the [Broker-J](broker-j/index.html) and the
[C++ broker](cpp-broker/index.html).

[Dispatch router](dispatch-router/index.html) is a new kind of
messaging server.  It allows you to build redundant router networks
connecting clients, brokers, and standalone services.

## Messaging APIs

 - [Qpid Proton]({{site_url}}/proton/index.html) - A toolkit allowing any application to speak AMQP
 - [Qpid JMS](jms/index.html) - An AMQP-fluent [Java Message Service](http://en.wikipedia.org/wiki/Java_Message_Service) implementation
 - [Qpid Messaging API](messaging-api/index.html) - A connection-oriented messaging API that supports many languages

## Messaging servers

 - [Broker-J](broker-j/index.html) - A pure-Java AMQP message broker
 - [C++ broker](cpp-broker/index.html) - A native-code AMQP message broker
 - [Dispatch router](dispatch-router/index.html) - An AMQP router for scalable messaging interconnect

## Messaging tools

- [Qpid Interop Test](interop-test/index.html) - An AMQP 1.0 interoperability test suite

## Compatibility

<div class="scroll" markdown="1">

| Component | Languages | Platforms | AMQP versions |
| --------- | --------- | --------- | ------------- |
| [C++ broker]({{site_url}}/components/cpp-broker/index.html) | - | Linux, Windows | 1.0, 0-10 |
| [Dispatch router]({{site_url}}/components/dispatch-router/index.html) | - | Linux | 1.0 |
| [Broker-J]({{site_url}}/components/broker-j/index.html) | - | JVM | 1.0, 0-10, 0-9-1, 0-9, 0-8 |
| [Qpid JMS]({{site_url}}/components/jms/index.html) | Java | JVM | 1.0, 0-10, 0-9-1, 0-9, 0-8 |
| [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html) | C++, Python | Linux, Windows | 1.0, 0-10 |
| [Qpid Proton]({{site_url}}/proton/index.html) | C, C++, Java, Python, Ruby | JVM, Linux, Windows | 1.0 |
| [Qpid Interop Test](interop-test/index.html) | - | Linux | 1.0 |

Any Qpid components that share an AMQP version can interoperate.  For
instance, the brokers are implemented in C++ and Java respectively,
but they do not require C++ or JMS clients for communication.

</div>

;;## Other components
;;
;; - [Qpid Interop Test](interop-test/index.html) - Tests for interoperability of AMQP components
