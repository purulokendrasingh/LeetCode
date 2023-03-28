# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        temp = startUrl.replace('http://', '')
        hostName = 'http://' + temp[:temp.index('/')] if '/' in temp else startUrl
        print(hostName)
        visited = []
        q = deque()
        q.append(startUrl)
        while q:
            count = len(q)
            for _ in range(count):
                temp = q.popleft()
                if temp in visited:
                    continue
                if temp.startswith(hostName):
                    visited.append(temp)
                    nodes = htmlParser.getUrls(temp)
                    for node in nodes:
                        if node not in visited:
                            q.append(node)
        return visited