class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_map = {}
        left, right = 0, 0
        min_cards = float('inf')

        while right < len(cards):
            if cards[right] not in card_map:
                card_map[cards[right]] = right
                right += 1
            else:
                min_cards = min(min_cards, right - card_map[cards[right]] + 1)
                left = card_map[cards[right]] + 1
                card_map[cards[right]] = right
                right += 1

        return min_cards if min_cards != float('inf') else -1