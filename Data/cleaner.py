import pandas as pd

# Fix Dates
fh = 'F:\\Research\\Funded\\UIREEJ\\Flint_River_Ecology\\Data\\Dates.csv'
df = pd.read_csv(fh)

# Replace Weather IDs with Verbal.
df['Weather'] = df['Weather'].replace([1.0],'Sunny')
df['Weather'] = df['Weather'].replace([2.0],'Partly-Cloudy')
df['Weather'] = df['Weather'].replace([3.0],'Cloudy')

# Map DateTimes.
df['Date'] = df[['Year', 'Month', 'Day']].astype(str).apply(lambda x: '/'.join(x), axis=1)

# Overwrite, Pickle
df.to_csv(fh, index=False)
dates = pd.read_csv(fh)
dates.to_pickle('F:\\Research\\Funded\\UIREEJ\\Flint_River_Ecology\\Data\\Dates.pkl')

# Fix Effort
fh = 'F:\\Research\\Funded\\UIREEJ\\Flint_River_Ecology\\Data\\Effort.csv'
df = pd.read_csv(fh)

# Replace Gear IDs w/ Gear Name.
df['Fishing_Gear'] = df['Fishing Gear']
df['Fishing_Gear'] = df['Fishing_Gear'].replace([1.0],'Hoop trap')
df['Fishing_Gear'] = df['Fishing_Gear'].replace([2.0],'Electrofishing')
df['Fishing_Gear'] = df['Fishing_Gear'].replace([3.0],'Cast Net')
df['Fishing_Gear'] = df['Fishing_Gear'].replace([4.0],'Hook and Line')
df['Fishing_Gear'] = df['Fishing_Gear'].replace([5.0],'Gill net')

# Replace Site IDs w/ Site Verbal.
df['_Site'] = df['Site']
df['_Site'] = df['_Site'].replace([1.0],'South Down-Stream')
df['_Site'] = df['_Site'].replace([2.0],'South Up-Stream')
df['_Site'] = df['_Site'].replace([3.0],'North Down-Stream')
df['_Site'] = df['_Site'].replace([4.0],'North Up-Stream')

# Replace Day IDs w/ DateTime.
df['Fishing_Day']  = df['Fishing Day']
for date in dates.values:
    date_id = date[0]
    date_date = date[-1]
    df['Fishing_Day'] = df['Fishing_Day'].replace([date_id],date_date)

# Overwrite, Pickle
df.to_csv(fh, index=False)
effort = pd.read_csv(fh)
effort.to_pickle('F:\\Research\\Funded\\UIREEJ\\Flint_River_Ecology\\Data\\Effort.pkl')

# Fix Catch 
fh = 'F:\\Research\\Funded\\UIREEJ\\Flint_River_Ecology\\Data\\Catch.csv'
df = pd.read_csv(fh)

# Replace Gear IDs w/ Gear Name.
df['Fishing_Gear'] = df['Fishing Gear']
df['Fishing_Gear'] = df['Fishing_Gear'].replace([1.0],'Hoop trap')
df['Fishing_Gear'] = df['Fishing_Gear'].replace([2.0],'Electrofishing')
df['Fishing_Gear'] = df['Fishing_Gear'].replace([3.0],'Cast Net')
df['Fishing_Gear'] = df['Fishing_Gear'].replace([4.0],'Hook and Line')
df['Fishing_Gear'] = df['Fishing_Gear'].replace([5.0],'Gill net')
df['Fishing_Gear'] = df['Fishing_Gear'].replace([6.0],'Dip net')

# Replace Species IDs w/  Nomenclature.
df['_Species'] = df['Species']
df['_Species'] = df['_Species'].replace([0.0],'Unknown')
df['_Species'] = df['_Species'].replace([1.0],'Common carp')
df['_Species'] = df['_Species'].replace([2.0],'Smallmouth bass')
df['_Species'] = df['_Species'].replace([3.0],'Largemouth bass')
df['_Species'] = df['_Species'].replace([4.0],'Rock bass')
df['_Species'] = df['_Species'].replace([5.0],'Bluegill')
df['_Species'] = df['_Species'].replace([6.0],'Gizzard shad')
df['_Species'] = df['_Species'].replace([7.0],'Black bullhead')
df['_Species'] = df['_Species'].replace([8.0],'Green sunfish')
df['_Species'] = df['_Species'].replace([9.0],'Yellow perch')
df['_Species'] = df['_Species'].replace([10.0],'Round goby')
df['_Species'] = df['_Species'].replace([11.0],'Pumpkinseed sunfish')
df['_Species'] = df['_Species'].replace([12.0],'Black crappie')
df['_Species'] = df['_Species'].replace([13.0],'White sucker')
df['_Species'] = df['_Species'].replace([14.0],'Warmouth')
df['_Species'] = df['_Species'].replace([15.0],'Walleye')
df['_Species'] = df['_Species'].replace([16.0],'White bass')
df['_Species'] = df['_Species'].replace([17.0],'Quillback')
df['_Species'] = df['_Species'].replace([18.0],'Channel catfish')
df['_Species'] = df['_Species'].replace([19.0],'Freshwater drum')
df['_Species'] = df['_Species'].replace([20.0],'Redhorse')
df['_Species'] = df['_Species'].replace([21.0],'Brown bullhead')
df['_Species'] = df['_Species'].replace([22.0],'Northern Pike')
df['_Species'] = df['_Species'].replace([23.0],'Bowfin')
df['_Species'] = df['_Species'].replace([24.0],'Northern Logperch')
df['_Species'] = df['_Species'].replace([25.0],'Yellow Bullhead')
df['_Species'] = df['_Species'].replace([26.0],'White Crappie')
df['_Species'] = df['_Species'].replace([27.0],'Common Shinner')
df['_Species'] = df['_Species'].replace([28.0],'Bigmouth Buffalo')
df['_Species'] = df['_Species'].replace([29.0],'White Perch')
df['_Species'] = df['_Species'].replace([30.0],'Emmerald Shinner')
df['_Species'] = df['_Species'].replace([31.0],'Mirror Carp')
df['_Species'] = df['_Species'].replace([32.0],'Goldfish')
df['_Species'] = df['_Species'].replace([33.0],'Longnose Gar')

# Replace Day IDs w/ DateTime.
df['Fishing_Day'] = df['Fishing Day']
for date in dates.values:
    date_id = date[0]
    date_date = date[-1]
    df['Fishing_Day'] = df['Fishing_Day'].replace([date_id],date_date)

# Replace Site IDs w/ Verbal.
df['Site']  = df['Site'].replace([11.0],1.0)
df['_Site'] = df['Site']
df['_Site'] = df['_Site'].replace([1.0],'South Down-Stream')
df['_Site'] = df['_Site'].replace([2.0],'South Up-Stream')
df['_Site'] = df['_Site'].replace([3.0],'North Down-Stream')
df['_Site'] = df['_Site'].replace([4.0],'North Up-Stream')

# Ease of Access
df['Weight'] = df['Weight (kg)']
df['Length'] = df['Length (cm)']

# Overwrite, Pickle
df.to_csv(fh, index=False)
catch = pd.read_csv(fh)
catch.to_pickle('F:\\Research\\Funded\\UIREEJ\\Flint_River_Ecology\\Data\\Catch.pkl')