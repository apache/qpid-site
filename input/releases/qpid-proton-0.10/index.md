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
      if ("0.10" === "{{current_proton_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>

# Qpid Proton 0.10

Qpid Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

## Download

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

| Content | Download | Verify |
| ------- | -------- | ------ |
| Qpid Proton | [qpid-proton-0.10.tar.gz](http://archive.apache.org/dist/qpid/proton/0.10/qpid-proton-0.10.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/proton/0.10/qpid-proton-0.10.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/proton/0.10/qpid-proton-0.10.tar.gz.md5), [SHA1](http://archive.apache.org/dist/qpid/proton/0.10/qpid-proton-0.10.tar.gz.sha) |

## Documentation

<div class="two-column" markdown="1">

 - [C API reference](proton/c/api/files.html)
 - [Java API reference](proton/java/api/index.html)
 - [Python tutorial](proton/python/tutorial/tutorial.html)
 - [Python API reference](proton/python/api/index.html)
 - [Python examples](proton/python/examples/index.html)
 - [Installing Qpid Proton](https://git-wip-us.apache.org/repos/asf?p=qpid-proton.git;a=blob_plain;f=INSTALL.md;hb=0.10)

</div>

## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/proton/0.10)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+PROTON+AND+fixVersion+%3D+%270.10%27+ORDER+BY+priority+DESC)
 - [Source repository branch](https://git-wip-us.apache.org/repos/asf?p=qpid-proton.git;a=tree;hb=0.10)
 - [Source repository tag](https://git-wip-us.apache.org/repos/asf?p=qpid-proton.git;a=tag;h=0.10)