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
      if ("0.30" === "{{current_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>

# Qpid 0.30

Qpid is a cross-platform AMQP messaging system.  It provides message
brokers written in C++ and Java, and clients for C++, Java, Perl,
Python, Ruby, and .NET.  More about [Qpid]({{site_url}}/index.html).

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

## Source archives

| Content | Download | Verify |
| ------- | -------- | ------ |
| C++ broker, Qpid Messaging API (C++, bindings) | [qpid-cpp-0.30.tar.gz](http://archive.apache.org/dist/qpid/0.30/qpid-cpp-0.30.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/0.30/qpid-cpp-0.30.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/0.30/qpid-cpp-0.30.tar.gz.md5), [SHA1](http://archive.apache.org/dist/qpid/0.30/qpid-cpp-0.30.tar.gz.sha1) |
| C++ broker command-line tools | [qpid-tools-0.30.tar.gz](http://archive.apache.org/dist/qpid/0.30/qpid-tools-0.30.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/0.30/qpid-tools-0.30.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/0.30/qpid-tools-0.30.tar.gz.md5), [SHA1](http://archive.apache.org/dist/qpid/0.30/qpid-tools-0.30.tar.gz.sha1) |
| Java broker, Qpid JMS, Qpid JCA | [qpid-java-0.30.tar.gz](http://archive.apache.org/dist/qpid/0.30/qpid-java-0.30.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/0.30/qpid-java-0.30.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/0.30/qpid-java-0.30.tar.gz.md5), [SHA1](http://archive.apache.org/dist/qpid/0.30/qpid-java-0.30.tar.gz.sha1) |
| Qpid Messaging API (Python) | [qpid-python-0.30.tar.gz](http://archive.apache.org/dist/qpid/0.30/qpid-python-0.30.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/0.30/qpid-python-0.30.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/0.30/qpid-python-0.30.tar.gz.md5), [SHA1](http://archive.apache.org/dist/qpid/0.30/qpid-python-0.30.tar.gz.sha1) |

## Java binaries

| Content | Download | Verify |
| ------- | -------- | ------ |
| Java broker | [qpid-broker-0.30-bin.tar.gz](http://archive.apache.org/dist/qpid/0.30/binaries/qpid-broker-0.30-bin.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/0.30/binaries/qpid-broker-0.30-bin.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/0.30/binaries/qpid-broker-0.30-bin.tar.gz.md5), [SHA1](http://archive.apache.org/dist/qpid/0.30/binaries/qpid-broker-0.30-bin.tar.gz.sha1) |
| Qpid JMS (AMQP 1.0) | [qpid-amqp-1-0-client-jms-0.30-bin.tar.gz](http://archive.apache.org/dist/qpid/0.30/binaries/qpid-amqp-1-0-client-jms-0.30-bin.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/0.30/binaries/qpid-amqp-1-0-client-jms-0.30-bin.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/0.30/binaries/qpid-amqp-1-0-client-jms-0.30-bin.tar.gz.md5), [SHA1](http://archive.apache.org/dist/qpid/0.30/binaries/qpid-amqp-1-0-client-jms-0.30-bin.tar.gz.sha1) |
| Qpid JMS (AMQP 0-10, 0-9-1, 0-9, 0-8) | [qpid-client-0.30-bin.tar.gz](http://archive.apache.org/dist/qpid/0.30/binaries/qpid-client-0.30-bin.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/0.30/binaries/qpid-client-0.30-bin.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/0.30/binaries/qpid-client-0.30-bin.tar.gz.md5), [SHA1](http://archive.apache.org/dist/qpid/0.30/binaries/qpid-client-0.30-bin.tar.gz.sha1) |

## Components

| Component | Languages | Platforms | AMQP versions |
| --------- | --------- | --------- | ------------- |
| [C++ broker]({{site_url}}/components/cpp-broker/index.html) | C++ | Linux, Windows | 1.0, 0-10 |
| [Java broker]({{site_url}}/components/java-broker/index.html) | Java | JVM | 1.0, 0-10, 0-9-1, 0-9, 0-8 |
| [Qpid JMS]({{site_url}}/components/jms/index.html) | Java | JVM | 1.0, 0-10, 0-9-1, 0-9, 0-8 |
| [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html) | C++, Perl, Python, Ruby, .NET | Linux, Windows | 1.0, 0-10 |

## Documentation

<div class="two-column" markdown="1">
<div class="column" markdown="1">

### Installation

 - [Installing Qpid Java](java-broker/book/Java-Broker-Installation.html)
 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/branches/0.30/qpid/cpp/INSTALL)
 - [Installing Qpid Python](http://svn.apache.org/repos/asf/qpid/branches/0.30/qpid/python/README.txt)

### C++ Broker

 - [C++ broker book](cpp-broker/book/index.html) ([PDF](cpp-broker/cpp-broker-book.pdf))

### Java Broker

 - [Java broker book](java-broker/book/index.html) ([PDF](java-broker/java-broker-book.pdf))

### Qpid JCA

 - [README](http://svn.apache.org/repos/asf/qpid/branches/0.30/qpid/java/jca/README.txt)
 - [Examples](http://svn.apache.org/repos/asf/qpid/branches/0.30/qpid/java/jca/example/)

</div>
<div class="column" markdown="1">

### Qpid JMS

 - [API reference](http://docs.oracle.com/javaee/1.4/api/javax/jms/package-summary.html)
 - [Using the Qpid JMS client (AMQP 0-10)](programming/book/QpidJMS.html) ([PDF](programming/programming-book.pdf))
 - [Using the Qpid JMS client (AMQP 0-9-1, 0-9, 0-8)](jms-client-0-8/book/index.html) ([PDF](jms-client-0-8/jms_client08-book.pdf))
 - [Examples (AMQP 1.0)](http://svn.apache.org/repos/asf/qpid/branches/0.30/qpid/java/amqp-1-0-client-jms/example)
 - [Examples (AMQP 0-10)](qpid-jms/examples/index.html)
 - [Examples (AMQP 0-9-1, 0-9, 0-8)](jms-client-0-8/book/JMS-Client-0-8-Examples.html)

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

</div>
</div>

## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/0.30)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+QPID+AND+fixVersion+in+%28%270.29%27%2C+%270.30%27%29+ORDER+BY+priority+DESC)
 - [Source repository branch](http://svn.apache.org/repos/asf/qpid/branches/0.30)
 - [Source repository tag](http://svn.apache.org/repos/asf/qpid/tags/0.30)
