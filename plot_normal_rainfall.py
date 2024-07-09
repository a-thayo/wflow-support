# normal rainfall refers to the year with the closest rainfall to average

normal = pd.read_excel(r"PATH TO RAINFALL DATA", index_col=[0], usecols=[0,1,2], parse_dates=[0], date_format="%Y-%m-%d %H:%M:%S")
normalxr = normal.to_xarray()
avg_yr = normalxr["DATAARRAY NAME"].resample(indexer={"Time": "1YE"}).sum()
avg_yr_sg = 2113 # data from gov
factor = avg_yr_sg/avg_yr.mean()

avg_mth = normalxr["DATAARRAY NAME"].resample(Time="1ME").sum().groupby("Time.month").mean()
def to_monthly(ds):
    year = ds.Time.dt.year
    month = ds.Time.dt.month
    # assign new coords
    ds = ds.assign_coords(year=("Time", year.data), month=("Time", month.data))
    # reshape the array to (..., "month", "year")
    return ds.set_index(Time=("year", "month")).unstack("Time") 
avg_mth_yr = to_monthly(normalxr["LCK & Sembawang"].resample(Time="1ME").sum())

yr = []
rmse = []
for year in avg_mth_yr:
    var = (avg_mth - year)**2
    mse = var.mean.values()
    err_tot = mse**0.5
    yr.append(int(year["year"].values))
    rmse.append(float(err_tot))
rmse = np.array(rmse)

# find 5 closest year to average
k = 5
idx = np.argpartition(rmse, k)[:k]
yr_idx = []
for x in idx:
    yr_idx.append(yr[x])

plt.rcParams['axes.prop_cycle'] = plt.cycler(color='bgcmykr')

for year in avg_mth_yr:
    if year["year"] in yr_idx:
        plt.plot(year,"--",alpha=0.8,label=year["year"].values)
    else:
        plt.plot(year,"k--",alpha=0.05)
plt.plot(avg_mth,"r",linewidth=1.7,label="average")
plt.legend()
plt.show()
