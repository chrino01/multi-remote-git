import math
import pandas as pd

##### Activity: Implement the `birthday_probability` function

def birthday_probability(number_of_people):
    pass

### NBA Birthday Paradox Analysis

df = pd.read_csv('nba_2017.csv', parse_dates=['Birth Date'])

df.head()

##### Activity: Create the `Birth Date` column

df['Birth Date'].dt.strftime("%Y-%m-%d").head()

df["Birthday"] = df['Birth Date'].dt.strftime("%m-%d")
df.head()

### Interlude: Combinatorics

For this project, you're free to use any techinque that you prefer to answer how many players share a birthday for a given team. But, one recommendation would be to use combinatorics; specifically the *Combinations*, using the `itertools.combinations` function. Here's a quick example. Suppose we have these samples:

| Name | Birthday  |
|------|-----------|
| John | March 5th |
| Mary | Sept 20th |
| Rob  | March 5th |

Using combinations, we can take all the samples in paris (`r=2`) to compare them:

| Person 1 | Person 2  |
|------|-----------|
| John | Mary |
| John | Rob |
| Mary  | Rob |

Using Python:

from itertools import combinations

names = ["John", "Mary", "Rob"]
birthdays = ["March 5th", "Sept 20th", "March 5th"]

# Note: we need to wrap it in a list to force display
list(combinations(names, 2))

# Note: we need to wrap it in a list to force display
list(combinations(birthdays, 2))

We can see how `March 5th` (John and Rob) are the same dates. Using Pandas:

names_df = pd.DataFrame(combinations(names, 2), columns=["Person 1", "Person 2"])
names_df

birthdays_df = pd.DataFrame(combinations(birthdays, 2), columns=["Birthday 1", "Birthday 2"])
birthdays_df

Combining it:

df = pd.concat([names_df, birthdays_df], axis=1)

df

df['Birthday 1'] == df['Birthday 2']

End of the interlude! Now, it's your turn to answer questions.

---

### Activities

##### How many pairs of players share a birthday for the **Atlanta Hawks**?

atlanta = df.loc[df['Team'] == "Atlanta Hawks"]
atlanta.head()

math.comb(5,2)

player = list(combinations(atlanta['Player'], 2))

at_birthday= list(combinations(atlanta['Birthday'], 2))


player_at = pd.DataFrame(combinations(atlanta['Player'], 2), columns=["Player 1", "Player 2"])
player_at.head()

birthday_at=pd.DataFrame(combinations(atlanta['Birthday'], 2), columns=["birthday 1", "Birthday 2"])
birthday_at.head()

df_at = pd.concat([player_at, birthday_at], axis=1)

df_at

(df_at['birthday 1'] == df_at['Birthday 2']).sum()

##### How many pairs of players share a birthday in the **Cleveland Cavaliers**?

CC= df.loc[df['Team'] == "Cleveland Cavaliers"]
CC.head()

player_cc = pd.DataFrame(combinations(CC['Player'], 2), columns=["Player 1", "Player 2"])
player_cc

birthday_cc=pd.DataFrame(combinations(CC['Birthday'], 2), columns=["birthday 1", "birthday 2"])
birthday_cc

df_cc = pd.concat([player_cc, birthday_cc], axis=1)
df_cc

(df_cc['birthday 1'] == df_cc['birthday 2']).sum()

df_cc.loc[(df_cc['birthday 1'] == df_cc['birthday 2'])]

##### In the **Dallas Mavericks**, who shares a birthday with *J.J. Barea*?

df_DM = df.loc[df['Team'] == "Dallas Mavericks"]
df_DM.head()

df_DM.loc[df_DM['Player']== 'J.J. Barea']

name_DM = pd.DataFrame(list(combinations(df_DM['Player'], 2)), columns=['Player 1', 'Player 2'])
birthday_DM = pd.DataFrame(list(combinations(df_DM['Birthday'], 2)), columns=['Birthday 1', 'Birthday 2'])

check_DM = pd.concat([name_DM,birthday_DM], axis = 1)
check_DM.head()

result =(check_DM['Birthday 1'] == check_DM['Birthday 2']).sum()
result

check_DM.loc[(check_DM['Birthday 1'] == check_DM['Birthday 2'])]

check_DM.loc[(check_DM['Birthday 1'] == check_DM['Birthday 2'])]