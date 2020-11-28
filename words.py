import random
print('If you dont know say n')

words = ['Abate', 'Aberrant', 'Abeyance', 'Abscond', 'Abstemious', 'Admonish', 'Adulterate', 'Aesthetic', 'Aggregate', 'Alacrity', 'Alleviate', 'Amalgamate', 'Ambiguous', 'Ambivalence', 'Ameliorate', 'Anachronism', 'Analogous', 'Anarchy', 'Anomalous', 'Antipathy', 'Apathy', 'Appease', 'Apprise', 'Approbation', 'Appropriate', 'Arduous', 'Artless', 'Ascetic', 'Assiduous', 'Assuage', 'Attenuate', 'Audacious', 'Austere', 'Autonomous', 'Aver', 'Banal', 'Belie', 'Beneficent', 'Bolster', 'Bombastic', 'Boorish', 'Burgeon', 'Burnish', 'Buttress', 'Capricious', 'Castigation', 'Catalyst', 'Caustic', 'Chicanery', 'Coagulate', 'Coda', 'Cogent', 'Commensurate', 'Compendium', 'Complaisant', 'Compliant', 'Conciliatory', 'Condone', 'Confound', 'Connoisseur', 'Contention', 'Contentious', 'Contrite', 'Conundrum', 'Converge', 'Convoluted', 'Craven', 'Daunt', 'Decorum', 'Default', 'Deference', 'Delineate', 'Denigrate', 'Deride', 'Derivative', 'Desiccate', 'Desultory', 'Deterrent', 'Diatribe', 'Dichotomy', 'Diffidence', 'Diffuse', 'Digression', 'Dirge', 'Disabuse', 'Discerning', 'Discordant', 'Discredit', 'Discrepancy', 'Discrete', 'Disingenuous', 'Disinterested', 'Disjointed', 'Dismiss', 'Disparage', 'Disparate', 'Dissemble', 'Disseminate', 'Dissolution', 'dissonance', 'distend', 'intimate', 'maintain', 'aboveboard', 'amorous', 'egoist', 'egotist', 'obnoxious', 'alltruist', 'propriety', 'ambivert', 'cynical', 'embitter', 'misaanthrope', 'misogynist', 'misogamist', 'excursions', 'morbid', 'profanity', 'altercation', 'alterego', 'loquacious', 'spartan', 'reticent', 'salutary', 'ephemeral', 'transient', 'inclement', 'mollifying', 'placating', 'enervating', 'sporadic', 'imperceptible', 'granular', 'delegate', 'shirk', 'amenable', 'consummate', 'protean', 'revelry', 'wallowed', 'amiability', 'conservatism', 'carousing', 'lamentable', 'piecemeal', 'hackneyed', 'edifice', 'indulgent', 'fleeting', 'languish', 'serendipitous', 'debonairness', 'modicum', 'wherewithal', 'brash', 'embellish', 'hindsight', 'pauper', 'curmudgeon', 'steadfast', 'roundabout', 'refunctory', 'brusque', 'unseemly', 'enumerate', 'skewered', 'ineptitude', 'polemic', 'churlish', 'surly', 'inhibited', 'overseer', 'martinet', 'veritable', 'tapestry', 'cosmopolitan', 'polyglot', 'populace', 'dissemble', 'mince', 'apolmb', 'dissimilitude', 'histrionic', 'prevarication ', 'shunned', 'rambling', 'labyrinthine', 'aphorisms', 'terse', 'contemporary', 'ignominy', 'amiable', 'melancholia', 'protracted', 'forlorn', 'ostentatious', 'gregarious', 'contingent', 'whimsical', 'idolatrous', 'diva', 'myriad', 'exaltation', 'notoriety', 'finesse', 'affront', 'endearing', 'fortuitous', 'precipitate', 'coyly', 'albeit', 'posthumously', 'hapless', 'preeminent ,sycophantic', 'detractors', 'obscure', 'congenial', 'prolific', 'amenable', 'maladroit', 'adroit', 'malign', 'magnanimous', 'animous', 'erudite', 'ponderous', 'prodigal', 'prodigious', 'lambast', 'doleful', 'cupidity', 'verisimilitude', 'extant', 'loathe', 'viciate', 'aberration', 'venerate']

outof = len(words)
score = 0
while True:
    choice = random.choice(words)
    print(f'Say the meaning of:{choice}    {score}/{outof}')
    response = input(f'Do you know? ')
    if (response == 'n'):
        if score < outof / 3:
            remark = 'Poor'
        elif score > outof / 3 and score < 2 * outof / 3:
            remark = 'Good'
        elif score > 2 * outof / 3 and score < outof:
            remark = 'Great'
        elif score == outof:
            remark = 'Awesome'
        print(f'You scored {score} out of {outof}.{remark}!!')
        break
    else:
        words.remove(choice)
        score += 1
        if(len(words) == 0):
            print('You scored full!!!!!!!!🤩')
            break
