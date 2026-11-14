class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)

        citation_counts = [0] * (n + 1)

        for citation in citations:
            if citation >= n:
                # n + 1 index counts papers with n citations or more
                citation_counts[n] += 1
            else:
                citation_counts[citation] += 1

        eligible_papers = 0
        for h in range(n, -1, -1):
            eligible_papers += citation_counts[h]
            if eligible_papers >= h:
                return h

        return 0