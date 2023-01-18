import { useState } from 'react';

export default function Word({word:w}) {
    //word:w => 새로운 변수명 w로 할당 props로 넘어온 변수를 w로 사용하겠다 의미
    const [word, setWord] = useState(w);
    const [IsShow, setIsShow] = useState(false);
    const [isDone, setIsDone] = useState(word.isDone);
    function toggleShow(){
        setIsShow(!IsShow)
    }
    function toggleDone(){
        //setIsDone(!isDone);
        // UPdate - PUT
        fetch(`http://localhost:3002/words/${word.id}`,{
            method:'PUT',
            headers: {
                'Content-Type' : 'application/json',
            },
            body : JSON.stringify({
                ...word,
                isDone: !isDone,
            }),
        })
        .then(res => {
            if(res.ok){
                setIsDone(!isDone);
            }
        });
    }
    // DELETE

    function del() {
        if(window.confirm('삭제하시겠습니까?')){
            fetch(`http://localhost:3002/words/${word.id}`,{
                method:'DELETE',
            }).then(res=>{
                if(res.ok){
                    setWord({id:0})
                }
            });
        }
    }
    if (word.id == 0){
        return null;
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
            <button onClick={del} className ="btn_del" >삭제</button>
        </td>
    </tr >
    );
}