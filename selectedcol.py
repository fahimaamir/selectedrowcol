import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import ColumnsAutoSizeMode
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode
data = {
    'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia'],
    'Country': ['USA', 'USA', 'Canada', 'Germany', 'France', 'Japan', 'China'],
    'City': ['New York', 'Los Angeles', 'Toronto', 'Berlin', 'Paris', 'Tokyo', 'Beijing'],
    'rate': [54,76,345,6786,67868, 65765, 675]
    }

df = pd.DataFrame(data)


gb = GridOptionsBuilder.from_dataframe(df)
for column in df.columns:
    gb.configure_column(column, filter=True)
gb.configure_selection(selection_mode="multiple", use_checkbox=True, pre_selected_rows=None,  )
gridOptions = gb.build()
mfa = AgGrid(
        df,
        gridOptions=gridOptions,
        update_mode=GridUpdateMode.GRID_CHANGED,
        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
        data_return_mode=DataReturnMode.FILTERED   # <-- Gets filtered data, but not filters applied to columns
    )
#mfa = AgGrid(df, gridOptions=gridOptions,              update_mode=GridUpdateMode.MODEL_CHANGED)



if st.button('Check availability'):
    mfa4 =mfa['data']
    fild = pd.DataFrame(mfa['columns_state'])
    above_35= fild["hide"] 
    above_36= fild["colId"] 
    list_from_df = above_36.values.tolist()
    list_from_column = fild["colId"].tolist()
    fild["hide"] = fild["hide"].astype(int) 
    fild = fild[fild["hide"]==0 ]
    list_from_df2 = fild["colId"].values.tolist()
    mfa5 = mfa4[list_from_column]
    mfa6 = mfa4[list_from_df2]
    st.write(mfa5)
    st.write(mfa6)
