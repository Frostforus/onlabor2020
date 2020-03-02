from numpy.dual import norm


def similarity(a, b):
    if int(a[1]) == int(b[1]):  # első autó edge-e megegyezik-e a másik autó edgével?
        return norm(a[2:4] - b[2:4])  # ha igen, akkor adjuk meg a tavolsagot. dataframe oszlopait címzem itt
    else:
        return 1000000  # egy meglehetosen nagy ertek ami megakadalyozza hogy a nem azonos edge-n levok azonos klaszterben legyenek
