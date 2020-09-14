class carFuel():	
    def __init__(self, grade):	
        self.grade = grade	
        self.gallons = 0	
        self.taxes = 0	
        self.amount = 0	

    def fillUp(self, gallons, taxes):	
        self.gallons += gallons	

        if(self.gallons > 0):	
            self.gallons * .076	
            return taxes	

    def drive(self, gallons, ):	
        self.gallons -= gallons