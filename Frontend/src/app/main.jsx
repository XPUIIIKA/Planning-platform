import { createRoot } from "react-dom/client";
import "../assets/css/index.css";
import "../assets/css/app.css";
import "../assets/css/theme.css";
import "../assets/css/my.css";
import { Provider } from "react-redux";
import { store } from "../store/store.js";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { RegistrationPage } from "../pages/RegistrationPage.jsx";
import { Layout } from "./Layout.jsx";
import { ThemeProvider } from "../store/providers/ThemeProvider";
import { HomePage } from "../pages/HomePage.jsx";


const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      { path: "", element: <HomePage /> },
      { path: "registration", element: <RegistrationPage /> },
    ],
  },
]);

createRoot(document.getElementById("root")).render(
  <Provider store={store}>
    <ThemeProvider>
      <RouterProvider router={router} />
    </ThemeProvider>
  </Provider>
);
