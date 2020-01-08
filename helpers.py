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
    df['Owner Average'] = (df['Lower Limit Owners'] + df['Upper Limit Owners'])/2
    df['ownerAvg'] = df['Owner Average']/df['Count']
    df['llAvg'] = df['Lower Limit Owners']/df['Count']
    df['ulAvg'] = df['Upper Limit Owners']/df['Count']
    return df

#plotting the dataframe
def plotOwners(listOfDfs, names, horizontal = False,
                rotation=0, title1 = "Number of Owners", title2 = 
                "Number of Games", title3 = "Average Owners per game"):
    df = createOwnersDF(listOfDfs, names)

    if horizontal:
        ax = df.plot.barh(x = 'Type',y = 'Owner Average',rot=rotation, 
                        figsize = (20,10), title=title1, color = 'blue') 
        ax.tick_params(axis = 'both', labelsize=15)
        ax.title.set_size(40)

        ax = df.plot.barh(x = 'Type',y = 'Count',rot=rotation, figsize = (20,10), title = title2
                            , color = 'red')
        ax.tick_params(axis = 'both', labelsize=15)
        ax.title.set_size(40)
        
        ax = df.plot.barh(x = 'Type',y = 'ownerAvg', rot=rotation, figsize=(20,10),color = 'green',
                        title = title3)
        ax.tick_params(axis = 'both', labelsize=15)
        ax.title.set_size(40)
    else:
        ax = df.plot.bar(x = 'Type',y = 'Owner Average',rot=rotation, 
                        figsize = (20,10), title=title1) 
        ax.tick_params(axis = 'both', labelsize=15)
        ax.title.set_size(40)

        ax = df.plot.bar(x = 'Type',y = 'Count',rot=rotation, figsize = (20,10), title = title2)
        ax.tick_params(axis = 'both', labelsize=15)
        ax.title.set_size(40)
        
        ax = df.plot.bar(x = 'Type',y = 'ownerAvg', rot=rotation, figsize=(20,10), 
                        title = title3)
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
def plotNewOwners(listOfDfs, names, horizontal = False, 
                  rotation=0, title1=" Total Average Number of New Owners", 
                  title3="Average new owners per game"):
    df = createAvgMedDF(listOfDfs, names)
    
    if horizontal:
        ax = df.plot.barh(x = 'Type',y = 'Avg New Users',rot=rotation, color = 'blue',
                        figsize = (20,10), title=title1) 
        ax.tick_params(axis = 'both', labelsize=15)
        ax.title.set_size(40)

        ax = df.plot.barh(x = 'Type',y = 'avgAvg',rot=rotation, figsize=(20,10), color = 'red',
                        title = title3)
        ax.tick_params(axis = 'both', labelsize=15)
        ax.title.set_size(40)
    else:
        ax = df.plot.bar(x = 'Type',y = 'Avg New Users',rot=rotation, color = 'blue',
                        figsize = (20,10), title=title1) 
        ax.tick_params(axis = 'both', labelsize=15)
        ax.title.set_size(40)

        ax = df.plot.bar(x = 'Type',y = 'avgAvg',rot=rotation, figsize=(20,10), color = 'red',
                        title = title3)
        ax.tick_params(axis = 'both', labelsize=15)
        ax.title.set_size(40)

#removes the average and medians that are 0
def remove0s(df):
    return df[(df.average_forever != 0) & (df.median_forever != 0)]

#counts the number of rows that have an average/median of 0
def count0s(df):
    return df[(df.average_forever == 0) & (df.median_forever == 0)].shape[0]
