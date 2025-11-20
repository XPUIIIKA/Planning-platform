import { createSlice } from "@reduxjs/toolkit"

const initialState = {
    mode: 'light'
}

const themeSlice = createSlice({
    name: 'teame',
    initialState,
    reducers: {
        toggleTheme: (state) => {
            state.mode = state.mode === 'light' ? 'dark' : 'light'
        }
    }
});

export const {
    toggleTheme,

 } = themeSlice.actions;
 
export default themeSlice.reducer;