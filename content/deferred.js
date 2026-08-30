/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 * 
 *   http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
 */

"use strict";

var _loggingEnabled = true;

function _log(message) {
    if (!_loggingEnabled) {
        return;
    }

    console.log(message);
}

_log("Loading deferred javascript");

/* IE lte 8 */
if (!("trim" in String.prototype)) {
    String.prototype.trim = function() {
        return this.replace(/^\s+|\s+$/g, "");
    }
}

function _getDescendant(elem, path) {
    var names = path.split(".");
    var node = elem;

    for (var i = 0; i < names.length; i++) {
        var elems = node.getElementsByTagName(names[i]);

        if (elems.length === 0) {
            return null;
        }

        node = elems[0];
    }

    return node;
}

function _getText(elem) {
    var child = elem.firstChild;

    while (child) {
        if (child.nodeType === 3 && child.data.trim() !== "") {
            return child.data;
        }

        child = child.nextSibling;
    }

    return null;
}

function _addEventListener(elem, type, listener) {
    if (typeof elem === "string") {
        elem = document.getElementById(elem);
    }

    if (!elem) {
        return;
    }

    _log("Adding event listener " + listener.name + " to " + elem);

    if ("addEventListener" in elem) {
        elem.addEventListener(type, listener, false);
        return;
    }

    if ("attachEvent" in elem) {
        /* IE lte 8 */
        elem.attachEvent("on" + type, listener);
        return;
    }
}

function _getEventTarget(event) {
    if ("target" in event) {
        return event.target;
    } else {
        /* IE lte 8 */
        return event.srcElement;
    }
}

function _preventDefault(event) {
    if (!event) {
        return;
    }

    if ("preventDefault" in event) {
        event.preventDefault();
    } else {
        /* IE lte 8 */
        event.returnValue = false;
    }
}

var _searchIcon = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAgCAYAAABkWOo9AAADfElEQVRYw71YSWgTURgeF1ySybQWF6yCohcFcQG3i1iPgoIm8yZpRexBBJeCB1G7zMzvwQU3vFj14EFRETfQi4LihhYvQl2KWrQKLlVwKeqh2mr8/yaB9s2b5L1kxsKjCXnzvW++//2rlk6nNdmFf4OiDGbrJsRxbdBNxzVM2IyfUzHTXqTVwggVPKWzZTaVJWCuYbmHYwzexZibzrN+GBacoxf5r0S1pXXDY6a7Dwn8KUBQtK5GUlAZOtFo0p6FCj4ugmC/BV/pWoRCVAMYHLOcbXjQLwkyUkobDM7iqgiUKKqwN49CLw3m7jCS9jyd1Y8h56pYBYaebJquM2c97rnj96zO3IdaFQwNhKiRsBcgmV6hchbspztbCBCVq8H934SELWgomWif4zC3TaDiG53Zi1VAR8ZhIhK+IcDqJvVLIopvu0sA/JRMWxQwXgvEOCbAbCE/KIooxUmvyaGX7mIpDjBu9ZYo4nR4nAuTRFFEySs9b27CniDCim45S5DsXw6/kxRXsxB6ovfyw/Mg0yFeq6MeVZOwUIkoBuQqr2mcuiDTXywB0wRRYLcSUTTxVh6EvDboXI24rwbGVbimSvQgZ/auMKofxL3ACfJIzfTMPc0BPAuDKDpsMyfIZzVFmXuRA2gNgyia+hB3zk8lopk6cwDAx3CI8paDdjXTW47N53UK1CHc0QfcObdUw1PKU+lYTiJQktUw2lMSmu5xJaJlNdtH4YM9nFmuBGp2y9koqKRWKKdQJHbbo2pAfQ+1I4LM1125HCLqRC1njSBzdJZalWcD/WWfIrwVI4Epm/P7xTn3utc87omSYqflVEu0Km1UbGuMDZEiWp6CyRTbBP1Os6qZ+pQ0Ya0IL0+b046r1q9d4bPHJh+gF/jbfCnHWQljyRl9cN5LkH6Nz6/TGAzzJZqpyuGuD0AP9U3RBMwUOk28YXzWuz/5KNZFeyIJew5+viSoUfn1loTLlZvefoc1TkCQewVASJn72QNvUv2a/2D4QAX0AOWTMCNbsBdouaEDO5Ap4otLvb3p1Ev29iX19JlaFU76dL+5UHkm732jgRhufFIkyS8qU5KyZNNUylZI+LdoPFQ4fmXmTzslBmQ5U33XLThV7NypPN44yTDdI5QUcnjUtii1v+T5NCkhIlRUZOYA0IL/z+M6gCFpmcyQQrY+oPkXEafv/wAY1thC2lNEvwAAAABJRU5ErkJggg==";

var _selectedSearchIcon = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAgCAYAAABkWOo9AAACrUlEQVRYw73YTYiVVRjA8d9MgzMkCIYJjgNGbRwIx6CZ3IjOvkVMLSY3uZCgMnClKEi0SMU02sxoi1kUFtKHkJuColEpaRNYKtmQH6DjFGQOOYvRGbsuOgNyOO+d99z73hbP7t7/8+ec95zneY5araZsoA3rMYTX8RZ2YBgb0ZXDy8pdUvBZjOAGanXiDj7F0P8qik68i/uLCKbiK3S3XBR9+KUBwYfjbwy3RBTt2IW7JUTKrvRxPFa16ME6CX/H2+jH4+FwLUMvXsPpOv/9CR2ViOI5zBes3CF0ljh4W3C7QHZP06Lh4FxMwK9hU+Y11oNvE6xZ9DYrui8BvoBlDYH/+yw+SDDPor0h0XBPxls+j/6mDgBLcSUhu6NR0eMJ2IFKrhUG8W/EnkJbJkdH4uO/VGU5xNHEQmzIFd2cgLxZafljbSLH/lzRnQlIT+W1mstRjq9zRd+LANMt6X74PMrzc67oxxHg1xaJjkZ5/soV/SICnGuR6PtRnplc0ZEI8EeLROOdm8gV3Zuo60tbIPpjlGc8V3Q4cepfrFhyRaIlHMsVXY65CHKyYtE3EovxQiMl9FQCNFSRZHei8s3i0UZEX0mITjXblQf2lwW96Tm8VLbmPwz8JgH7sEnJl0uMKRdDs/1IWdEnMJMAjeZuU+BtK+AVxQS2Fo0rMXx7AeQ3DJQUXImTBZzJEsJX8SqW1BNtw5kCwFyYm9YVCK4Kp/vPgv9Ph988gxOJHjWO62Hhuoqm0NX4fhHIJH4ICb8L/Wu9xDcxGOV5OjTsi43cV/Bk0fa1Y3fJ2b6pmT70qh8VTL8L8cli39t6nG9Q8FbOKwmewhjuJZ+HSgA68U6JB7KF+AfHGn13whocCUVhgbchd/wdCC8lxzAe7sCz+AyH8XyZR4qM/qAPa2q1mgf+B/5gM0c9BAAAAABJRU5ErkJggg==";

var _menuIcon = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABIElEQVRYw+2WMUqDQRCFB7QJ2dmfFMEmndhFsLO1EQRBJDIzIgim8wCCFsm/LyIIgo1VQASP4FW0tLSyEC+gMjaSI+xabPHV8+3CezPk7lQSqgLuTp0RBtHSjBXzLBhu4uF0092JgmHImr5Yk+cF38EwpKi4zD98wT0FhRYTsHZM7k5BcceKz4zf/8mWrleOz7o1hlWgChCJLAXFKUt6ZsV7Fgyv0XDl7kRRsFOqiIK1QmzptlwVY05dma6zpp8SAo202+TuFKXdZcUjC56yoOlhsY5rDKvAvxHojDDoCjZy0NhkdSHQk/PmLxqZuwAvfUEgtnZcqgmjAkWv4mhpRs3RRY8VHwVe/xYPJmvk7tQXBFbss+AkE3u0heXaA+5Ov5Qac0WEwD/XAAAAAElFTkSuQmCC";

var _selectedMenuIcon = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAzUlEQVRYw+3WMUqDURBF4Q+0S0Ds7cROIZ0rEAQh2GhtOpdhgiAINqkCIriEbCUpU1pZSDZgwtj8L2QFbyxecep7ipk7IyJkoglEBJxgjFklXnHZZTvHL6Iymy7bJCG88A73iQKjMgNTrCsGr/GCXlvDJtAE4ACPWOC7Eis8F4HrxCK6g7dEgRlcYJskcFUG4QafmFfiY3eO2xo2gX8j0D2mg0qc7lfxUbcatbtgiT6MEpvwKfsrHsMxfhLCv3BWBqGPWzxUYojD1gMR4Q/TDLoC9ghWqAAAAABJRU5ErkJggg==";

function _updateGlobalNavigation() {
    _log("Updating global navigation");

    var href = window.location.href;
    var elem = document.getElementById("-global-navigation");
    var child = elem.firstChild;

    if (href.charAt(href.length - 1) === "/") {
        href += "index.html";
    }

    while (child) {
        if (child.nodeType === 1) {
            var link = _getDescendant(child, "a");

            if (link.href === href) {
                child.className += " selected";
                break;
            }
        }

        child = child.nextSibling;
    }

    var link = document.getElementById("-search-link");
    var img = _getDescendant(link, "img");
    img.src = _searchIcon;

    link = document.getElementById("-menu-link");
    img = _getDescendant(link, "img");
    img.src = _menuIcon;
}

function _hideMenu() {
    var menu = document.getElementById("-menu");
    var link = document.getElementById("-menu-link");
    var icon = _getDescendant(link, "img");

    menu.style.display = "none";
    icon.src = _menuIcon;
}

function _hideSearch() {
    var search = document.getElementById("-search");
    var link = document.getElementById("-search-link");
    var icon = _getDescendant(link, "img");

    search.style.display = "none";
    icon.src = _searchIcon;
}

function _toggleMenu() {
    _log("Toggling menu");

    var link = document.getElementById("-menu-link");
    var img = _getDescendant(link, "img");
    var menu = document.getElementById("-menu");

    if (menu.style.display === "none") {
        menu.style.display = "block";
        img.src = _selectedMenuIcon;
        _hideSearch();
    } else {
        _hideMenu();
    }
}

function _toggleSearch() {
    _log("Toggling search");

    var link = document.getElementById("-search-link");
    var img = _getDescendant(link, "img");
    var search = document.getElementById("-search");
    var menu = document.getElementById("-menu");

    if (search.style.display === "none") {
        search.style.display = "block";
        img.src = _selectedSearchIcon;
        _hideMenu();
    } else {
        _hideSearch();
    }
}

function _updatePathNavigation() {
    var elem = document.getElementById("-path-navigation");

    if (!elem) {
        return;
    }

    _log("Updating path navigation");

    var child = elem.firstChild;
    var count = 0;

    while (child) {
        if (child.nodeType === 1) {
            count++;
        }

        child = child.nextSibling;
    }

    if (count >= 3) {
        elem.style.display = "inherit";
    }
}

function _getHeadings() {
    var tags = ["h2", "h3", "h4", "h5", "h6"];
    var headings = [];

    for (var i = 0; i < tags.length; i++) {
        var tag = tags[i];
        var elems = document.getElementsByTagName(tag);

        for (var j = 0; j < elems.length; j++) {
            var elem = elems[j];
            headings.push(elem);
        }
    }

    return headings;
}

function _addHeadingAnchors() {
    _log("Adding heading anchors");

    var headings = _getHeadings();

    for (var i = 0; i < headings.length; i++) {
        var heading = headings[i];
        var id = heading.id;

        if (!id) {
            var docbookAnchor = _getDescendant(heading, "a");

            if (docbookAnchor) {
                id = docbookAnchor.id;
            }
        }

        if (!id) {
            continue;
        }

        var anchor = document.createElement("a");
        anchor.className = "heading-link";
        anchor.href = "#" + id;

        var text = document.createTextNode("\u00a7");
        anchor.appendChild(text);

        heading.appendChild(anchor);
    }
}

function _updateHeadingSelection() {
    var hash = window.location.hash;

    if (!hash) {
        return;
    }

    _log("Updating the selected heading");

    /* Clear any existing selections */

    var headings = _getHeadings();

    for (var i = 0; i < headings.length; i++) {
        var heading = headings[i];

        if (heading.className === "selected") {
            heading.className = "";
        }
    }

    /* Mark the current selection */

    var elem = document.getElementById(hash.substring(1));

    if (!elem) {
        return;
    }

    elem.className = "selected";
}

function _gotoJira(event) {
    _log("Navigating to a jira issue page");

    var form = _getEventTarget(event);
    var jira = form.jira.value;

    jira = jira.trim();

    if (jira.search(/^[A-z]+-/) === -1) {
        jira = "QPID-" + jira;
    }

    var uri = "https://issues.apache.org/jira/browse/" + encodeURIComponent(jira);

    window.location.href = uri;

    _preventDefault(event);
}

function _searchJiras(event) {
    _log("Submitting a jira search query");

    var form = _getEventTarget(event);
    var text = form.text.value;
    var jql = "project in (QPID, QPIDIT, QPIDJMS, PROTON, DISPATCH) and text ~ '{}' order by updatedDate desc";

    text = text.trim();

    if (form.jql) {
        jql = form.jql.value;
    }

    jql = jql.replace("{}", text)

    var uri = "https://issues.apache.org/jira/issues/?jql=" + encodeURIComponent(jql);

    window.location.href = uri;

    _preventDefault(event);
}

function _focusJiraSearchForm() {
    var hash = window.location.hash;

    if (hash !== "#search-issues") {
        return;
    }

    _log("Moving focus to the jira search form");

    var searchForm = document.getElementById("-jira-search-form");

    if (searchForm !== null) {
        searchForm.text.focus();
    }
}

function _normalizeRevision() {
    _log("Normalizing revision string");

    var form = document.getElementById("-viewvc-goto-form");

    form.revision.value = form.revision.value.trim();
}

function _modifyCurrentReleaseLinks() {
    _log("Modifying current release links");

    var elems = document.getElementsByTagName("a");

    for (var i = 0; i < elems.length; i++) {
        var elem = elems[i];

        if (!elem.hasAttribute("href")) {
            continue;
        }

        var href = elem.href;
        var ext = href.substring(href.length - 4)
        var ext7 = href.substring(href.length - 7)

        if (ext === ".asc" || ext7 === ".sha512") {
            href = href.replace("https://archive.apache.org/dist/qpid/",
                                "https://downloads.apache.org/qpid/");
        } else if ((ext === ".zip" || ext7 === ".tar.gz") && href.indexOf("https://archive.apache.org/dist/qpid/") == 0) {
                href = href.replace("https://archive.apache.org/dist/qpid/",
                                    "https://www.apache.org/dyn/closer.lua?filename=qpid/");
                href = href.concat("&action=download");
        } else {
            href = href.replace("https://archive.apache.org/dist/qpid/",
                                "https://www.apache.org/dyn/closer.lua/qpid/");
        }

        elems[i].href = href;
    }
}

function _toggleDiv(toggleInfo) {
    var div = document.getElementById(toggleInfo.divId);
    var control = document.getElementById(toggleInfo.controlId);
    if (div.style.display !== "none") {
	div.style.display = "none";
	control.innerHTML = toggleInfo.showMore;
    } else {
	div.style.display = "block";
	control.innerHTML = toggleInfo.showLess;
    }
}

_updateGlobalNavigation();

_addEventListener("-menu-link", "click", _toggleMenu);
_addEventListener("-search-link", "click", _toggleSearch);

var siteUrl = "";

if (siteUrl === "" || siteUrl.charAt(0) === "/") {
    siteUrl = window.location.protocol + "//" + window.location.host + siteUrl;
}

var path = window.location.href.substring(siteUrl.length);

if (path === "/index.html" || path === "/") {
    var elem = document.getElementById("-apache-navigation");
    elem.style.display = "none";
} else {
    _updatePathNavigation();
    _updateHeadingSelection();
    _addHeadingAnchors();
    _focusJiraSearchForm();

    _addEventListener("-jira-goto-form", "submit", _gotoJira);
    _addEventListener("-jira-search-form", "submit", _searchJiras);
    _addEventListener("-viewvc-goto-form", "submit", _normalizeRevision);

    _addEventListener(window, "hashchange", _updateHeadingSelection);
    _addEventListener(window, "hashchange", _focusJiraSearchForm);
}

_log("Calling deferred functions")

for (var i = 0; i < _deferredFunctions.length; i++) {
    var func = _deferredFunctions[i];
    func();
}
