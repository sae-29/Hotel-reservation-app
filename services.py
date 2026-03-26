from itertools import combinations


class BookingService:
    """
    Core booking algorithm.

    Travel time rules:
      - Horizontal: 1 min per room apart on same floor
      - Vertical:   2 min per floor apart

    Priority:
      1. Same floor → sliding window to find tightest cluster
      2. Multi-floor → minimise (vertical + horizontal) travel time
    """

    def __init__(self, hotel):
        self.hotel = hotel

    # ── public ───────────────────────────────────────────

    def book_rooms(self, n: int):
        available = self.hotel.get_available_rooms()
        if len(available) < n:
            return None

        result = self._same_floor(available, n)
        if result:
            return result

        return self._multi_floor(available, n)

    # ── travel time ──────────────────────────────────────

    @staticmethod
    def travel_time(room_list):
        if not room_list:
            return {"vertical": 0, "horizontal": 0, "total": 0}
        floors = [r["floor"] for r in room_list]
        positions = [r["position"] for r in room_list]
        vertical   = (max(floors) - min(floors)) * 2
        horizontal = max(positions) - min(positions)
        return {
            "vertical": vertical,
            "horizontal": horizontal,
            "total": vertical + horizontal
        }

    # ── same-floor algorithm (sliding window O(n)) ────────

    def _same_floor(self, available, n):
        # Group by floor
        floor_map = {}
        for r in available:
            floor_map.setdefault(r["floor"], []).append(r)

        best_group = None
        min_time   = float("inf")

        for floor_rooms in floor_map.values():
            if len(floor_rooms) < n:
                continue

            floor_rooms.sort(key=lambda x: x["position"])

            for i in range(len(floor_rooms) - n + 1):
                group  = floor_rooms[i : i + n]
                travel = self.travel_time(group)
                t      = travel["total"]

                if t < min_time:
                    min_time   = t
                    best_group = (group, travel)

                if t == 0:          # best possible → early exit
                    return best_group

        return best_group

    # ── multi-floor algorithm ─────────────────────────────

    def _multi_floor(self, available, n):
        # Sort by floor then position for locality
        available.sort(key=lambda x: (x["floor"], x["position"]))

        best_group = None
        min_time   = float("inf")

        # Windowed combinations: only consider windows of nearby rooms
        window = min(len(available), 25)

        for start in range(len(available) - n + 1):
            candidates = available[start : start + window]
            for combo in combinations(candidates, n):
                travel = self.travel_time(list(combo))
                t      = travel["total"]
                if t < min_time:
                    min_time   = t
                    best_group = (list(combo), travel)

            # Once we've scanned past a reasonable cluster, stop
            if start >= 20:
                break

        return best_group

        return best_group
