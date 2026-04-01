class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def check_station(station)->int:
            start_station = station
            tank = 0
            # we need a do-while so this is for the first station
            tank+=gas[station] #fill up gas
            tank -= cost[station]   #deduct cost of moving to next station
            if tank >= 0:
                station+=1  #move to next station
                station = station % len(gas)    #circular circuit
            if station == start_station and tank >= 0:
                return start_station
            while tank > 0:
                print("start is: ", start_station)
                print("tank: ",tank," ,station: ",station)
                tank+=gas[station] #fill up gas
                tank -= cost[station]   #deduct cost of moving to next station
                if tank >= 0:
                    station+=1  #move to next station
                    station = station % len(gas)    #circular circuit
                if station == start_station:
                    print("stopped in while")
                    return start_station
            return -1
        
        # checking for all stations
        for i in range(len(gas)):
            ans = check_station(i)
            if ans != -1:
                return ans
        return -1