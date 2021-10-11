
import numpy as np


def kohonen(data, k=5, epocas=500, R=5, alpha=0.01):
    Ri = R
    alphai = alpha
    indices = data.index.tolist()
    n = len(data.iloc[indices[0]])
    max_epocas = epocas * n
    epo = 0

    dist = np.zeros([k, k])
    dist_comp = np.zeros([(2 * k) - 1, (2 * k) - 1])

    red = np.zeros([k, k, n])
    for i in range(k):
        for j in range(k):
            red[i, j] = data.sample(n=1)
            dist[i, j] = ((i ** 2) + (j ** 2)) ** 0.5

    dist_comp[(k - 1):, (k - 1):] = dist
    dist_comp[0:k, (k - 1):] = np.flip(dist, axis=0)
    dist_comp[:, 0:k] = np.flip(dist_comp[:, (k - 1):], axis=1)
    dist_comp[k - 1, k - 1] = Ri + 1

    while epo < max_epocas:
        random.shuffle(indices)
        for i in indices:
            m_aux = np.zeros([k, k, n])
            m_aux[:, :] = data.loc[i, :]
            distances = (np.sum(((red - m_aux) ** 2), axis=2) ** (0.5))
            arg = np.unravel_index(np.argmin(distances, axis=None), distances.shape)

            red[arg] = red[arg] + alpha * (data.loc[i, :] - red[arg])

            mascara = dist_comp[k - arg[0] - 1:2 * k - arg[0] - 1, k - arg[1] - 1:2 * k - arg[1] - 1]
            e = np.exp(-2 * mascara[mascara < R] / R).reshape(len(mascara[mascara < R]), 1)
            red[mascara < R, :] = red[mascara < R, :] + alpha * e * (data.loc[i, :].to_numpy() - red[mascara < R, :])

        epo += 1
        if epo % 100 == 0:
            print(epo)
        R = (max_epocas - epo) * Ri / max_epocas
        alpha = alphai * (1 - (epo / max_epocas))
    return red



def prueba_kohonen(red, data):
    M, N = red[:, :, 0].shape
    activacion = np.zeros([M, N])
    indices = data.index.tolist()
    n = len(data.iloc[indices[0]])
    dic = {}

    for i in data.index:
        m_aux = np.zeros([M, N, n])
        m_aux[:, :] = data.loc[i, :]
        distances = (np.sum(((red - m_aux) ** 2), axis=2) ** (0.5))
        arg = np.unravel_index(np.argmin(distances, axis=None), distances.shape)

        if activacion[arg] == 0:
            dic[str(arg[0]) + '_' + str(arg[1])] = [i]
        else:
            dic[str(arg[0]) + '_' + str(arg[1])] = dic[str(arg[0]) + '_' + str(arg[1])] + [i]

        activacion[arg] += 1

    return activacion, dic