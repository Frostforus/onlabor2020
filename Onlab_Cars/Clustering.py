from numpy.dual import norm
import traci
from math import *


def similarity(a, b):
    if int(a[1]) == int(b[1]):  # első autó edge-e megegyezik-e a másik autó edgével?
        return norm(a[2:4] - b[2:4])  # ha igen, akkor adjuk meg a tavolsagot. dataframe oszlopait címzem itt
    else:
        return 1000000  # egy meglehetosen nagy ertek ami megakadalyozza hogy a nem azonos edge-n levok azonos klaszterben legyenek


class Clusters:
    __slots__ = ["Clusters"]

    def __init__(self):
        self.Clusters = dict()


def find_priority_edge(clus_nom, all_clusters, current_prio, tls_x, tls_y):
    # TODO: Távolság alapján is nézni
    # Ha még létezik a current_prio akkor az legyen a benchmark
    if current_prio in all_clusters:
        priority_cluster = current_prio

        current_distance = find_distance(current_prio, all_clusters, tls_x, tls_y)
        biggest_weight = (len(all_clusters[current_prio]) / max(current_distance, 1)) * 1.1  # Súlyozzás
    # Ha nem akkor biztosan új lesz
    else:
        priority_cluster = 0
        biggest_weight = 0

    for i in clus_nom:
        # print("Cluster id:", i)
        distance_from_tls = find_distance(i, all_clusters, tls_x, tls_y)
        # print("Distance from TLS:", distance_from_tls)

        candidate_weight = len(all_clusters[i]) / max(distance_from_tls, 1)
        if candidate_weight > biggest_weight:
            biggest_weight = candidate_weight
            priority_cluster = int(i)

    return priority_cluster


def find_distance(cluster_id, all_clusters, tls_x, tls_y):
    if cluster_id in all_clusters:
        x_cluster = 0
        y_cluster = 0
        cluster_len = len(all_clusters[cluster_id])
        # print("\ntlsx:{}, tlsy {}".format(tls_x, tls_y))
        for i in all_clusters[cluster_id]:
            x, y = traci.vehicle.getPosition(i)
            x_cluster += x
            y_cluster += y
        # print("\nx: {} y: {} \nclusterx:{}, clustery {}".format(x, y, x_cluster, y_cluster))

        x_cluster = x_cluster / cluster_len
        y_cluster = y_cluster / cluster_len

        return sqrt((tls_x - x_cluster) ** 2 + (tls_y - y_cluster) ** 2)

    else:
        return 100000
