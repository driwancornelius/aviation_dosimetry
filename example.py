import matplotlib.pyplot as plt


# define toy data for altitudes and doses #

altitudes = [0, 500, 1000, 1500] #metres
doses = [0, 7, 21, 28]

# TODO do the same for model data
model_doses = [3, 4, 5, 6]

# TODO import experimental data from csv file

#TODO specify the latitude, longitude, date of the experimnt

#TODO for each altiude in the list

#TODO requestrequest model prediction from API at same conditions

#create plot of experimental and model predicted doses vs aaltitude

fig = plt.figure()

axes = fig.add_subplot(111)

axes.plot(altitudes, doses, label="exp")
axes.plot(altitudes, model_doses, label="model")



axes.set_xlim(left=0)
axes.set_ylim(bottom=0)
axes.set_xlabel("Altitude, m")
axes.set_ylabel("doses, uSv")

plt.legend(loc="lower left")
plt.show()
