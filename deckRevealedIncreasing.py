class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """

        size = len(deck)
        if size == 1:
            return deck
        if size == 2:
            return sorted(deck)
        
        deck = sorted(deck)
        p1 = deck[:size/2]
        p2 = deck[size/2:]        
        # print p1, p2

        p2 = self.deckRevealedIncreasing(p2)
        # print p2
        
        if len(p1) < len(p2):
            p1 = p1 + [p2[0]]
            p2 = p2[1:]
            # print p1, p2
        
        newlist = self.twolists(p1, p2)
        return newlist


    def twolists(self, list1, list2):
        newlist = []
        a1 = len(list1)
        a2 = len(list2)

        for i in range(max(a1, a2)):
            if i < a1:
                newlist.append(list1[i])
            if i < a2:
                newlist.append(list2[i])

        return newlist


        