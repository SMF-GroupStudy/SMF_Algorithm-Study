import { useState } from "react";
import UserName from "./UserName";

export default function Hello({age}) {
    //console.log(props);
    const [name, setName] = useState('Mike');
    // 그냥 컴포넌트에 짚어 넣게 되면 props는 바꿀수 없음.
    // <h2 id = "name">{name}({props.age}세)</h2> 밑에 return문에 작성함.
    // props.age = 100;
    // 위 코드는 에러임 props는 저렇게 못바꿈.
    // const [age, setAge] = useState(props.age);
    // 위코드는 Hello(props){}

    const msg = age > 19 ?  '성인입니다.':'미성년자 입니다.';

    return (
     <div>
        <h2 id = "name">{name}({age}) : {msg}</h2>
        <UserName name = {name} />
        {/* return 문 전체를 보자면 {name}은 useState인데, 
            UserName 입장에서 보면 props임.
        */}
        <button onClick={()=>{
            setName(name === "Mike" ? "Jane" : "Mike");
            //setAge(age + 1);
       }}>Change</button>
     </div>
    );
}
// event
