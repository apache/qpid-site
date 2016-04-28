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
      if ("0.34" === "{{current_cpp_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>

# Qpid C++ 0.34

A connection-oriented messaging API that supports many languages and
platforms. A message-oriented middleware message broker written in C++
that stores, routes, and forwards messages using AMQP. More about [Qpid]({{site_url}}/index.html).

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

## Source archives

| Content | Download | Verify |
| ------- | -------- | ------ |
| C++ broker, Qpid Messaging API (C++, bindings) | [qpid-cpp-0.34.tar.gz](http://archive.apache.org/dist/qpid/0.34/qpid-cpp-0.34.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/0.34/qpid-cpp-0.34.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/0.34/qpid-cpp-0.34.tar.gz.md5), [SHA1](http://archive.apache.org/dist/qpid/0.34/qpid-cpp-0.34.tar.gz.sha1) |

## Components

| Component | Languages | Platforms | AMQP versions |
| --------- | --------- | --------- | ------------- |
| [C++ broker]({{site_url}}/components/cpp-broker/index.html) | C++ | Linux, Windows | 1.0, 0-10 |
| [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html) | C++, Perl, Python, Ruby, .NET | Linux, Windows | 1.0, 0-10 |

## Documentation

 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/tags/qpid-cpp-0.34/qpid/cpp/INSTALL)
 - [C++ broker book](cpp-broker/book/index.html) ([PDF](cpp-broker/cpp-broker-book.pdf))
 - See the [Messaging API]({{site_url}}/components/messaging-api/index.html#documentation) page for relevant documentation.

## More information

 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+QPID+AND+fixVersion+%3D+%27qpid-cpp-0.34%27+ORDER+BY+priority+DESC)
 - [Source repository tag](http://svn.apache.org/repos/asf/qpid/tags/qpid-cpp-0.34)