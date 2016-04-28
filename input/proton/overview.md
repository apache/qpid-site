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

# Overview

The goal of Proton is to provide ubiquitous access to a global-scale
interoperable message bus based on AMQP 1.0. At its core Proton
provides three parallel implementations of the AMQP 1.0 protocol, one
in C, one in Java, and one in Javascript. These implementations all
share the same architecture and interface and are rigorously tested
against a single common test suite to guarantee identical
behavior. These three implementations serve as the basis for
delivering protocol access to a wide variety of environments.

The common architecture used by the protocol engines is designed to be
a suitable basis for both high performance-network servers and simple
clients, and to be usable in both threaded and non-threaded
contexts. In short, with the use of binding tools such as SWIG, it is
the goal of Proton to make it trivial for any application to speak
AMQP 1.0 regardless of language, platform, or environment.

 - *Universal* - Proton is designed to scale both up and down. Equally
   suitable for simple clients or high-powered servers, it can be
   deployed in simple peer-to-peer configurations or as part of a
   global federated messaging network.

 - *Embeddable* - Proton is carefully written to be portable and cross
   platform. It has minimal dependencies, and it is architected to be
   usable with any threading model, as well as with non-threaded
   applications. These features make it uniquely suited for embedding
   messaging capabilities into existing software.

 - *Standard* - Built around the AMQP 1.0 messaging standard, Proton
   is not only ideal for building out your own messaging applications
   but also for connecting them to the broader ecosystem of AMQP
   1.0-based messaging applications.
