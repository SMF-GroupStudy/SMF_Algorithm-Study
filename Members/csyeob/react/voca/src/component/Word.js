import { useState } from 'react';

export default function Word({ word }) {
    const [IsShow, setIsShow] = useState(false);
    const [isDone, setIsDone] = useState(word.isDone);
    function toggleShow(){
        setIsShow(!IsShow)
    }
    function toggleDone(){
        setIsDone(!isDone);
    }

    return (
        <tr className={isDone ? "off" : ""}>
        <td><input type="checkbox" checked = {isDone} onChange = {toggleDone}></input></td>
        <td>{word.eng}</td>
        <td>{IsShow && word.kor}</td>
        <td>
            <button onClick={toggleShow}>
                뜻 {IsShow ? "숨기기" :"보기"}
            </button>
            <button className ="btn_del">삭제</button>
        </td>
    </tr >
    );
}