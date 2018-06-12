init_code = """
if not "Guitar" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Guitar'?")

Guitar = USER_GLOBAL['Guitar']

if not "Drums" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Drums'?")

Drums = USER_GLOBAL['Drums']

if not "Piano" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Piano'?")

Piano = USER_GLOBAL['Piano']

if not "Flute" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Flute'?")

Flute = USER_GLOBAL['Flute']

if not "Digital" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Digital'?")

Digital = USER_GLOBAL['Digital']

if not "GuitarAdapter" in USER_GLOBAL:
    raise NotImplementedError("Where is 'GuitarAdapter'?")

GuitarAdapter = USER_GLOBAL['GuitarAdapter']

if not "DrumsAdapter" in USER_GLOBAL:
    raise NotImplementedError("Where is 'DrumsAdapter'?")

DrumsAdapter = USER_GLOBAL['DrumsAdapter']

if not "PianoAdapter" in USER_GLOBAL:
    raise NotImplementedError("Where is 'PianoAdapter'?")

PianoAdapter = USER_GLOBAL['PianoAdapter']

if not "FluteAdapter" in USER_GLOBAL:
    raise NotImplementedError("Where is 'FluteAdapter'?")

FluteAdapter = USER_GLOBAL['FluteAdapter']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="\n", show_code=None):
    if show_code is None:
        show_code = middle_code + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}

TESTS = {
    "Instruments": [
        prepare_test(test="Guitar().play_guitar()",
                     answer="guitar music"),
        prepare_test(test="Drums().play_drums()",
                     answer="drums music"),
        prepare_test(test="Piano().play_piano()",
                     answer="piano music"),
        
        prepare_test(test="Flute().play_flute()",
                     answer="flute music"),
        prepare_test(test="Digital().play_digital()",
                     answer="digital music"),
        prepare_test(test="GuitarAdapter().play_digital()",
                     answer="guitar music"),

        prepare_test(test="DrumsAdapter().play_digital()",
                     answer="drums music"),
        prepare_test(test="PianoAdapter().play_digital()",
                     answer="piano music"),
        prepare_test(test="FluteAdapter().play_digital()",
                     answer="flute music")
    ]

}
