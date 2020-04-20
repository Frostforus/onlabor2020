from numpy.dual import norm


def similarity(a, b):
    if int(a[1]) == int(b[1]):  # első autó edge-e megegyezik-e a másik autó edgével?
        return norm(a[2:4] - b[2:4])  # ha igen, akkor adjuk meg a tavolsagot. dataframe oszlopait címzem itt
    else:
        return 1000000  # egy meglehetosen nagy ertek ami megakadalyozza hogy a nem azonos edge-n levok azonos klaszterben legyenek


class Clusters:
    __slots__ = ["Clusters"]

    def __init__(self):
        self.Clusters = dict()


def find_priority_edge(clus_nom, all_clusters):
    priority_cluster = 0
    biggest_len = 0
    for i in clus_nom:
        if len(all_clusters[i]) > biggest_len:
            biggest_len = len(all_clusters[i])
            priority_cluster = int(i)

    return priority_cluster