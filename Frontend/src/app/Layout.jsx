import { Outlet } from "react-router-dom";
import { Header } from "../compositionsElem/Header";

export function Layout() {
  return (
    <>
      <Header />
      <Outlet />
    </>
  );
}
