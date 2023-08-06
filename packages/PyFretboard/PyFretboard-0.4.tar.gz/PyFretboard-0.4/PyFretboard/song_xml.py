from xml.dom.minidom import parse
from PyFretboard.section import Section, Scale, Chord, Note
from PyFretboard.finger import Finger
from PyFretboard.shape import Shape
from PyFretboard.definitions import PyFretboard as PF

def parse_song_xml(xml_file_path):
    """Parse XML file into Song Object"""
    doc = parse(xml_file_path)
    # get song title
    title = ""
    try:
        title = doc.getElementsByTagName("title")[0].firstChild.data
    except:
        print("No title found")

    # get song author
    author = ""
    try:
        author = doc.getElementsByTagName("author")[0].firstChild.data
    except:
        print("No author found")

    # get all section tags
    secs = []
    sections = doc.getElementsByTagName("section")
    for section in sections:
        s = __parse_section__(section)
        secs.append(s)
    
    return title, author, secs
    
def __parse_section__(section):
    """Parse section tag into Section tag"""
    sec_obj = Section()
    # get section scale
    try:
        scales = section.getElementsByTagName("scale")
        for scale in scales:
            s = __get_scale__(scale)
            sec_obj.add_scale(s)
    except:
        pass

    # get section chords
    try:
        chords = section.getElementsByTagName("chord")
        for chord in chords:
            c = __get_chords__(chord)
            sec_obj.add_chord(c)
    except:
        pass
    return sec_obj

def __get_scale__(element):
    root, type = __get_root_and_type__(element)
    s = Scale(root, type)
    # get shapes
    shapes = element.getElementsByTagName("shape")
    s.shape = __get_shapes__(shapes)
    return s
            

def __get_root_and_type__(element):
    """Get root and type from scale or chord tag"""
    try:
        root = element.getElementsByTagName("root")[0].firstChild.data
        type = element.getElementsByTagName("type")[0].firstChild.data
        return root, type
    except:
        print("No root or type found")

def __get_chords__(chord):
    bass = None
    try:
        root, type = __get_root_and_type__(chord)
        duration = chord.getElementsByTagName("duration")[0].firstChild.data
    except:
        print("Invalid chord tag")
    try:
        bass = chord.getElementsByTagName("bass")[0].firstChild.data
    except:
        pass
    chord_obj = Chord(root, type, int(duration), bass)
    
    # get melodies in chord
    melodies = chord.getElementsByTagName("melody")
    for melody in melodies:
        try:
            melody_id = melody.getAttribute("id")
            notes = melody.getElementsByTagName("note")
            melody_notes = []
            for note in notes:
                n = __get_note__(note)
                melody_notes.append(n)
            chord_obj.add_melody(melody_id, melody_notes)
        except:
            print("Invalid melody tag")

    # get shapes
    shapes = chord.getElementsByTagName("shape")
    chord_obj.shape = __get_shapes__(shapes)
    return chord_obj

def __get_shapes__(shapes):
    sh = {}
    for shape in shapes:
        shape_type = PF.SHAPE_TYPE["ARPEGGIO"]
        try:
            shape_type = (shape.getElementsByTagName("type")[0].firstChild.data).upper()
        except:
            pass
        try:
            shape_id = shape.getAttribute("id")
            fingers = shape.getElementsByTagName("finger")
            all_fingers = []
            for finger in fingers:
                f = __get_finger__(finger)
                all_fingers.append(f)
            sh[shape_id] = Shape(all_fingers, shape_type)
        except:
            print("Invalid shape tag")
    return sh

def __get_finger__(finger):
    pitch = None
    string = None
    fret = None
    function = None
    fingering = ""
    barrel = False
    visual = 0
    try:
        pitch = finger.getElementsByTagName("pitch")[0].firstChild.data
        string = finger.getElementsByTagName("string")[0].firstChild.data
        fret = int(finger.getElementsByTagName("fret")[0].firstChild.data)
        function = finger.getElementsByTagName("function")[0].firstChild.data
    except:
        print("No finger pitch, string, fret or function found")
    try:
        fingering = finger.getElementsByTagName("fingering")[0].firstChild.data
    except:
        pass
    try:
        barrel = finger.getElementsByTagName("barrel")[0].firstChild.data
        barrel = barrel in ['true', 'True', 'TRUE']
    except:
        print("Barrel not found")
    try:
        visual = int(finger.getElementsByTagName("visual")[0].firstChild.data)
    except:
        pass
    return Finger(function=function, string=string, fret=fret, finger=fingering, pitch=pitch, barrel=barrel, visual=visual)


def __get_note__(note):
    try:
        pitch = note.getElementsByTagName("pitch")[0].firstChild.data
        octave = note.getElementsByTagName("octave")[0].firstChild.data
        duration = note.getElementsByTagName("duration")[0].firstChild.data
        return Note(pitch, int(octave), int(duration))
    except:
        print("No note pitch, octave or duration found")
