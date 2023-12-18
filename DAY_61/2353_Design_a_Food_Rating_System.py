def __init__(self, foods, cuisines, ratings):
    """
    :type foods: List[str]
    :type cuisines: List[str]
    :type ratings: List[int]
    """
    self.foods=foods
    self.cuisines=cuisines
    self.ratings=ratings
    

def changeRating(self, food, newRating):
    
    for inx in range(len(self.foods)):
        if self.foods[inx]==food:
            self.ratings[inx]=newRating
            break
            


    

def highestRated(self, cuisine):
    
    rating=0
    value=0
    
    for inx in range(len(self.cuisines)):
        if self.cuisines[inx]==cuisine:
            if (rating < self.ratings[inx]):
                rating=self.ratings[inx]
                value=inx
            elif (rating == self.ratings[inx]):
                if self.foods[value] < self.foods[inx]:
                    pass
                else:
                    value=inx
    string= self.foods[value]
    return string
    