class RulerMeasurement:
    Measurement = 0.0
    units = "cm"

#returns a measurement by reading the ruler
	#define enum based on whether we're working in inches or cm
    def ReadMeasurement(Camera):
        Measurement = 0.0
        units = FindUnits(Camera)
        Markings = CountMarkings(Camera)
        for i in range(Markings):
            if (units == "inches"):
                Measurement += 1/16
            elif (units == "cm"):
                Measurement += 0.1
        return Measurement

    def CountMarkings(Camera):
        NumberofMarkings = 0
#insert code to find nearest marked number and then count tick marks up to red dot
        return NumberofMarkings

    def FindUnits(Camera):
	#For now, default to cm
	#later, can use algorithm based on spacing of markings
        units = "cm"
        return units

