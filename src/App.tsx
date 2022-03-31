import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { UserContextProvider } from "./context/userContext";
import PrivateRoute from "./PrivateRoute";
import Index from "./views/Index";
import { Login } from "./views/Login";
import { Monedero } from "./views/Monedero";
import { Register } from "./views/Register";
import { ResetPassword } from "./views/ResetPassword";

function App() {
  return (
    <UserContextProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Index />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route
            path="/monedero"
            element={<PrivateRoute children={<Monedero />} />}
          />
          <Route path="/reset-password" element={<ResetPassword />} />
          <Route path="*" element={<p>Ruta no encontrada</p>} />
        </Routes>
      </Router>
    </UserContextProvider>
  );
}

export default App;
