import pandas as pd
#takes in a list of dataframes and outputs the values of the amount of owners and counts
def getOwnersCount(listOfDfs):
    lowerOwners = []
    upperOwners = []
    count = []
    for i in listOfDfs:
        lowerOwners.append(i['llOwners'].sum())
        upperOwners.append(i['ulOwners'].sum())
        count.append(i.shape[0])
    return lowerOwners, upperOwners, count

#takes in a list of dataframes and names for the dataframes and outputs a new dataframe with owners and count 
def createOwnersDF(listOfDfs, names):
    lO, uO, count = getOwnersCount(listOfDfs)
    df = pd.DataFrame({'Type':names,'Lower Limit Owners':lO, 'Upper Limit Owners': uO, 'Count':count})
    df['llAvg'] = df['Lower Limit Owners']/df['Count']
    df['ulAvg'] = df['Upper Limit Owners']/df['Count']
    return df

#plotting the dataframe
def plotOwners(listOfDfs, names, rotation=0):
    df = createOwnersDF(listOfDfs, names)

    ax = df.plot.bar(x = 'Type',y = ['Lower Limit Owners', 'Upper Limit Owners'],rot=rotation, 
                     figsize = (20,10), title="Number of Owners") 
    ax.tick_params(axis = 'both', labelsize=15)
    ax.title.set_size(40)

    ax = df.plot.bar(x = 'Type',y = 'Count',rot=rotation, figsize = (20,10), title = "Number of Games")
    ax.tick_params(axis = 'both', labelsize=15)
    ax.title.set_size(40)
    
    ax = df.plot.bar(x = 'Type',y = ['llAvg','ulAvg'],rot=rotation, figsize=(20,10), title = "Average owners per game")
    ax.tick_params(axis = 'both', labelsize=15)
    ax.title.set_size(40)

#takes in a list of dataframes and outputs the values of avg and median new users and counts
def getAvgMedCount(listOfDfs):
    avg = []
    median = []
    count = []
    for i in listOfDfs:
        avg.append(i['average_forever'].sum())
        median.append(i['median_forever'].sum())
        count.append(i.shape[0])
    return avg, median, count

#takes in a list of dataframes and names for the dataframes and outputs a new dataframe with new users and count 
def createAvgMedDF(listOfDfs, names):
    avg, med, count = getAvgMedCount(listOfDfs)
    df = pd.DataFrame({'Type':names,'Avg New Users':avg, 'Median New Users': med, 'Count':count})
    df['avgAvg'] = df['Avg New Users']/df['Count']
    df['medAvg'] = df['Median New Users']/df['Count']
    return df

#plotting the dataframe
def plotNewOwners(listOfDfs, names, rotation=0):
    df = createAvgMedDF(listOfDfs, names)

    ax = df.plot.bar(x = 'Type',y = ['Avg New Users', 'Median New Users'],rot=rotation, 
                     figsize = (20,10), title="Number of New Owners") 
    ax.tick_params(axis = 'both', labelsize=15)
    ax.title.set_size(40)

    ax = df.plot.bar(x = 'Type',y = ['avgAvg','medAvg'],rot=rotation, figsize=(20,10), 
                     title = "Average new owners per game")
    ax.tick_params(axis = 'both', labelsize=15)
    ax.title.set_size(40)

#removes the average and medians that are 0
def remove0s(df):
    return df[(df.average_forever != 0) & (df.median_forever != 0)]

#counts the number of rows that have an average/median of 0
def count0s(df):
    return df[(df.average_forever == 0) & (df.median_forever == 0)].shape[0]
