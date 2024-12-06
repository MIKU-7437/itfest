import React, {InputHTMLAttributes, ReactNode} from "react";
import cn from "classnames";
import "./index.scss";

interface IInputProps extends InputHTMLAttributes<HTMLInputElement> {
    className?: string;
    classField?: string;
    children?: ReactNode;
}

const Input: React.FC<IInputProps> = ({
                                          className,
                                          classField,
                                          children,
                                          ...rest
                                      }) => {
    return (
        <div className={cn(classField, "field")}>
            <input
                className={cn(className, `field__input`)}
                {...rest}
            />
            {children}
        </div>
    );
};

export default Input;