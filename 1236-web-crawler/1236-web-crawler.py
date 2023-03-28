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
        hostName = startUrl.split('/')[2]
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
                if hostName in temp:
                    visited.append(temp)
                    nodes = htmlParser.getUrls(temp)
                    for node in nodes:
                        if node not in visited:
                            q.append(node)
        return visited