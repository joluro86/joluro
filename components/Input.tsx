interface InputProps {
  label: string;
  placeholder?: string;
  type?:"text"|"email"|"password";
}
const Input = ({ label, placeholder, type }: InputProps) => {
  return (
    <label htmlFor="fist-name">
      <span>{label}</span>
      <input type={type} name="fist-name" placeholder={placeholder} />
    </label>
  )
}

export { Input }
