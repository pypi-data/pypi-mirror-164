class Finger:
    # TODO: Move all definitions to definitions file!
    NOTES7 = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    NOTES = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'Fb': 4, 'E#': 5, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A':9, 'A#': 10, 'Bb': 10, 'B': 11, 'Cb': 11, 'B#': 0}
    INTERVALS = {'1': 0, 'b2': 1, 'b9': 1, '2': 2, '9': 2, '#9': 3, '#2': 3, 'b3': 3, '3': 4, '#3': 5, 'b4': 4, 'b11': 4, '4': 5, '11': 5, '#4': 6, '#11': 6, 'b5': 6, '5': 7, '#5': 8, 'b6': 8, 'b13': 8, '6': 9, '13': 9, '#6': 10, '#13': 10, 'b7': 10, '7': 11, 'b9': 12, '9': 13, '#9': 14, 'b11': 14, '11': 15, '#11': 16, 'b13': 16, '13': 17, '#13': 18}
    SEMITONE_TO_PITCH = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']
    guitar_strings = ['e', 'B', 'G', 'D', 'A', 'E']
    strings_semitones = [24, 19, 15, 10, 5, 0]

    def __init__(self, function, string, fret, finger="", pitch=None, barrel=False, visual=0):
        self.function = function
        self.string = string
        self.fret = fret
        self.finger = finger
        self.barrel = barrel
        self.visual = visual
        if pitch is None:
            self.pitch = self.__finger_to_pitch__()
        else:
            self.pitch = pitch
        self.octave = self.__finger_to_octave__()
        
        
    def __finger_to_pitch__(self):
        return Finger.SEMITONE_TO_PITCH[(Finger.strings_semitones[Finger.guitar_strings.index(self.string)] + self.fret + 4) % 12]
    
    def __finger_to_octave__(self):
        return (Finger.strings_semitones[Finger.guitar_strings.index(self.string)] + self.fret + 4) // 12
        

    def dist(self, f):
        s_num = Finger.guitar_strings.index(self.string)
        f_num = Finger.guitar_strings.index(f.string)
        return (Finger.strings_semitones[s_num] + self.fret) - (Finger.strings_semitones[f_num] + f.fret)
    
    def to_xml(self):
        return "     <finger>\n      <pitch>{}</pitch>\n      <string>{}</string>\n      <fret>{}</fret>\n      <function>{}</function>\n      <fingering>{}</fingering>\n      <barrel>False</barrel>\n      <visual>{}</visual>\n     </finger>".format(self.pitch, self.string, self.fret, self.function, self.finger, self.visual)
        
    def __eq__(self, f):
        return self.fret == f.fret and self.string == f.string and self.finger == f.finger

    def __str__(self):
        return "{} ({}) --> [{}/{}]({})".format(self.pitch, self.function, self.string, self.fret, self.finger)
