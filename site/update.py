#!/usr/bin/env python3
import time
from pathlib import Path
from typing import NamedTuple

import lxml.etree
import lxml.html
import markdown
import requests

template = (Path(__file__).parent / "template.html").read_text()


def update():
    response = requests.get(
        "https://codeberg.org/hjacobs/mlops-failure-stories/raw/branch/main/README.md",
        timeout=5,
    )
    response.raise_for_status()

    html = markdown.markdown(response.text)

    out = template.replace("{{content}}", html)

    Path("index.html").write_text(out)
    Path("rss.xml").write_bytes(prepare_rss_feed(html))


def prepare_rss_feed(html):
    readme_tree = lxml.html.fromstring(html)

    feed = lxml.etree.Element("rss", attrib={"version": "2.0"})
    channel = lxml.etree.SubElement(feed, "channel")
    channel.append(text_element("title", readme_tree.find("h1").text))
    channel.append(text_element("link", "https://k8s.af/"))
    channel.append(text_element("description", readme_tree.find("p").text))

    for entry in entries_from_etree(readme_tree):
        item = lxml.etree.SubElement(channel, "item")
        item.append(text_element("title", entry.title))
        item.append(text_element("link", entry.url))
        item.append(text_element("description", entry.description))

    return lxml.etree.tostring(
        feed, encoding="utf-8", xml_declaration=True, pretty_print=True
    )


def entries_from_etree(tree):
    entry_nodes = tree.find("ul")
    for entry_node in entry_nodes:
        a = entry_node.find("a")
        props = [n.text for n in entry_node.find("ul")]
        yield Entry(title=a.text, url=a.attrib["href"], description="\n".join(props))


class Entry(NamedTuple):
    title: str
    url: str
    description: str


def text_element(tag, text):
    element = lxml.etree.Element(tag)
    element.text = text
    return element


while True:
    update()
    time.sleep(300)
