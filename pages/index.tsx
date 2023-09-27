import { Button } from "@/components/Button";
import { Input } from "@/components/Input";

const  PaginaPrincipal = () => {
  return <div className="flex flex-col items-center m-20 gap-3">
    <Input label="Primer nombre" placeholder={"Ingresa primer nombre"}/>
    <Input label="Apellidos" placeholder="Ingresa tus apellidos"/>
    <Input label="Correo" type="email"/>
    <Input label="Password" type="password"/>
    <Button/> <br />
    
  </div>;
};

export default PaginaPrincipal; 