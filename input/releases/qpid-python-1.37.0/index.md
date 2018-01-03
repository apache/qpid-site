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

# Qpid Python 1.37.0

Qpid Python offers a connection-oriented AMQP messaging API. More
about [Qpid]({{site_url}}/index.html).

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

## Source archives

| Content | Download | Verify |
|---------|----------|--------|
| Qpid Messaging API (Python) | [qpid-python-1.37.0.tar.gz](http://archive.apache.org/dist/qpid/python/1.37.0/qpid-python-1.37.0.tar.gz) | [ASC](https://archive.apache.org/dist/qpid/python/1.37.0/qpid-python-1.37.0.tar.gz.asc), [MD5](https://archive.apache.org/dist/qpid/python/1.37.0/qpid-python-1.37.0.tar.gz.md5), [SHA512](https://archive.apache.org/dist/qpid/python/1.37.0/qpid-python-1.37.0.tar.gz.sha512) |

## Components

| Component | Languages | Platforms | AMQP versions |
|-----------|-----------|-----------|---------------|
| [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html) | Python | Linux, Windows | 0-10 |

## Documentation


<div class="two-column" markdown="1">

 - [Installing Qpid Python](https://git-wip-us.apache.org/repos/asf?p=qpid-python.git;a=blob_plain;f=README.md;hb=HEAD)
 - [Python API reference](messaging-api/api/index.html)
 - [Python examples](messaging-api/examples/index.html)

</div>


## More information

 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+QPID+AND+fixVersion+%3D+%27qpid-python-1.37.0%27+AND+resolution+%3D+%27fixed%27+ORDER+BY+priority+DESC)
 - [Source repository tag](https://git-wip-us.apache.org/repos/asf?p=qpid-python.git;a=tag;h=1.37.0)

<script type="text/javascript">
  _deferredFunctions.push(function() {
      if ("1.37.0" === "{{current_python_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>