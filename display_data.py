import sys
import os
import cPickle as pickle
import matplotlib.pyplot as plt
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
from utility_functions import display_stats, plot_error, write_wavs

folder = "five_operator"
all_models_error = pickle.load(open("stats/" + folder + "/all_models_error.p", "rb")).items()

try:
    all_ga_error = pickle.load(open("stats/" + folder + "/ga_models_error.p", "rb")).items()
    all_models_error.extend(all_ga_error)
except:
    pass

try:
    all_hills_error = pickle.load(open("stats/" + folder + "/all_hills_error.p", "rb")).items()
    all_models_error.extend(all_hills_error)
except:
    pass

# Based on: http://stackoverflow.com/a/35971096/5398272
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

for i in range(len(all_models_error)):
    (label, error) = all_models_error[i]
    if len(error) > 0:
        ax1.plot(error, label=label)

colormap = plt.cm.Set2
colors = [colormap(i) for i in np.linspace(0, 1, len(ax1.lines))]
for i, j in enumerate(ax1.lines):
    j.set_color(colors[i])
ax1.legend(loc=2)
plt.show()







# hill_climber_stats = pickle.load(open("stats/hill_climber.p", "rb"))


    # display_stats(ga_stats)
    # plot_error(model_errors['ga'])
    # write_wavs("ga",
    #            ga_stats[1]['predicted_features'],
    #            ga_stats[1]['actual_features'],
    #            extractor)
    #
    # display_stats(lstm_stats)
    # plot_error(model_errors['lstm'])
    # write_wavs("lstm",
    #            lstm_stats[1]['predicted_features'],
    #            lstm_stats[1]['actual_features'],
    #            extractor)
