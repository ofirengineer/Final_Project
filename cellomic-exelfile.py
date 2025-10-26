import pandas as pd
import numpy as np

df = pd.read_csv('Cells_B3_1.csv')
df_sorted = df.sort_values(by=['ObjectNumber', 'ImageNumber'])
df_sorted.to_csv('Cells_B3_1_SortedByObjectNumber.csv', index=False)

#########################################################################

# טען את טבלת ה-TrackObjects ואת טבלת מיקום האובייקטים (Centers)
track_df = pd.read_csv('Track_B3_1.csv')
cells_df = pd.read_csv('Cells_B3_1.csv')

# שלב 1: הוצאת מיקום ה-X וה-Y של האובייקט הראשון והשני מהטבלה של Cells
# מיזוג נתוני האובייקטים הראשונים
cells_positions = cells_df[['ImageNumber', 'ObjectNumber', 'AreaShape_Center_X', 'AreaShape_Center_Y']]
track_with_first = pd.merge(track_df,
                            cells_positions,
                            left_on=['First Image Number', 'First Object Number'],
                            right_on=['ImageNumber', 'ObjectNumber'],
                            suffixes=('', '_First'))

track_with_first.rename(columns={'AreaShape_Center_X': 'Center_X_First',
                                 'AreaShape_Center_Y': 'Center_Y_First'}, inplace=True)

# מיזוג נתוני האובייקטים השניים
track_with_full = pd.merge(track_with_first,
                           cells_positions,
                           left_on=['Second Image Number', 'Second Object Number'],
                           right_on=['ImageNumber', 'ObjectNumber'],
                           suffixes=('', '_Second'))

track_with_full.rename(columns={'AreaShape_Center_X': 'Center_X_Second',
                                'AreaShape_Center_Y': 'Center_Y_Second'}, inplace=True)

# שלב 2: חישוב המרחק בין האובייקטים (Euclidean Distance)
track_with_full['Distance'] = np.sqrt(
    (track_with_full['Center_X_Second'] - track_with_full['Center_X_First']) ** 2 +
    (track_with_full['Center_Y_Second'] - track_with_full['Center_Y_First']) ** 2
)

# המהירות (פיקסלים לשעה) — שווה למרחק כי הפריים הבא אחרי שעה
track_with_full['Speed_per_Hour'] = track_with_full['Distance']

# שלב 3: הוספת עמודת תאוצה — שינוי במהירות בין פריימים עבור כל אובייקט
track_with_full = track_with_full.sort_values(by=['First Object Number', 'First Image Number']).reset_index(drop=True)
track_with_full['Acceleration'] = track_with_full.groupby('First Object Number')['Speed_per_Hour'].diff()

# שלב 4: שמירת הטבלה
output_path = 'Speed_and_Distance_Table_with_Acceleration.csv'
track_with_full[['First Image Number', 'First Object Number',
                 'Second Image Number', 'Second Object Number',
                 'Center_X_First', 'Center_Y_First',
                 'Center_X_Second', 'Center_Y_Second',
                 'Distance', 'Speed_per_Hour', 'Acceleration']].to_csv(output_path, index=False)

########################################################################################################
import pandas as pd

# שלב 1: טעינת הטבלאות
cells_df = pd.read_csv('Cells_B3_1_SortedByObjectNumber.csv')
speed_df = pd.read_csv('Speed_and_Distance_Table_with_Acceleration.csv')

# שלב 2: מיון שתי הטבלאות לפי ObjectNumber ואז לפי ImageNumber
cells_df_sorted = cells_df.sort_values(by=['ObjectNumber', 'ImageNumber']).reset_index(drop=True)
speed_df_sorted = speed_df.sort_values(by=['First Object Number', 'First Image Number']).reset_index(drop=True)

# שלב 3: הוספת העמודות הרלוונטיות מהטבלה הקטנה אל הטבלה הגדולה
cells_df_sorted['Distance'] = speed_df_sorted['Distance']
cells_df_sorted['Speed_per_Hour'] = speed_df_sorted['Speed_per_Hour']
cells_df_sorted['Acceleration'] = speed_df_sorted['Acceleration']

# שלב 4: שמירת הטבלה המאוחדת
output_path = 'Directly_Merged_Cells_Table.csv'
cells_df_sorted.to_csv(output_path, index=False)

print(f"Finished! Saved merged table to {output_path}")
