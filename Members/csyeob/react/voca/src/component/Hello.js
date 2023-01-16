import { useState } from "react";

export default function Hello() {
    // let name = "Mike";
    // name은 변수이기때문에 리액트에서는 관리해주지않음 웹에선 
    // 그럼 어떻게 state로 만드냐 --> useState를 사용해야함.
    const [name, setName] = useState('Mike');

    // function changeName(){
    //     // const newName = name === "Mike" ? "Jane" : "Mike"; // Mike 일땐 Jane으로 Jane일땐 Mike로
    //     console.log(name); // 웹에선 업데이트가 되지않음 이상태면
    //     // dom 업데이트 작업도 해줘야함.
    //     //document.getElementById("name").innerText = name;
    //     //setName(newName);
    //     setName(name === "Mike" ? "Jane" : "Mike");
    //     //<button onClick={changeName}>Change</button>
    // }
    return (
     <div>
        <h2 id = "name">{name}</h2>
        <button onClick={()=>{
            setName(name === "Mike" ? "Jane" : "Mike");
        }}>Change</button>
     </div>
    );
}
// event
