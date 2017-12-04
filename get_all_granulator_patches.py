import numpy as np
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    delta = 0.1
    iteration = 0.0

    totalIterations = ((1.0 / delta) + 1) ** 6
    print "Total iterations: " + str(totalIterations)
    all_patches = []

    a = 0.0
    while a <= 1.0:
        b = 0.0
        while b <= 1.0:
            c = 0.0
            while c <= 1.0:
                d = 0.0
                while d <= 1.0:
                    e = 0.0
                    while e <= 1.0:
                        f = 0.0
                        while f <= 1.0:
                            parameters = [a, b, c, d, e, f]
                            all_patches += [parameters]
                            iteration += 1.0
                            print str(int(iteration)) + "/" + str(int(totalIterations)) + " Done"
                            f += delta
                        e += delta
                    d += delta
                c += delta
            b += delta
        a += delta

    np.save("data/gran/all_patches.npy", np.array(all_patches))
