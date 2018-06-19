init_code = """
class Instrument:
    def play(self):
        pass

class Guitar(object):
    def __init__(self, name):
        self.name = name

    def play_guitar(self):
        VOWELS = 'aeiou'
        new_music = ''
        for i in self.name.lower():
            if i in VOWELS:
                new_music += '𝄫'
            else:
                new_music += '♮'
        return new_music

class Piano(object):
    def __init__(self, name):
        self.name = name

    def play_piano(self):
        VOWELS = 'aeiou'
        new_music = ''
        for i in self.name.lower():
            if i in VOWELS:
                new_music += '♯'
            else:
                new_music += '♭'
        return new_music

class Violin(object):
    def __init__(self, name):
        self.name = name

    def play_violin(self):
        VOWELS = 'aeiou'
        new_music = ''
        for i in self.name.lower():
            if i in VOWELS:
                new_music += '~'
            else:
                new_music += '♭'
        return new_music

if not "GuitarAdapter" in USER_GLOBAL:
    raise NotImplementedError("Where is 'GuitarAdapter'?")

GuitarAdapter = USER_GLOBAL['GuitarAdapter']

if not "PianoAdapter" in USER_GLOBAL:
    raise NotImplementedError("Where is 'PianoAdapter'?")

PianoAdapter = USER_GLOBAL['PianoAdapter']

if not "ViolinAdapter" in USER_GLOBAL:
    raise NotImplementedError("Where is 'ViolinAdapter'?")

ViolinAdapter = USER_GLOBAL['ViolinAdapter']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}

TESTS = {
    "1. Guitar": [
        prepare_test(middle_code='''song_1 = Guitar("'A thousand years' by Christina Perri")
g_song_1 = GuitarAdapter(song_1)''',
                     test="g_song_1.play()",
                     answer="♮𝄫♮♮♮𝄫𝄫♮𝄫♮♮♮♮𝄫𝄫♮♮♮♮♮♮♮♮♮♮𝄫♮♮𝄫♮𝄫♮♮𝄫♮♮𝄫"),
        prepare_test(middle_code='''song_2 = Guitar("'Skyfall' by Adele")
g_song_2 = GuitarAdapter(song_2)''',
                     test="g_song_2.play()",
                     answer="♮♮♮♮♮𝄫♮♮♮♮♮♮♮𝄫♮𝄫♮𝄫"),
        prepare_test(middle_code='''song_3 = Guitar("'In the end' by Linkin Park")
g_song_3 = GuitarAdapter(song_3)''',
                     test="g_song_3.play()",
                     answer="♮𝄫♮♮♮♮𝄫♮𝄫♮♮♮♮♮♮♮♮𝄫♮♮𝄫♮♮♮𝄫♮♮")
    ],
    "2. Piano": [
        prepare_test(middle_code='''song_4 = Piano("'Time' from Inception by Hans Zimmer")
p_song_4 = PianoAdapter(song_4)''',
                     test="p_song_4.play()",
                     answer="♭♭♯♭♯♭♭♭♭♯♭♭♯♭♭♯♭♭♯♯♭♭♭♭♭♭♯♭♭♭♭♯♭♭♯♭"),
        prepare_test(middle_code='''song_5 = Piano("'My Immortal' by Evanescence")
p_song_5 = PianoAdapter(song_5)''',
                     test="p_song_5.play()",
                     answer="♭♭♭♭♯♭♭♯♭♭♯♭♭♭♭♭♭♯♭♯♭♯♭♭♯♭♭♯"),
        prepare_test(middle_code='''song_6 = Piano("'When you gone' by Avril Lavigne")
p_song_6 = PianoAdapter(song_6)''',
                     test="p_song_6.play()",
                     answer="♭♭♭♯♭♭♭♯♯♭♭♯♭♯♭♭♭♭♭♯♭♭♯♭♭♭♯♭♯♭♭♯")
    ],
    "3. Violin": [
        prepare_test(middle_code='''song_7 = Violin("'Who wants to live forever' by Queen")
v_song_7 = ViolinAdapter(song_7)''',
                     test="v_song_7.play()",
                     answer="♭♭♭~♭♭~♭♭♭♭♭~♭♭~♭~♭♭~♭~♭~♭♭♭♭♭♭♭~~~♭"),
        prepare_test(middle_code='''song_8 = Violin("'Space Oddity' by David Bowie")
v_song_8 = ViolinAdapter(song_8)''',
                     test="v_song_8.play()",
                     answer="♭♭♭~♭~♭~♭♭~♭♭♭♭♭♭♭♭~♭~♭♭♭~♭~~"),
        prepare_test(middle_code='''song_9 = Violin("'Lilium' by Elfen Lied")
v_song_9 = ViolinAdapter(song_9)''',
                     test="v_song_9.play()",
                     answer="♭♭~♭~~♭♭♭♭♭♭~♭♭~♭♭♭~~♭"),
    ]

}
