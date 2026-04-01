class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        # IMPORTANT: A car can not pass another car ahead of it.
        # It can only catch up to another car and then drive at the same speed as the car ahead of it.

        # sort by position
        for i in range(len(speed)):
            cars.append([position[i], speed[i]])
        cars.sort(reverse = True)

        fleet = 0
        time_to_target = 0  # leading car's time to target

        for pos,spd in cars:
            # car[i]'s time to target
            cur_time = (target - pos)/spd   # how many time units until current car reaches destination
            if cur_time > time_to_target:   # if cur car is slower it is a seperate fleet, if not then they will arrive together beacuse it cant pass the first car.
                fleet += 1
                time_to_target = cur_time # if cur is slower the first one then the one behind cur can only catch up to it and then drive at the same speed as cur.
        
        return fleet
