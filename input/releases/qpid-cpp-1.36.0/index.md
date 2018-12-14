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

# Qpid C++ 1.36.0

Qpid C++ offers a connection-oriented messaging API and a message
broker written in C++ that stores, routes, and forwards messages using
AMQP. More about [Qpid]({{site_url}}/index.html).

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

## Source archives

| Content | Download | Verify |
|---------|----------|--------|
| C++ broker, Qpid Messaging API (C++) | [qpid-cpp-1.36.0.tar.gz](http://archive.apache.org/dist/qpid/cpp/1.36.0/qpid-cpp-1.36.0.tar.gz) | [ASC](https://archive.apache.org/dist/qpid/cpp/1.36.0/qpid-cpp-1.36.0.tar.gz.asc), [MD5](https://archive.apache.org/dist/qpid/cpp/1.36.0/qpid-cpp-1.36.0.tar.gz.md5), [SHA1](https://archive.apache.org/dist/qpid/cpp/1.36.0/qpid-cpp-1.36.0.tar.gz.sha1) |

## Components

| Component | Languages | Platforms | AMQP versions |
|-----------|-----------|-----------|---------------|
| [C++ broker]({{site_url}}/components/cpp-broker/index.html) | C++ | Linux, Windows | 1.0, 0-10 |
| [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html) | C++ | Linux, Windows | 1.0, 0-10 |

## Documentation


<div class="two-column" markdown="1">

 - [Installing Qpid C++](https://gitbox.apache.org/repos/asf?p=qpid-cpp.git;a=blob_plain;f=INSTALL.txt;hb=HEAD)
 - [C++ broker book](cpp-broker/book/index.html) ([PDF](cpp-broker/cpp-broker-book.pdf))
 - [Using the Qpid Messaging API](messaging-api/book/using-the-qpid-messaging-api.html) ([PDF](messaging-api/qpid-messaging-api-book.pdf))
 - [C++ API reference](messaging-api/cpp/api/index.html)
 - [C++ examples](messaging-api/cpp/examples/index.html)

</div>


## More information

 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+QPID+AND+fixVersion+%3D+%27qpid-cpp-1.36.0%27+AND+resolution+%3D+%27fixed%27+ORDER+BY+priority+DESC)
 - [Source repository tag](https://gitbox.apache.org/repos/asf/qpid-cpp.git/tree/refs/tags/1.36.0)

<script type="text/javascript">
  _deferredFunctions.push(function() {
      if ("1.36.0" === "{{current_cpp_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>