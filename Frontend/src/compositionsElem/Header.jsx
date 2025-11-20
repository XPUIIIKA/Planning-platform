import { LoginLogoutBtn } from "../ui_elements/buttons/LoginLogoutBtn";
import { MeInfoBtn } from "../ui_elements/buttons/MeInfoBtn";
import { SetingsBtn } from "../ui_elements/buttons/SetingsBtn";
import { ThemeChangeBtn } from "../ui_elements/buttons/ThemeChangeBtn";

export function Header() {
  return (
    <div className="header">
        <div className="header-left-btns">
            <MeInfoBtn />
            <SetingsBtn />
        </div>
        <h1>Ne Notion</h1>
        <div className="header-right-btns">
            <LoginLogoutBtn />
            <ThemeChangeBtn />
        </div>
    </div>
  );
};