class HotelModel:
    """
    97 rooms across 10 floors.
    Floors 1-9: 10 rooms each (101-110, 201-210, ... 901-910)
    Floor 10:    7 rooms      (1001-1007)
    Lift/stairs on LEFT side → position 1 is closest to lift.
    """

    def __init__(self):
        self._rooms = {}
        self._build()

    def _build(self):
        self._rooms = {}
        # Floors 1–9: 10 rooms each
        for floor in range(1, 10):
            for pos in range(1, 11):
                num = floor * 100 + pos
                self._rooms[num] = {
                    "number": num,
                    "floor": floor,
                    "position": pos,
                    "status": "available"   # available | booked
                }
        # Floor 10: 7 rooms
        for pos in range(1, 8):
            num = 1000 + pos
            self._rooms[num] = {
                "number": num,
                "floor": 10,
                "position": pos,
                "status": "available"
            }

    # ── queries ──────────────────────────────────────────

    def get_all_rooms(self):
        return list(self._rooms.values())

    def get_available_rooms(self):
        return [r for r in self._rooms.values() if r["status"] == "available"]

    def get_state(self):
        rooms = list(self._rooms.values())
        total    = len(rooms)
        booked   = sum(1 for r in rooms if r["status"] == "booked")
        available = total - booked
        return {
            "rooms": rooms,
            "stats": {
                "total": total,
                "booked": booked,
                "available": available,
                "occupancy_pct": round(booked / total * 100, 1)
            }
        }

    # ── mutations ─────────────────────────────────────────

    def mark_booked(self, number: int):
        if number in self._rooms:
            self._rooms[number]["status"] = "booked"

    def reset(self):
        self._build()
