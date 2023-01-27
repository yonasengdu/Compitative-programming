class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        left = 0
        right = len(people)-1
        number_of_boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -=1
                number_of_boats += 1
            elif people[right] <= limit:
                right -= 1
                number_of_boats += 1
            else:
                right -= 1
        return number_of_boats
        