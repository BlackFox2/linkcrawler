from urllib import request
from urllib import parse
import re

from link_object import LinkObject


class LinkCrawler:
    def __init__(self, starting_url):
        parsed_url = parse.urlparse(starting_url)
        self.scheme = parsed_url.scheme
        self.netloc = parsed_url.netloc
        self.starting_url = starting_url


    def grab_links(self, html_code):
        get_links = re.compile(b'<a\s+(?:[^>]*?\s+)?href="([^"]*)"[^>]*>')
        result = get_links.findall(html_code)   # result = [content von <a...>]
        return result


    def get_page(self, url):
        response = request.urlopen(url)
        return response.read()

    def get_links(self, url):
        link_object = LinkObject(self.starting_url)
        html_code = self.get_page(self.starting_url)
        links = self.grab_links(html_code)
        result = []
        for link in links:
            href = link.decode('iso-8859-1')
            if len(href) > 1 and href[0] == '/' and href[1] != '/':
                href = self.netloc + href
            if self.netloc in href:
                result.append(href)
        link_object.subsequent = result
        return link_object

    def get_links_from_object(self, link_object):
        link_objects = []
        for link in link_object.subsequent:
            link_objects.append(self.get_links(link))
        return link_objects

    def start_analyisis(self):
        stages = []
        stage_one = [self.get_links(self.starting_url)]
        stages.append(stage_one)
        depth = 50
        while depth > 0:
            new_link_objects = []
            for link_object in stages[-1]:
                new_link_objects.append(self.get_links_from_object(link_object))
            stages.append(new_link_objects)
