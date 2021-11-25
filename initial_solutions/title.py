def title_case(title, minor_words=''):
    minor_words = [x.lower() for x in minor_words.split(' ')]
    # print(minor_words)
    return " ".join(x.title() if nm == 0 or not x.lower() in minor_words else x.lower() for nm, x in enumerate(title.split(' ')))

print(title_case('THE WIND IN THE WILLOWS', 'The In'))


# -------------------------------------
def title_case(title, minor_words=''):
    title, minor_words = title.lower().split(), minor_words.lower().split()
    for i in range(len(title)):
        if i == 0 or title[i] not in minor_words:
            title[i] = title[i].capitalize()
    return ' '.join(title)

# -----------------------------
def title_case(title, minor_words=''):
    return ' '.join(
        w if w in minor_words.lower().split() and i else w.capitalize() for i, w in enumerate(title.lower().split()))

