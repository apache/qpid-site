#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

from __future__ import print_function

import codecs as _codecs
import fnmatch as _fnmatch
import markdown2 as _markdown2
import os as _os
import re as _re
import runpy as _runpy
import sys as _sys
import tempfile as _tempfile

from collections import defaultdict as _defaultdict
from xml.etree.ElementTree import XML as _XML

try:
    from urllib.request import urlopen as _urlopen
except:
    from urllib2 import urlopen as _urlopen

try:
    from urllib.parse import urlsplit as _urlsplit
except:
    from urlparse import urlsplit as _urlsplit

try:
    from urllib.parse import urljoin as _urljoin
except:
    from urlparse import urljoin as _urljoin

_title_regex = _re.compile(r"<([hH][12]).*?>(.*?)</\1>")
_tag_regex = _re.compile(r"<.+?>")
_page_extensions = ".md", ".html.in", ".html", ".css", ".js"
_buffer_size = 128 * 1024

class Transom:
    def __init__(self, site_url, input_dir, output_dir, home_dir=None):
        self.site_url = site_url
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.home_dir = home_dir

        self.verbose = False

        self.template_path = _join(self.input_dir, "_transom_template.html")
        self.config_path = _join(self.input_dir, "_transom_config.py")

        self.template_content = None
        self.config_env = None
        
        extras = {
            "code-friendly": True,
            "footnotes": True,
            "header-ids": True,
            "markdown-in-html": True,
            "metadata": True,
            "tables": True,
            }

        self.markdown = _markdown2.Markdown(extras=extras)

        self.files = list()
        self.files_by_path = dict()

        self.resources = list()
        self.pages = list()

        self.links = _defaultdict(set)
        self.link_targets = set()

    def init(self):
        if not _is_file(self.template_path):
            if self.home_dir is not None:
                path = _join(self.home_dir, "resources", "template.html")
                self.template_path = path

        if not _is_file(self.template_path):
            raise Exception("No template found")
            
        self.template_content = _read_file(self.template_path)

        init_globals = {"site_url": self.site_url}

        if _is_file(self.config_path):
            self.config_env = _runpy.run_path(self.config_path, init_globals)
        else:
            self.config_env = init_globals

        self.traverse_input_pages("", None)
        self.traverse_input_resources("")

        for file in self.files:
            file.init()

    def render(self):
        for page in self.pages:
            page.load_input()

        for page in self.pages:
            page.convert()

        for page in self.pages:
            page.process()

        for page in self.pages:
            page.render()

        for page in self.pages:
            page.save_output()

        for resource in self.resources:
            resource.save_output()

        if self.home_dir is not None:
            self.copy_default_resources()

    def copy_default_resources(self):
        from_dir = _join(self.home_dir, "resources")
        to_dir = _join(self.output_dir, "transom")
        subpaths = list()

        for root, dirs, files in _os.walk(from_dir):
            dir = root[len(from_dir) + 1:]

            for file in files:
                subpaths.append(_join(dir, file))

        for subpath in subpaths:
            from_file = _join(from_dir, subpath)
            to_file = _join(to_dir, subpath)

            _copy_file(from_file, to_file)

    def check_output_files(self):
        expected_files = set()
        found_files = set()

        for file in self.files:
            expected_files.add(file.output_path)

        self.traverse_output_files("", found_files)

        missing_files = expected_files.difference(found_files)
        extra_files = found_files.difference(expected_files)

        if missing_files:
            print("Missing files:")

            for path in sorted(missing_files):
                print("  {}".format(path))

        if extra_files:
            print("Extra files:")

            for path in sorted(extra_files):
                print("  {}".format(path))

    def traverse_output_files(self, subdir, files):
        output_dir = _join(self.output_dir, subdir)
        names = set(_os.listdir(output_dir))

        for name in names:
            path = _join(subdir, name)
            output_path = _join(self.output_dir, path)

            if _is_file(output_path):
                files.add(output_path)
            elif _is_dir(output_path):
                if name == ".svn":
                    continue

                if name == "transom":
                    continue
                
                self.traverse_output_files(path, files)

    def check_links(self, internal=True, external=False):
        for page in self.pages:
            page.load_output()

        for page in self.pages:
            page.find_links()

        errors_by_link = _defaultdict(list)
        links = self.filter_links(self.links)

        for link in links:
            if internal and link.startswith(self.site_url):
                if link[len(self.site_url):].startswith("/transom"):
                    continue
                
                if link not in self.link_targets:
                    errors_by_link[link].append("Link has no target")

            if external and not link.startswith(self.site_url):
                code, error = self.check_external_link(link)
            
                if code >= 400:
                    msg = "HTTP error code {}".format(code)
                    errors_by_link[link].append(msg)

                if error:
                    errors_by_link[link].append(error.message)

            _sys.stdout.write(".")
            _sys.stdout.flush()

        print()

        for link in errors_by_link:
            print("Link: {}".format(link))

            for error in errors_by_link[link]:
                print("  Error: {}".format(error))

            for source in self.links[link]:
                print("  Source: {}".format(source))

    def filter_links(self, links):
        config_path = _join(self.input_dir, "_transom_ignore_links")

        if _is_file(config_path):
            ignore_patterns = _read_file(config_path).splitlines()

            def retain(link):
                for pattern in ignore_patterns:
                    pattern = pattern.strip()
                    path = link[len(self.site_url) + 1:]

                    if _fnmatch.fnmatch(path, pattern):
                        return False

                return True

            return filter(retain, links)

        return links
                
    def check_external_link(self, link):
        sock, code, error = None, None, None

        try:
            sock = _urlopen(link, timeout=5)
            code = sock.getcode()
        except IOError as e:
            error = e
        finally:
            if sock:
                sock.close()

        return code, error

    def traverse_input_pages(self, subdir, parent_page):
        input_dir = _join(self.input_dir, subdir)
        names = set(_os.listdir(input_dir))

        if "_transom_ignore_pages" in names:
            return

        for name in ("index.md", "index.html", "index.html.in"):
            if name in names:
                names.remove(name)
                parent_page = _Page(self, _join(subdir, name), parent_page)
                break

        for name in sorted(names):
            if name.startswith("_transom_"):
                continue

            if name == ".svn":
                continue

            path = _join(subdir, name)
            input_path = _join(self.input_dir, path)

            if _is_file(input_path):
                if input_path.endswith(".html.in"):
                    ext = ".html.in"
                else:
                    stem, ext = _os.path.splitext(name)

                if ext in _page_extensions:
                    _Page(self, path, parent_page)
            elif _is_dir(input_path):
                self.traverse_input_pages(path, parent_page)

    def traverse_input_resources(self, subdir):
        input_dir = _join(self.input_dir, subdir)
        names = set(_os.listdir(input_dir))

        if "_transom_ignore_resources" in names:
            return

        for name in sorted(names):
            if name.startswith("_transom_"):
                continue

            if name == ".svn":
                continue

            path = _join(subdir, name)
            input_path = _join(self.input_dir, path)

            if _is_file(input_path):
                if path not in self.files_by_path:
                    _Resource(self, path)
            elif _is_dir(input_path):
                self.traverse_input_resources(path)

    def get_url(self, output_path):
        path = output_path[len(self.output_dir) + 1:]
        path = path.replace(_os.path.sep, "/")

        return "{}/{}".format(self.site_url, path)

    def info(self, message, *args):
        if self.verbose:
            print(message.format(*args))

    def warn(self, message, *args):
        message = message.format(*args)
        print("Warning! {}".format(message))

class _File(object):
    def __init__(self, site, path):
        self.site = site
        self.path = path

        self.input_path = _join(self.site.input_dir, self.path)
        self.output_path = _join(self.site.output_dir, self.path)
        self.url = self.site.get_url(self.output_path)

        self.site.files.append(self)
        self.site.files_by_path[self.path] = self

    def init(self):
        self.site.link_targets.add(self.url)

        if self.url.endswith("/index.html"):
            self.site.link_targets.add(self.url[:-10])
            self.site.link_targets.add(self.url[:-11])

    def replace_placeholders(self, content, page_vars):
        out = list()
        tokens = _re.split("({{.+?}})", content)

        for token in tokens:
            if token[:2] != "{{" or token[-2:] != "}}":
                out.append(token)
                continue
            
            token_content = token[2:-2]

            if page_vars and token_content in page_vars:
                out.append(page_vars[token_content])
                continue

            expr = token_content
            env = self.site.config_env
            
            try:
                result = eval(expr, env)
            except Exception as e:
                msg = "Expression '{}'; file '{}'; {}"
                args = expr, self.input_path, e

                print(msg.format(*args))

                out.append(token)
                continue

            if result is not None:
                out.append(str(result))

        return "".join(out)

    def __repr__(self):
        return _format_repr(self, self.path)

class _Resource(_File):
    def __init__(self, site, path):
        super(_Resource, self).__init__(site, path)

        self.site.resources.append(self)

    def save_output(self):
        _copy_file(self.input_path, self.output_path)

class _Page(_File):
    def __init__(self, site, path, parent):
        super(_Page, self).__init__(site, path)

        self.parent = parent

        self.content = None
        self.template_content = None

        self.title = None
        self.attributes = dict()
        
        self.site.pages.append(self)

    def init(self):
        if self.output_path.endswith(".md"):
            self.output_path = "{}.html".format(self.output_path[:-3])
        elif self.output_path.endswith(".html.in"):
            self.output_path = self.output_path[:-3]

        self.url = self.site.get_url(self.output_path)

        super(_Page, self).init()

        self.template_content = self.site.template_content
        
        input_dir, name = _split(self.input_path)
        template_path = _join(input_dir, "_transom_template.html")

        if _is_file(template_path):
            self.template_content = _read_file(template_path)
        
    def load_input(self):
        self.site.info("Loading {}", self)
        self.content = _read_file(self.input_path)

    def save_output(self, path=None):
        self.site.info("Saving {} to {}", self, self.output_path)

        if path is None:
            path = self.output_path

        _write_file(self.output_path, self.content)

    def load_output(self):
        self.content = _read_file(self.output_path)

    def convert(self):
        if self.path.endswith(".md"):
            self.convert_from_markdown()
        elif self.path.endswith(".html.in"):
            self.convert_from_html_in()

    def convert_from_markdown(self):
        self.site.info("Converting {} from markdown", self)

        # Strip out comments
        content_lines = self.content.splitlines()
        content_lines = [x for x in content_lines if not x.startswith(";;")]

        content = _os.linesep.join(content_lines)
        content = self.site.markdown.convert(content)

        self.content = self.apply_template(content)
        self.attributes.update(content.metadata)

    def convert_from_html_in(self):
        self.site.info("Converting {} from html.in", self)
        self.content = self.apply_template(self.content)

    def apply_template(self, content):
        return self.template_content.replace("{{content}}", content)

    def process(self):
        self.site.info("Processing {}", self)

        # Restore previous behavior
        if self.parent is None:
            self.title = "Home"
            return

        dir, name = _split(self.output_path)
        self.title = name

        if isinstance(self.title, bytes):
            self.title = self.title.decode("utf8")

        match = _title_regex.search(self.content)

        if match:
            self.title = match.group(2)

        self.title = _tag_regex.sub("", self.title)
        self.title = self.title.strip()

    def render(self):
        self.site.info("Rendering {}", self)

        page_vars = {
            "title": self.title,
            "path_navigation": self.render_path_navigation(),
            "extra_headers" : self.attributes.get("extra_headers", ""),
        }

        self.content = self.replace_placeholders(self.content, page_vars)

    def render_link(self):
        return u"<a href=\"{}\">{}</a>".format(self.url, self.title)

    def render_path_navigation(self):
        links = list()
        page = self.parent

        links.append(self.title)

        while page:
            links.append(page.render_link())
            page = page.parent

        links = u"".join((u"<li>{}</li>".format(x) for x in reversed(links)))

        return u"<ul id=\"-path-navigation\">{}</ul>".format(links)

    def find_links(self):
        if not self.output_path.endswith(".html"):
            return

        self.site.info("Finding links in {}", self)
        
        try:
            root = self.parse_xml(self.content)
        except Exception as e:
            self.site.warn(str(e))
            return

        links = self.gather_links(root)
        link_targets = self.gather_link_targets(root)

        for link in links:
            if link == "?":
                continue

            scheme, netloc, path, query, fragment = _urlsplit(link)

            if scheme and scheme not in ("file", "http", "https", "ftp"):
                continue

            if netloc in ("issues.apache.org", "bugzilla.redhat.com"):
                continue

            if (fragment and not path) or not path.startswith("/"):
                link = _urljoin(self.url, link)

            self.site.links[link].add(self.url)

        self.site.link_targets.update(link_targets)

    def parse_xml(self, xml):
        try:
            return _XML(xml)
        except Exception as e:
            path = _tempfile.mkstemp(".xml")[1]
            msg = "{} fails to parse; {}; see {}".format(self, str(e), path)

            with _open_file(path, "w") as file:
                file.write(xml)

            raise Exception(msg)

    def gather_links(self, root_elem):
        links = set()

        for elem in root_elem.iter("*"):
            for name in ("href", "src", "action"):
                try:
                    link = elem.attrib[name]
                except KeyError:
                    continue

                links.add(link)

        return links

    def gather_link_targets(self, root_elem):
        link_targets = set()

        for elem in root_elem.iter("*"):
            try:
                id = elem.attrib["id"]
            except KeyError:
                continue

            target = "{}#{}".format(self.url, id)

            if target in link_targets:
                self.site.warn("Duplicate link target in '{}'", target)

            link_targets.add(target)

        return link_targets

_join = _os.path.join
_split = _os.path.split
_is_file = _os.path.isfile
_is_dir = _os.path.isdir

def _make_dir(dir):
    if not _os.path.exists(dir):
        _os.makedirs(dir)

def _open_file(path, mode):
    return _codecs.open(path, mode, "utf8", "replace", _buffer_size)

def _read_file(path):
    with _open_file(path, "r") as file:
        return file.read()

def _write_file(path, content):
    _make_dir(_split(path)[0])

    with _open_file(path, "w") as file:
        return file.write(content)
    
# Adapted from http://stackoverflow.com/questions/22078621/python-how-to-copy-files-fast

_read_flags = _os.O_RDONLY
_write_flags = _os.O_WRONLY | _os.O_CREAT | _os.O_TRUNC
_eof = b""

def _copy_file(src, dst):
    _make_dir(_split(dst)[0])
    
    try:
        fin = _os.open(src, _read_flags)
        fout = _os.open(dst, _write_flags)

        for x in iter(lambda: _os.read(fin, _buffer_size), _eof):
            _os.write(fout, x)
    finally:
        _os.close(fin)
        _os.close(fout)

def _format_repr(obj, *args):
    cls = obj.__class__.__name__
    strings = [str(x) for x in args]
    return "{}({})".format(cls, ",".join(strings))
