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

<script type="text/javascript">
  _deferredFunctions.push(function() {
      if ("0.28" === "{{current_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>

# Qpid 0.28

Qpid is a cross-platform AMQP messaging system.  It provides message
brokers written in C++ and Java, and clients for C++, Java, Perl,
Python, Ruby, and .NET.  More about [Qpid]({{site_url}}/index.html).

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

## Downloads

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

| Content | Download | Signature |
| ------- | -------- | --------- |
| Full source | [qpid-0.28.tar.gz](http://archive.apache.org/dist/qpid/0.28/qpid-0.28.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/0.28/qpid-0.28.tar.gz.asc) |
| C++ broker, Qpid Messaging API (C++, bindings) | [qpid-cpp-0.28.tar.gz](http://archive.apache.org/dist/qpid/0.28/qpid-cpp-0.28.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/0.28/qpid-cpp-0.28.tar.gz.asc) |
| C++ broker command-line tools | [qpid-tools-0.28.tar.gz](http://archive.apache.org/dist/qpid/0.28/qpid-tools-0.28.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/0.28/qpid-tools-0.28.tar.gz.asc) |
| Java broker | [qpid-java-broker-0.28.tar.gz](http://archive.apache.org/dist/qpid/0.28/qpid-java-broker-0.28.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/0.28/qpid-java-broker-0.28.tar.gz.asc) |
| Qpid JMS (AMQP 0-10, 0-91, 0-9, 0-8) | [qpid-java-client-0.28.tar.gz](http://archive.apache.org/dist/qpid/0.28/qpid-java-client-0.28.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/0.28/qpid-java-client-0.28.tar.gz.asc) |
| Qpid JMS (AMQP 1.0) | [qpid-java-amqp-1-0-client-jms-0.28.tar.gz](http://archive.apache.org/dist/qpid/0.28/qpid-java-amqp-1-0-client-jms-0.28.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/0.28/qpid-java-amqp-1-0-client-jms-0.28.tar.gz.asc) |
| Qpid JCA | [qpid-java-0.28.tar.gz](http://archive.apache.org/dist/qpid/0.28/qpid-java-0.28.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/0.28/qpid-java-0.28.tar.gz.asc) |
| Qpid Messaging API (Python) | [qpid-python-0.28.tar.gz](http://archive.apache.org/dist/qpid/0.28/qpid-python-0.28.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/0.28/qpid-python-0.28.tar.gz.asc) |
| Qpid WCF | [qpid-wcf-0.28.zip](http://archive.apache.org/dist/qpid/0.28/qpid-wcf-0.28.zip) | [PGP](http://archive.apache.org/dist/qpid/0.28/qpid-wcf-0.28.zip.asc) |
| QMF | [qpid-qmf-0.28.tar.gz](http://archive.apache.org/dist/qpid/0.28/qpid-qmf-0.28.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/0.28/qpid-qmf-0.28.tar.gz.asc) |

Java artefacts are released as compiled bytecode.  Source code is
available in the full source artefact.

## Components

| Component | Languages | Platforms | AMQP versions |
| --------- | --------- | --------- | ------------- |
| [C++ broker]({{site_url}}/components/cpp-broker/index.html) | C++ | Linux, Windows | 1.0, 0-10 |
| [Java broker]({{site_url}}/components/java-broker/index.html) | Java | JVM | 1.0, 0-10, 0-91, 0-9, 0-8 |
| [Qpid JCA]({{site_url}}/components/qpid-jca/index.html) | Java | JVM | 0-10 |
| [Qpid JMS]({{site_url}}/components/jms/index.html) | Java | JVM | 1.0, 0-10, 0-91, 0-9, 0-8 |
| [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html) | C++, Perl, Python, Ruby, .NET | Linux, Windows | 1.0, 0-10 |
| [Qpid WCF]({{site_url}}/components/qpid-wcf/index.html) | .NET | Windows | 0-10 |
| [QMF]({{site_url}}/components/qmf/index.html) | C++, Python | Linux | 0-10 |

## Documentation

<div class="three-column" markdown="1">

### Installation

 - [Installing Qpid Java](java-broker/book/Java-Broker-Installation.html)
 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/branches/0.28/qpid/cpp/INSTALL)
 - [Installing Qpid Python](http://svn.apache.org/repos/asf/qpid/branches/0.28/qpid/python/README.txt)

### C++ Broker

 - [C++ broker book](cpp-broker/book/index.html) ([PDF](cpp-broker/cpp-broker-book.pdf))

### Java Broker

 - [Java broker book](java-broker/book/index.html) ([PDF](java-broker/java-broker-book.pdf))

### QMF
 
 - [Introduction](cpp-broker/book/ch02s02.html)
 - [C++ API reference](qmf/cpp/api/index.html)
 - [C++ examples](qmf/cpp/examples/index.html)
 - [Python examples](qmf/python/examples/index.html)
 - [Ruby examples](qmf/ruby/examples/index.html)

### Qpid JCA

 - [README](http://svn.apache.org/repos/asf/qpid/branches/0.28/qpid/java/jca/README.txt)
 - [Examples](http://svn.apache.org/repos/asf/qpid/branches/0.28/qpid/java/jca/example/)

### Qpid JMS

 - [API reference](http://docs.oracle.com/javaee/1.4/api/javax/jms/package-summary.html)
 - Using the Qpid JMS client with [AMQP 0-10](programming/book/QpidJMS.html) ([PDF](programming/programming-book.pdf)), or [AMQP 0-91..0-8](jms-client-0-8/book/index.html) ([PDF](jms-client-0-8/jms_client08-book.pdf))
 - Examples for [AMQP 1.0](http://svn.apache.org/repos/asf/qpid/branches/0.28/qpid/java/amqp-1-0-client-jms/example), [AMQP 0-10](qpid-jms/examples/index.html), or  [0-91..0-8](jms-client-0-8/book/JMS-Client-0-8-Examples.html)

### Qpid Messaging API

 - [Using the Qpid Messaging API](programming/book/ch02.html) ([PDF](programming/programming-book.pdf))
 - [The .NET Binding for the C++ Messaging Client](programming/book/ch05.html)
 - [.NET API reference](messaging-api/dotnet/api/index.html)
 - [.NET examples](messaging-api/dotnet/examples/index.html)
 - [C++ API reference](messaging-api/cpp/api/index.html)
 - [C++ examples](messaging-api/cpp/examples/index.html)
 - [Python API reference](messaging-api/python/api/index.html)
 - [Python examples](messaging-api/python/examples/index.html)
 - [Ruby API reference](messaging-api/ruby/api/index.html)
 - [Ruby examples](messaging-api/ruby/examples/index.html)

### Qpid WCF

 - [README](http://svn.apache.org/repos/asf/qpid/branches/0.28/qpid/wcf/ReadMe.txt)
 - [Using the Qpid WCF client](programming/book/QpidWCF.html) ([PDF](programming/programming-book.pdf))
 - [API reference](http://msdn.microsoft.com/en-us/library/vstudio/ms735119\(v=vs.90\).aspx)
 - [Examples](http://svn.apache.org/repos/asf/qpid/branches/0.28/qpid/wcf/samples)

</div>

## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/0.28)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+QPID+AND+fixVersion+in+%28%270.27%27%2C+%270.28%27%29+ORDER+BY+priority+DESC)
 - [Source repository branch](http://svn.apache.org/repos/asf/qpid/branches/0.28)
 - [Source repository tag](http://svn.apache.org/repos/asf/qpid/tags/0.28)