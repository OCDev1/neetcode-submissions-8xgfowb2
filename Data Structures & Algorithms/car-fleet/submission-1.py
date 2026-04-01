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
            cur_time = (target - pos)/spd
            if cur_time > time_to_target:
                fleet += 1
                time_to_target = cur_time # move to check next fleet (every car before it can only catch up to it and then drive at the same speed as the car ahead of it.)
        
        return fleet


        
        return fleet
