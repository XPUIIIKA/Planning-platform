import { useSelector } from "react-redux";

export function LoginLogoutBtn() {
    // const theme = useSelector((state) => state.user.isLogin);

    const logoutBtnHandler = () => {

    }

    const loginBtnHandler = () => {

    }


  return (
    <button className="btn heder-btn" onClick={loginBtnHandler}>
        <p>Login</p>
    </button>
  );
};