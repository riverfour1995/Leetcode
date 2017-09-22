class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ord_value = [ord(letter) for letter in word]
        if min(ord_value) >= 65 and max(ord_value) <= 90:
            return True
        elif min(ord_value) >= 97 and max(ord_value) <= 122:
            return True
        elif ord_value[0] >= 65 and ord_value[0] <= 90 and min(ord_value[1:]) >= 97 and max(ord_value) <= 122:
            return True
        else:
            return False
