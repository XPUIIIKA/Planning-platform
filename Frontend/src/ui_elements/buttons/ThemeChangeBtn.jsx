import { useDispatch } from "react-redux";
import { toggleTheme } from "../../store/slices/themeSlice";

export function ThemeChangeBtn() {
  const dispatch = useDispatch();

  const handleChangeTheme = () => {
    dispatch(toggleTheme());
  };
  return (
    <button className="btn heder-btn" onClick={handleChangeTheme}>
      <p>Change theme</p>
    </button>
  );
}
